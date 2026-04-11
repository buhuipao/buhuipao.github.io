# 部署说明

本博客同时部署在两个平台，对应两个域名：

| 平台 | 域名 | 部署方式 |
|------|------|----------|
| Cloudflare Pages | `buhuipao.com` / `buhuipao-github-io.pages.dev` | 自动：push 到 `hugo` 分支后 Cloudflare 自动构建 |
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
1. 运行 `hugo -D` 生成站点到 `public/`
2. 将 `public/` 重命名为 `docs/`（GitHub Pages 的部署目录）

支持通过环境变量覆盖 `baseURL`：

```bash
HUGO_BASEURL="https://buhuipao.com/" bash scripts/build.sh
```

## 注意事项

- `docs/` 必须提交到 Git（不在 .gitignore 中），否则 GitHub Pages 无内容可部署
- `public/` 和 `resources/_gen/` 在 .gitignore 中，不会被提交
- Cloudflare Pages 不依赖 `docs/` 目录，它自己运行 Hugo 构建
