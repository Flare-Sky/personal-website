# 寄居者的日记 (Journal of a Sojourner)

> 亲爱的弟兄啊，你们是客旅，是寄居的。(彼得前书 2:11a)

这是一个基于 Hugo 构建的个人静态博客。它不仅是记录生活、思考与技术的数字花园，也是一个持续迭代的前端工程实践项目。

## 🛠 Tech Stack (技术栈)

* **Framework:** [Hugo](https://gohugo.io/) (静态网站生成器)
* **Theme:** [PaperMod](https://github.com/adityatelange/hugo-PaperMod) (深度魔改定制版)
* **Deployment:** GitHub Pages & GitHub Actions (自动化 CI/CD 部署)
* **Data Visualization:** Chart.js
* **Analytics:** Busuanzi (不蒜子极简统计)

## ✨ Key Features (核心魔改特性)

本博客在原版 PaperMod 主题的基础上，进行了深度的 UI 重构与逻辑覆写：

* **Parallax Scrolling Home Page (视差滚动首页):** * 采用“固定背景层 + 悬浮实体卡片层”的三明治架构。
  * 实现了移动端与 PC 端完美兼容的物理级滑动阻尼感，彻底消除了底部文字穿帮问题。
  * 注入原生 JS 实现了背景文字的滚动动态渐隐特效 (Scroll Fade-out)。
* **Interactive Archive Chart (数据驱动的动态归档):** * 在归档页 (`/archives`) 引入 Chart.js。
  * 在 Hugo 编译阶段利用 `.GroupByDate` 处理后端数据，由前端渲染发布频率柱状图。
  * 支持图表点击事件与平滑滚动联动，精准定位至特定月份目录。
* **Advanced Pagination UI (优雅的分页体验):** * 利用 CSS `scroll-margin-top` 与锚点定位 (`Anchor Fragment`) 配合，确保翻页时页面精准停留在目录上方，避免被冻结的导航栏遮挡，保持沉浸式阅读心流。
* **Custom Markdown Components (自定义短代码):** * 封装了 `<details>` 折叠框 Shortcode，专门用于优雅地展示解谜游戏 (如 CTF、Puzzle Hunts) 的提示与答案，解决原生 Markdown 解析器嵌套 HTML 的缩进失效问题。

## 🚀 Local Deployment (本地运行)

如果你想在本地预览这个项目：

1. **克隆本仓库 (包含子模块)**
    ```bash
    git clone --recurse-submodules [https://github.com/Flare-Sky/Flare-Sky.github.io](https://github.com/Flare-Sky/Flare-Sky.github.io)
    cd Flare-Sky.github.io
    ```

2. **启动本地服务器**

    ```bash
    hugo server -D
    ```

3. **访问预览**
在浏览器打开 `http://localhost:1313/`

## 📬 联系我（Contact Me）

* GitHub: [@Flare-Sky](https://github.com/Flare-Sky)
* 个人网址: <https://flaresky.me>

© 2026 Flare-Sky. 基于 MIT 协议开放源代码（博客文章与个人图片等内容版权归作者所有）。
