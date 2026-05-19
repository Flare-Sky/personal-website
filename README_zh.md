<div align="right">
  <a href="./README.md">English</a> | <strong>中文</strong>
</div>

# 寄居者的日记

> 亲爱的弟兄啊，你们是客旅，是寄居的。(彼得前书 2:11a)

这是一个基于 Hugo 构建的个人静态博客，旨在成为一个集生活记录、技术分享与前端工程实践于一体的数字花园。本项目的核心目标是展示现代前端开发的最佳实践，并通过持续迭代提升用户体验与技术深度。

## 💡 项目亮点

本项目在 [PaperMod](https://github.com/adityatelange/hugo-PaperMod) 主题基础上进行了深度定制与功能扩展，引入了多项创新特性：

* **沉浸式视差滚动首页:** 采用独特的“固定背景层 + 悬浮实体卡片层”三明治架构，实现了桌面与移动端设备间的完美兼容与流畅的物理级滑动阻尼感。通过原生 JavaScript 精心调校，实现了背景文字的智能滚动渐隐效果，极大提升了视觉沉浸感与交互体验。
* **数据驱动的动态归档:** 在归档页 (`/archives`) 集成了 Chart.js，于 Hugo 编译阶段利用 `.GroupByDate` 对后端文章数据进行聚合处理，并由前端动态渲染发布频率柱状图。此功能不仅提供直观的内容概览，还支持图表点击与平滑滚动联动，使用户能够精准定位到特定月份的文章目录。
* **优化分页导航系统:** 结合 CSS `scroll-margin-top` 与锚点定位 (Anchor Fragment) 技术，确保用户在翻页时，页面视图精准地停留在文章目录上方，有效避免了固定导航栏遮挡标题的问题，从而保障了流畅且无干扰的阅读心流。
* **自定义 Markdown 扩展:** 封装了 `<details>` 折叠框 Shortcode，专为优雅展示解谜游戏的提示与答案而设计。此定制化组件有效解决了原生 Markdown 解析器在嵌套 HTML 时可能出现的缩进失效问题，增强了内容展示的灵活性与专业性。

## 🛠 技术栈

* **静态网站生成器:** [Hugo](https://gohugo.io/)
* **主题框架:** [PaperMod](https://github.com/adityatelange/hugo-PaperMod) (深度定制版)
* **前端:** Vanilla JavaScript, HTML5, SCSS (兼容 Dark Mode)
* **数据可视化:** Chart.js
* **部署:** GitHub Pages & GitHub Actions (自动化 CI/CD)
* **统计分析:** Busuanzi (不蒜子极简统计)

## 🚀 本地开发环境搭建

要启动本地开发服务器并预览项目，请遵循以下步骤：

1.  **克隆仓库及子模块:**

    ```bash
    git clone --recurse-submodules https://github.com/Flare-Sky/personal-website.git
    cd personal-website
    ```

2.  **启动 Hugo 本地服务器:**

    ```bash
    hugo server -D
    ```

3.  **访问预览:**

    在浏览器中打开 `http://localhost:1313/` 以查看项目。

## 🤝 贡献与支持

欢迎对本项目提出改进建议或贡献代码。如果您有任何问题或合作意向，请通过以下方式联系我：

* GitHub: [@Flare-Sky](https://github.com/Flare-Sky)
* 个人网址: <https://flaresky.me>

## 📜 许可协议

本项目代码基于 MIT 协议开源。博客文章与个人图片等内容版权归作者所有。

© 2026 Flare-Sky.