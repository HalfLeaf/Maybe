const resolve = require("vuepress-theme-hope/resolve");
module.exports = resolve({
  lange: 'zh-CN',
  title: 'Maybe',
  description: 'API接口探索性测试平台',
  author: '半片叶',
  port:8668,
  base: '/', // 这是部署到github相关的配置
  headOption: {
    icon: "/maybe.png",
  },
  themeConfig: {
    logo: "/maybe.png",
    author: "半片叶",
    baseLang: 'zh-CN',
    themeColor:false,
    nav:[ // 导航栏配置
      {text: '指南', link: '/guide/', icon: 'configuration'},
      {text: 'API文档', link: '/api/', icon: 'vue'},
      {text: '设计理念', link: '/home/', icon: 'infofill' },
      {text: '更新记录', link: '/updater/', icon: 'questionfill'}, 
    ],
    sidebar: 'auto', 
    sidebarDepth: 5,
    lastUpdated: '上次更新时间',
    markdown: {
      enableAll: true,
    },
    comment: {
      type: "valine",
      appId: "VVjE3KAOY4mRq6SXauTfp0FG-gzGzoHsz",
      appKey: "t7rtj1n7FGvchU6h5wEks9J8",
    }
  },
  sidebar:[
    ['/', '首页'],
  ],
  evergreen: true,
  activeHeaderLinks: true,
});