# Maybe

![Maybe](/document/public/logo.png)

## 介绍
API接口探索性自动化测试平台

## 项目背景

在测试他人或者自己开发的API接口时，是否遇到这样的困境：
* 需要编写多条用例，涵盖各个阈值，边界值
* 接口管理缺乏纵向管理，内容更新，其他人员却一无所知

本项目正式基于此困境，试图用来专业解决API接口测试的难题

## 软件架构

后台采用 Python fastapi框架搭建，数据库MongoDB，前端界面采用Vue语言实现

## 项目目录层级

* backend: 主要存放后台处理代码
    * 采用 Python fastapi框架搭建
    * 整个框架核心，单独存放在maybe目录下
    * 默认地址: http://localhost:8866/
* frontend: 主要存放后台处理代码
    * 采用Vue框架渲染界面
    * 使用vuetify组件库搭建组件
    * 默认地址: http://localhost:8686/
* document: 主要存放markdown文档，包括使用手册，API接口说明等
    * 采用Vuepress框架渲染界面
    * 默认地址: http://localhost:8668/
* docs: 主要存放一些设计方案，设计思路等office文档

项目目前正在孕育孵化中...
