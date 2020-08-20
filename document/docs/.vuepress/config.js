module.exports = {
  lange: 'zh-CN',
  title: 'Maybe',
  description: 'API接口探索性测试平台',
  author: '半片叶',
  port:8686,
  head: [
    ['link', { rel: 'icon', href: '/maybe.png' }],
    ['link', { rel: 'stylesheet', href: 'https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.7.1/katex.min.css' }],
    ['link', { rel: "stylesheet", href: "https://cdnjs.cloudflare.com/ajax/libs/github-markdown-css/2.10.0/github-markdown.min.css" }]
  ],
  base: '/', // 这是部署到github相关的配置
  markdown: {
    lineNumbers: false, // 代码块显示行号
    config: md => {
      md.set({html: true})
      md.use(require("markdown-it-katex"))
    }
  },
  themeConfig: {
    nav:[ // 导航栏配置
      {text: '快速入门', link: '/quickly/' },
      {text: '指南', link: '/guide/'},
      {text: 'API文档', link: '/api/'},
      {text: '更新记录', link: '/updater/'}, 
    ],
    sidebar: 'auto', 
    sidebarDepth: 4, 
  },
  sidebar:[
    ['/', '首页'],
  ],
  evergreen: true,
  activeHeaderLinks: true,
  plugins: [
    ['@vuepress/plugin-back-to-top', true],
  ],
};