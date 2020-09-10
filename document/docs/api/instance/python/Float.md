---
title: Float 浮点数数据类型
lang: zh-CN
publish: true
author: 半片叶
time: 2020-08-23
backToTop: true
article: false
timeline: false
next: /api/instance/python/Bool.md
prev: /api/instance/python/Int.md
---

# Float 浮点数类型

## 1. interer_bits

参数描述: <b class="grey-bg"> 整数位数 </b>

参数类型: <b class="pink-color grey-bg"> int </b>

参数默认值: <b class="grey-bg"> None </b>

interer_bits 参数优先级最高

当interer_bits不为空时，max_value 和 min_value 参数失效！

interer_bits 初始默认值: None

当参数 max_value 和 min_value 均为空值时，interer_bits自动配置为 <b class="blue-color grey-bg"> 3 </b>

## 2. decimal_bits

参数描述: <b class="grey-bg"> 小数位部分位数 </b>

参数类型: <b class="pink-color grey-bg"> int </b>

参数默认值: <b class="grey-bg"> 3 </b>

## 3. max_value

参数描述: <b class="grey-bg"> 最大范围值 </b>

参数类型: <b class="pink-color grey-bg"> int </b>

参数默认值: <b class="grey-bg"> None </b>

## 4. min_value

参数描述: <b class="grey-bg"> 最小范围值 </b>

参数类型: <b class="pink-color grey-bg"> int </b>

参数默认值: <b class="grey-bg"> None </b>

## 5. is_support_negative

参数描述: <b class="grey-bg"> 是否支持负数 </b>

参数类型: <b class="pink-color grey-bg"> bool </b>

参数默认值: <b class="grey-bg"> False </b>

