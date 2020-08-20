
module.exports = {
  "lintOnSave": false,
  "transpileDependencies": [
    
  ],
  publicPath:"./",
  runtimeCompiler:true,
  pages: {
    index: {
      // 入口文件
      entry: 'src/main.js',
      // 模板文件
      template: 'public/index.html',
      // 输出文件
      filename: 'index.html',
      // 页面title
      title: 'Maybe'
    },
    // 简写格式
    // 模板文件默认是 `public/subpage.html`
    // 如果不存在，就是 `public/index.html`.
    // 输出文件默认是 `subpage.html`.
    subpage: 'src/main.js'
  },
  devServer: {
    port: 8686, // 端口号
  },
}