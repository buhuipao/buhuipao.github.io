# 部署说明

本博客同时部署在两个平台，对应两个域名：

| 平台 | 域名 | 部署方式 |
|------|------|----------|
| Cloudflare Pages | `blog.buhuipao.com` / `buhuipao-github-io.pages.dev` | 自动：push 到 `hugo` 分支后 Cloudflare 自动构建 |
| GitHub Pages | `buhuipao.github.io` | 手动：需要本地运行构建脚本生成 `docs/` 目录后 push |

## 日常发布流程

```bash
# 1. 编辑文章
#    content/post/YYYY-MM-DD-slug.md

# 2. 本地预览
hugo server -D

# 3. 构建 GitHub Pages 所需的 docs/ 目录
bash scripts/build.sh

# 4. 提交并推送
git add .
git commit -m "feat: 发布新文章"
git push origin hugo
```

push 后：
- **Cloudflare Pages** 会自动拉取 `hugo` 分支并构建部署，无需额外操作
- **GitHub Pages** 从仓库的 `docs/` 目录提供服务，所以 push 前必须先跑 `scripts/build.sh`

## 构建脚本

`scripts/build.sh` 的作用：
1. 运行 `hugo` 生成正式站点到 `public/`，不发布 `draft: true` 的文章
2. 将 `public/` 重命名为 `docs/`（GitHub Pages 的部署目录）

配置文件的默认 `baseURL` 是博客站 `https://blog.buhuipao.com/`，Cloudflare Pages 使用博客站地址构建。`scripts/build.sh` 默认使用 `https://buhuipao.github.io/`，也支持通过环境变量覆盖：

```bash
HUGO_BASEURL="https://blog.buhuipao.com/" bash scripts/build.sh
```

## 域名与顶层站点

- `buhuipao.com`（及 `www`）现在是个人主页，不再是本博客；博客只在新域名 `blog.buhuipao.com` 提供
- 旧地址（`buhuipao.com/2016/*`、`/2017/*`、`/2023/*`，以及 `/post`、`/categories`、`/tags`、`/about`、`/privacy`、`/link`、`/index.xml`，含不带结尾斜杠的形式）由主页仓库 `buhuipao/homepage` 根目录的 `_redirects` 301 到对应子域路径；博客新增年份目录或顶层路径时，必须在 `_redirects` 中补一条规则
- GitHub Pages 镜像仍为 `buhuipao.github.io`，正文 canonical 统一指向 `blog.buhuipao.com`

## 注意事项

- `docs/` 必须提交到 Git（不在 .gitignore 中），否则 GitHub Pages 无内容可部署
- `public/` 和 `resources/_gen/` 在 .gitignore 中，不会被提交
- Cloudflare Pages 不依赖 `docs/` 目录，它自己运行 Hugo 构建
- Cloudflare Pages 的生产构建命令必须使用 `hugo`，不能带 `-D` / `--buildDrafts`；`HUGO_BASEURL` 如已设置，应为 `https://blog.buhuipao.com/`

## 内容与 AdSense

- `static/ads.txt` 保留现有发布商记录；网站所有权验证使用全站的 `google-adsense-account` 元标签
- 广告脚本仅在主站、`type: post` 且明确设置 `ads: true` 的正文页加载。首页、分类、标签、信息页、未指定广告的旧笔记和 GitHub Pages 镜像不加载广告脚本
- 开启单篇广告前，检查来源、正文的实际价值、示例能否运行以及引用是否清楚。`ads: true` 是本站的编辑选择，不代表 Google 已批准该文章
- 当前三篇明确转载的网络基础和 Linux 进程文章设为草稿，源码保留；有实质原创分析后再考虑发布。请勿为复审使用包含草稿的构建
- 四篇已修订教程在原 URL 上补充了分析、边界案例和运行检查，并使用 `lastmod` 标注修订日期
- `params.canonicalBaseURL` 为 `https://blog.buhuipao.com/`，正文的 canonical 统一指向博客站，镜像保留访问能力
- 隐私说明位于 `/privacy/`，联系与纠错入口位于 `/about/`

运行 `python3 scripts/check_site.py` 检查两个域名的构建、广告范围、草稿排除、验证信息及教程示例。已在 Hugo 0.158.0、Python 3.9.13、macOS 上验证；检查需要 Python 3.9+、Hugo，以及支持 `os.fork` 的 macOS/Linux。

复审前先部署并检查线上首页、教程和 `ads.txt`，确认生产构建排除了草稿。AdSense 仍会评估整个站点的内容，关闭部分页面的广告不能代替内容质量整改。只有确认线上问题已处理，才在 AdSense 网站详情中勾选“我确认已解决相关问题”并申请审核。涉及地区同意要求的广告投放，应同时在 AdSense 的“隐私权和消息”中完成适用设置。

参考：[复制内容政策](https://support.google.com/publisherpolicies/answer/11190248)、[网站内容与体验要求](https://support.google.com/adsense/answer/7299563)、[隐私披露要求](https://support.google.com/adsense/answer/1348695)。
