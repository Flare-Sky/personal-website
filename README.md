<div align="right">
  <strong>English</strong> | <a href="./README_zh.md">中文</a>
</div>

# Journal of a Sojourner

> *Dear friends, I urge you, as foreigners and exiles... (1 Peter 2:11a)*

This is a personal static blog built with Hugo, designed to be a digital garden that integrates life documentation, technical sharing, and front-end engineering practice. The core objective of this project is to showcase best practices in modern front-end development and to enhance user experience and technical depth through continuous iteration.

## 💡 Project Highlights

This project features deep customization and functional extensions based on the [PaperMod](https://github.com/adityatelange/hugo-PaperMod) theme, introducing several innovative features:

* **Immersive Parallax Home Page:** Utilizes a unique "Fixed Background Layer + Floating Solid Card Layer" sandwich architecture, achieving perfect cross-device compatibility and a smooth, physics-based sliding damping effect. Through carefully tuned vanilla JavaScript, it implements a smart scroll fade-out effect for the background text, greatly enhancing visual immersion and the interactive experience.
* **Data-Driven Dynamic Archives:** Integrates Chart.js on the archive page (`/archives`). During the Hugo build phase, it utilizes `.GroupByDate` to aggregate backend post data and dynamically renders a publication frequency bar chart on the front end. This feature not only provides an intuitive content overview but also supports click events on the chart linked with smooth scrolling, allowing users to precisely navigate to specific monthly post directories.
* **Refined Pagination Navigation:** Combines CSS `scroll-margin-top` with Anchor Fragment positioning to ensure that upon pagination, the viewport accurately snaps above the post directory. This effectively prevents the sticky navigation bar from obscuring titles, ensuring a seamless and uninterrupted reading flow.
* **Custom Markdown Extensions:** Encapsulates a `<details>` collapsible Shortcode tailored for elegantly displaying hints and solutions for puzzle games. This custom component effectively resolves the indentation failure issues that can occur with native Markdown parsers when nesting HTML, enhancing the flexibility and professionalism of content presentation.

## 🛠 Tech Stack

* **Static Site Generator:** [Hugo](https://gohugo.io/)
* **Theme Framework:** [PaperMod](https://github.com/adityatelange/hugo-PaperMod) (Deeply customized)
* **Front-end:** Vanilla JavaScript, HTML5, SCSS (Dark Mode compatible)
* **Data Visualization:** Chart.js
* **Deployment:** GitHub Pages & GitHub Actions (Automated CI/CD)
* **Analytics:** Busuanzi (Minimalist site analytics)

## 🚀 Local Development Setup

To start the local development server and preview the project, follow these steps:

1.  **Clone the repository and submodules:**

    ```bash
    git clone --recurse-submodules [https://github.com/Flare-Sky/Flare-Sky.github.io](https://github.com/Flare-Sky/Flare-Sky.github.io)
    cd Flare-Sky.github.io
    ```

2.  **Start the Hugo local server:**

    ```bash
    hugo server -D
    ```

3.  **Access the preview:**

    Open `http://localhost:1313/` in your browser to view the project.

## 🤝 Contribution & Support

Suggestions for improvement and code contributions are welcome. If you have any questions or collaboration inquiries, please contact me via:

* GitHub: [@Flare-Sky](https://github.com/Flare-Sky)
* Personal Website: <https://flaresky.me>

## 📜 License

The code of this project is open-sourced under the MIT License. All rights reserved for blog articles, original text content, and personal images.

© 2026 Flare-Sky.