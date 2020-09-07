---
title: Maybe整体说明
lang: zh-CN
publish: true
author: 半片叶
time: 2020-08-23
backToTop: true
article: false
timeline: false
---

# Maybe

大数据时代，什么最重要？

数据当仁不让的排在所有答案的前列

API层的测试，占据测试工作的三分天下，API接口的数据是否能够管理起来呢？
让数据为我们所用，更便捷的参与到我们测试工作中！

我觉得是可以的，这也是我们进行API接口层面的探索性测试的初衷所在！

<span class="grey-bg">可以想象一下:</span>

当你打开Maybe项目进行测试，刚输入好要测试的URL，Maybe已经从数据库中获取到该URL的历史测试数据（可能是项目组其他成员）

并且，自动帮你预填入到界面中，而你只需要动手修改一些请求的参数或者响应的断言

同时，Maybe还会智能分析该接口所有历史数据，从中找出高频错误数据，边界范围值，为用户提供推荐。

经过，我们初步调查发现，大部分的API接口测试可能出现问题的地方，多数发现在<span class="vue-color grey-bg">边界值 </span>或者<span class="vue-color grey-bg">用户经验值 </span>

所以Maybe要做的是: <span class="vue-color grey-bg">智能分析边界值，集中管理用户经验值 </span>

<span class="pink-color grey-bg">集千万用户经验，我也能满级刷BOSS！ </span>


## 项目定位
* API接口测试工具 ( 单元测试 + 功能测试 + 兼容性测试 ... )
* 测试数据集中管理的数据中台
* 测试数据智能推荐平台
* 测试报告智能分析平台

## 测试数据分类
* <span class="vue-color grey-bg">有效域 : </span>  预期符合接口规范的合理参数
* <span class="vue-color grey-bg">无效域 : </span>  符合接口规范类型的不合理参数
* <span class="vue-color grey-bg">边界域 : </span>  接口规范定义中边界范围的参数
* <span class="vue-color grey-bg">经验域 : </span>  按照用户过往经验推测可能会出现问题的参数
* <span class="grey-bg">安全域 : </span>  涉及到安全测试领域的部分请求参数（待开放）

## 测试数据实例对象
* <span class="vue-color grey-bg">Python基本数据类型 : </span>  python基本的数据类型，包括:
    * <span class="pink-color grey-bg">Int </span>  整数类型
    * <span class="pink-color grey-bg">Float </span>  浮点数类型
    * <span class="pink-color grey-bg">Bool </span>  布尔类型
    * <span class="pink-color grey-bg">String </span>  字符串类型
    * <span class="pink-color grey-bg">List </span>  列表类型
    * <span class="pink-color grey-bg">Dict </span>  字典类型
* <span class="vue-color grey-bg"> 常用属性对象: </span>  常用的可用于随机生成的属性对象，包括:
    * <span class="pink-color grey-bg">UserAgent </span>   用户代理信息
    * <span class="pink-color grey-bg">Citys </span>  城市名
    * <span class="pink-color grey-bg">Country </span>  国家名
    * <span class="pink-color grey-bg">Address </span>  地址信息
    * <span class="pink-color grey-bg">Email </span>  邮件地址信息
    * <span class="pink-color grey-bg">PhoneNumber </span>  手机号码信息
    * <span class="pink-color grey-bg">PlateNumber </span>  车牌号信息
* <span class="vue-color grey-bg">数据库对象 : </span>  用于连接数据库，获取数据库中指定文档数据
* <span class="vue-color grey-bg">用户自定义对象 : </span>  用户编写的python类，经解析后，接入Maybe系统