---
title: UserAgent 用户代理
lang: zh-CN
publish: true
author: 半片叶
date: 2020-08-23
---

# UserAgent 用户代理

[基础知识](/api/common/UserAgent/BaseInfo.md)

## pattern
<b class="grey-bg"> pattern </b>  指定数据生成方式

* 类型: <b class="grey-bg pink-color"> string </b>
* 默认值: <b class="grey-bg pink-color"> default </b>
* 可选值:
  * <b class="vue-color grey-bg"> Fix </b>
  * <b class="vue-color grey-bg"> Random </b>
  * <b class="vue-color grey-bg"> Circle </b>
  * <b class="vue-color grey-bg"> Choice </b>
  * <b class="vue-color grey-bg"> Popular </b>
  * <b class="vue-color grey-bg"> Default </b>

:::tip 提示
上述参数对英文字母的大小写不敏感！同时支持大写和小写方式
:::

### Fix

<b class="grey-bg">Fix</b>用户指定UserAgent对象

UserAgent对象的具体值在 <b class="grey-bg">dataset</b> 参数中配置，且必须为字符串!

:::warning 警告
pattern指定为Fix时，此时dataset参数为必须参数，否则Fix设置失效！

此时，pattern生成方式转为默认值！
:::

### Random

<b class="grey-bg">Random</b>完全随机生成UserAgent对象

随机范围可在 dataset 参数中配置，可支持如下范围:

* 浏览器类型
  * <b class="vue-color grey-bg"> ie </b>
  * <b class="vue-color grey-bg"> chrome </b>
  * <b class="vue-color grey-bg"> firefox </b>
  * <b class="vue-color grey-bg"> opera </b>
  * <b class="vue-color grey-bg"> safari </b>
* 操作系统类型
  * <b class="vue-color grey-bg"> window </b>
  * <b class="vue-color grey-bg"> liunx </b>
* 完全随机

:::tip 提示
pattern指定为Random时，dataset参数为空，则默认 完全随机方式
:::

### Circle

<b class="grey-bg">Circle</b>轮询遍历方式生成UserAgent对象

此时程序将依次有序的遍历，用户设置的<b class="grey-bg">dataset</b>参数列表，
按照<span class="vue-color">用户配置顺序依次生成</span>UserAgent对象

轮询范围在 <b class="grey-bg">dataset</b> 参数中配置，且必须为列表

:::warning 警告
pattern指定为Circle时，此时dataset参数为必须参数，否则Circle设置失效！
:::

### Choice

<b class="grey-bg">Choice</b>随机选择方式生成UserAgent对象

此时程序将随机选择用户设置的<b class="grey-bg">dataset</b>参数列表，

选择范围在 <b class="grey-bg">dataset</b> 参数中配置，且必须为列表

支持权重配置，默认权重为10！

:::warning 警告
pattern指定为Choice时，此时dataset参数为必须参数，否则Choice设置失效！
:::

### Popular

<b class="grey-bg">Popular</b>根据UserAgent市场占有率随机遍历

根据第三方库: [shadow_useragent](https://github.com/lobstrio/shadow-useragent) 获取当下UserAgent的市场占有情况，

<b class="grey-bg">每周周日</b> 获取数据并更新到 Maybe 数据库

目前数据库中已存有 100 多种UserAgent对象，完全可用于一般测试！

### Default

<b class="grey-bg">Default</b>默认值

```python
Windows10 64位操作系统，Chrome浏览器 版本号:84.0.4147.105
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36
```

## dataset
<b class="grey-bg"> dataset </b>  指定数据集 , 需配合<b class="grey-bg"> pattern </b>参数一起使用！

* 类型: <b class="grey-bg pink-color"> list | string | 不设置 </b>
* 默认值: <b class="grey-bg pink-color"> [] </b>

### dataset 不设置的情况

此时<span class="grey-bg"> pattern </span>支持 <span class="vue-color"> Random/Popular </span> , 不支持<span class="pink-color"> Fix/Circle/Choice/Default </span>
  * <span class="grey-bg"> pattern = "Random" </span>, 程序在整个UserAgent对象库中随机取值
  * <span class="grey-bg"> pattern = "Popular" </span>, 程序在PopularUserAgent对象库中随机取值
  * <span class="grey-bg"> pattern = "Default" </span>, 程序固定返回设置的默认值，不对<span class="grey-bg"> dataset </span>参数取值，校验！
  * <span class="grey-bg"> pattern = "Fix" </span>, pattern设置失效，自动转为  <span class="vue-color">Default</span>
  * <span class="grey-bg"> pattern = "Circle" </span>, pattern设置失效，自动转为  <span class="vue-color">Random</span>
  * <span class="grey-bg"> pattern = "Choice" </span>, pattern设置失效，自动转为  <span class="vue-color">Random</span>

### dataset 字符串类型的情况

此时<span class="grey-bg"> pattern </span>支持 <span class="vue-color"> Fix/Random </span> , 不支持<span class="pink-color"> Circle/Choice/Popular/Default </span>

* <span class="grey-bg"> pattern = "Fix" </span>, <span class="grey-bg"> dataset </span> 必须是合法的User-Agent字符串，程序会进行合法性校验，如检验不通过，则该pattern自动转为<span class="vue-color">  Default</span>！
* <span class="grey-bg"> pattern = "Random" </span>, <span class="grey-bg"> dataset </span> 可支持如下字符串配置:
  * <b class="vue-color grey-bg"> ie </b>
  * <b class="vue-color grey-bg"> chrome </b>
  * <b class="vue-color grey-bg"> firefox </b>
  * <b class="vue-color grey-bg"> opera </b>
  * <b class="vue-color grey-bg"> safari </b>
  * <b class="vue-color grey-bg"> window </b>
  * <b class="vue-color grey-bg"> liunx </b>
  * <b class="vue-color grey-bg"> "" </b>  空字符串，等同于<span class="grey-bg"> dataset </span> 不设置
  * 其他字符串，无效！自动转为 <b class="vue-color grey-bg"> "" </b>
* <span class="grey-bg"> pattern = "Circle" </span>, 参数无效，<span class="grey-bg">pattern</span>自动转为<span class="vue-color">Random</span>
* <span class="grey-bg"> pattern = "Choice" </span>, 参数无效，<span class="grey-bg">pattern</span>自动转为<span class="vue-color">Random</span>
* <span class="grey-bg"> pattern = "Popular" </span>, 参数无效！
* <span class="grey-bg"> pattern = "Default" </span>, 程序固定返回设置的默认值，不对<span class="grey-bg"> dataset </span>参数取值，校验！

### dataset 列表类型的情况

此时<span class="grey-bg"> pattern </span>支持 <span class="vue-color"> Random/Circle/Choice </span> , 不支持<span class="pink-color"> Fix/Popular/Default </span>

* <span class="grey-bg"> pattern = "Random" </span>时, 程序通过随机函数在<span class="grey-bg"> dataset </span>列表中随机取值
  * 列表为空时，在整个UserAgent库中随机
  * 列表值非法时，自动以默认值替换
* <span class="grey-bg"> pattern = "Circle" </span>时, 程序在<span class="grey-bg"> dataset </span>列表中遍历取值
  * 列表为空时，<span class="grey-bg"> pattern </span>设置无效，自动转为<span class="vue-color">Random</span>
  * 列表值非法时，自动以默认值替换
* <span class="grey-bg"> pattern = "Choice" </span>时, 程序通过Choice函数在<span class="grey-bg"> dataset </span>列表中随机取值
  * 列表为空时，<span class="grey-bg"> pattern </span>设置无效，自动转为<span class="vue-color">Random</span>
  * 列表值非法时，自动以默认值替换
* <span class="grey-bg"> pattern = "Fix" </span>时, 参数无效，<span class="grey-bg">pattern</span>自动转为<span class="vue-color">Default</span>
* <span class="grey-bg"> pattern = "Popular" </span>时, 参数无效！
* <span class="grey-bg"> pattern = "Default" </span>时, 程序固定返回设置的默认值，不对<span class="grey-bg"> dataset </span>参数取值，校验！
