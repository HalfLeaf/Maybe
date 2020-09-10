---
title: String字符串数据类型
lang: zh-CN
publish: true
author: 半片叶
time: 2020-08-23
backToTop: true
article: false
timeline: false
next: /api/instance/python/List.md
prev: /api/instance/python/String.md
---

# String 字符串数据类型

## 1. length

参数描述: <b class="grey-bg"> 字符串长度 </b>

参数类型: <b class="pink-color grey-bg"> int </b>

参数默认值: <b class="grey-bg"> 8 </b>

## 2. max_length

参数描述: <b class="grey-bg"> 最大字符串长度 </b>

参数类型: <b class="pink-color grey-bg"> int </b>

参数默认值: <b class="grey-bg"> None </b>

## 3. min_length

参数描述: <b class="grey-bg"> 最小字符串长度 </b>

参数类型: <b class="pink-color grey-bg"> int </b>

参数默认值: <b class="grey-bg"> None </b>

## 4. min_length

参数描述: <b class="grey-bg"> 最小字符串长度 </b>

参数类型: <b class="pink-color grey-bg"> int </b>

参数默认值: <b class="grey-bg"> None </b>

## 5. is_support_capital

参数描述: <b class="grey-bg"> 是否支持大写字母 </b>

参数类型: <b class="pink-color grey-bg"> bool </b>

参数默认值: <b class="grey-bg"> True </b>

## 6. is_support_lower

参数描述: <b class="grey-bg"> 是否支持小写字母 </b>

参数类型: <b class="pink-color grey-bg"> bool </b>

参数默认值: <b class="grey-bg"> True </b>

## 7. is_support_digit

参数描述: <b class="grey-bg"> 是否支持数字 </b>

参数类型: <b class="pink-color grey-bg"> bool </b>

参数默认值: <b class="grey-bg"> True </b>

## 8. is_support_chinese_character

参数描述: <b class="grey-bg"> 是否支持中文字符 </b>

参数类型: <b class="pink-color grey-bg"> bool </b>

参数默认值: <b class="grey-bg"> True </b>

## 9. is_support_english_punctuation

参数描述: <b class="grey-bg"> 是否英文标点等特殊字符 </b>

参数类型: <b class="pink-color grey-bg"> bool </b>

参数默认值: <b class="grey-bg"> True </b>

## 10. code_range

参数描述: <b class="grey-bg"> 指定生成字符串UTF-8编码范围 </b>

参数类型: <b class="pink-color grey-bg"> string / list </b>

参数默认值: <b class="grey-bg"> None </b>

* <b class="vue-color grey-bg"> list </b>
程序默认取列表的第一个值与最后一个值，如列表长度为<b class="blue-color grey-bg"> 1 </b>,
自动配置起始范围为 <b class="blue-color grey-bg"> "0000" </b>

* <b class="vue-color grey-bg"> string </b>
程序自动配置起始值为 <b class="blue-color grey-bg"> "0000" </b>, 用户配置的值最为结束值

## 11. exclude

参数描述: <b class="grey-bg"> 生成源需要排除的数据 </b>

参数类型: <b class="pink-color grey-bg"> list </b>

参数默认值: <b class="grey-bg"> None </b>

数据源在生成字符串时，根据此配置，剔除部分数据，保证最终生成的字符串中符合用户要求

## 12. format

参数描述: <b class="grey-bg"> 指定字符串生成的格式 </b>

参数类型: <b class="pink-color grey-bg"> str </b>

参数默认值: <b class="grey-bg"> "" </b>

如需程序自动生成的数据部分，需用 <b class="blue-color grey-bg"> {} </b>
