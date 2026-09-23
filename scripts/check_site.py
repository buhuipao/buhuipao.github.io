"""Build both deployments and check the published ad boundaries and examples."""

import re
import subprocess
import sys
import tempfile
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PUBLISHER = "ca-pub-3487149104434430"
PRIMARY = "https://blog.buhuipao.com/"
MIRROR = "https://buhuipao.github.io/"
ADS_TXT = "google.com, pub-3487149104434430, DIRECT, f08c47fec0942fa0"


class Page(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.ads = []
        self.accounts = []
        self.canonicals = []
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "script" and "adsbygoogle.js" in attrs.get("src", ""):
            self.ads.append(attrs["src"])
        if tag == "meta" and attrs.get("name") == "google-adsense-account":
            self.accounts.append(attrs.get("content"))
        if tag == "link" and attrs.get("rel") == "canonical":
            self.canonicals.append(attrs.get("href"))


def check():
    reviewed, drafts = {}, []
    for source in (ROOT / "content/post").glob("*.md"):
        _, frontmatter, body = source.read_text().split("---", 2)
        url = re.search(r"^url: (.+)$", frontmatter, re.M).group(1)
        if re.search(r"^draft: true$", frontmatter, re.M):
            drafts.append(url)
        elif re.search(r"^ads: true$", frontmatter, re.M):
            reviewed[url] = source
            blocks = re.findall(r"^```python\n(.*?)^```", body, re.M | re.S)
            assert blocks, f"No runnable example: {source}"
            subprocess.run(
                [sys.executable, "-c", "\n\n".join(blocks)],
                check=True, timeout=30, cwd=ROOT,
            )
    assert reviewed, "No reviewed articles found"
    assert drafts, "Expected the republished articles to remain drafts"
    assert (ROOT / "static/ads.txt").read_text().strip() == ADS_TXT

    with tempfile.TemporaryDirectory(prefix="buhuipao-check-") as tmp:
        for index, base in enumerate((PRIMARY, MIRROR)):
            output = Path(tmp) / str(index)
            subprocess.run(
                ["hugo", "--baseURL", base, "--destination", str(output),
                 "--cacheDir", str(Path(tmp) / "cache")],
                check=True, cwd=ROOT,
            )
            actual_ads = set()
            for path in output.rglob("*.html"):
                page = Page(path.read_text())
                if page.ads:
                    actual_ads.add(path.relative_to(output).as_posix())
                    assert len(page.ads) == 1 and PUBLISHER in page.ads[0], path
            expected = {url.lstrip("/") + "index.html" for url in reviewed}
            assert actual_ads == (expected if base == PRIMARY else set()), actual_ads
            for url in ["/", "/about/", "/privacy/", *reviewed]:
                page = Page((output / url.lstrip("/") / "index.html").read_text())
                assert page.accounts == [PUBLISHER], url
                if url != "/":
                    assert page.canonicals == [PRIMARY.rstrip("/") + url], url
            sitemap = (output / "sitemap.xml").read_text()
            for url in drafts:
                assert not (output / url.lstrip("/")).exists(), url
                assert url not in sitemap, url
            assert "noindex" in (output / "404.html").read_text()
            assert (output / "robots.txt").is_file()
            assert (output / "ads.txt").read_text().strip() == ADS_TXT
            print(f"OK: {base} — {len(actual_ads)} ad pages, {len(drafts)} drafts excluded")


if __name__ == "__main__":
    check()
