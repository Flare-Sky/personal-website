# 寄居者的日记 ｜ Sojourner's Diary 🖋️

这是我的个人静态博客仓库，记录了我2023年至今的生活、学习、探索与奇遇。

> 亲爱的弟兄啊，你们是客旅，是寄居的。(彼得前书 2:11a)

---

## 🛠️ 技术栈（Tech Stack）

* **框架: ** [Hugo](https://gohugo.io/) (v0.146.0+ Extended)
* **主题: ** [PaperMod](https://github.com/adityatelange/hugo-PaperMod)
* **部署: ** GitHub Actions & GitHub Pages
* **统计: ** 不蒜子 (Busuanzi) 阅读量统计
* **语言: ** Markdown + TOML (支持 CJK 汉字统计)

## 📂 目录结构 (Project Structure)

```text
.
├── content/            # 所有的日记与文章 (.md)
│   ├── posts/          # 日记正文
│   └── archives.md     # 归档页面配置
├── static/             # 静态资源 (Favicon, 图片等)
├── themes/             # Hugo 主题 (PaperMod)
├── layouts/            # 覆盖主题的自定义布局
└── .github/workflows/  # GitHub Actions 自动化部署脚本

```

## 🚀 本地开发 (Local Development)
如果你想在本地运行或预览我的日记，请确保你已安装了 **Hugo Extended** 版本：
1. **克隆仓库**

```bash
git clone https://github.com/Flare-Sky/Flare-Sky.github.io.git
cd Flare-Sky.github.io
```

2. **启动本地服务器**

```bash
hugo server -D
```

3. **访问预览**
在浏览器打开 **http://localhost:1313/**

## 📝 自动化部署流程（CI/CD）
本项目配置了 GitHub Actions。每次我执行 **git push** 时，后台会自动：
1. 拉取最新版本的 Hugo 环境。
2. 构建静态 HTML 网页。
3. 将其部署到 **gh-pages** 分支并同步到[flare-sky.github.io](https://flare-sky.github.io)。

## 📬 联系我（Contact Me）
* GitHub: [@Flare-Sky](https://github.com/Flare-Sky)
* 个人网址: <https://flare-sky.github.io>

© 2026 Flare-Sky. 基于 MIT 协议开放源代码（文章内容保留版权）。
