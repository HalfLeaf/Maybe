---
title: UserAgent 基础知识
lang: zh-CN
publish: true
author: 半片叶
date: 2020-08-23
---

# UserAgent 用户代理

User Agent中文名为用户代理，简称 UA，它是一个特殊字符串头

<span class="vue-color">使得服务器能够识别客户使用的操作系统及版本、CPU 类型、浏览器及版本、浏览器渲染引擎、浏览器语言、浏览器插件等</span>


::: tip 标准格式
浏览器标识 (操作系统标识; 加密等级标识; 浏览器语言)&emsp;&emsp;   渲染引擎标识 &emsp;&emsp;      版本信息
:::

## 浏览器标识
自浏览器 10 之后的版本中浏览器标识项固定为浏览器，在 UA 字串尾部添加真实版本信息。

## 操作系统标识
* FreeBSD
  * X11; FreeBSD (version no.) i386
  * X11; FreeBSD (version no.) AMD64
  
* Linux
  * X11; Linux ppc
  * X11; Linux ppc64
  * X11; Linux i686
  * X11; Linux x86_64
  
* Mac
  * Macintosh; PPC Mac OS X
  * Macintosh; Intel Mac OS X
  * Solaris
  
* Windows:
  * Windows NT 10.0 对应操作系统windows 10
  * windows NT 6.2 对应操作系统 windows 8
  * Windows NT 6.1 对应操作系统 windows 7

## 加密等级标识

* N:&emsp;表示无安全加密
* I:&emsp;表示弱安全加密
* U:&emsp;表示强安全加密
  
## 浏览器语言

在首选项 > 常规 > 语言中指定的语言

## 渲染引擎

浏览器使用Presto渲染引擎，格式为：<span class="vue-color">Presto/版本号</span>

## 版本信息

显示浏览器真实版本信息，格式为：<span class="vue-color">Version/版本号</span>

::: danger 声明
以上内容摘自: [百度百科 - 用户代理](https://baike.baidu.com/item/%E7%94%A8%E6%88%B7%E4%BB%A3%E7%90%86/1471005?fromtitle=useragent&fromid=5534048&fr=aladdin)
:::

## 示例

UA字符串: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36

可识别到的信息有:

| 浏览器名称 | 浏览器版本 | 系统平台 |
|  ----    | ----  | ----  |
| Chrome | 84.0.4147.105 | Windows7 |
