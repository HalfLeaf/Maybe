---
title: Int整数数据类型
lang: zh-CN
publish: true
author: 半片叶
date: 2020-08-23
---

# Int 整数类型

## 1. interer_bits

参数描述: <b class="grey-bg"> 整数位数 </b>

参数类型: <b class="pink-color grey-bg"> int/string </b>

可支持配置:
* <b class="vue-color grey-bg"> 8   /  byte    </b>
* <b class="vue-color grey-bg"> 16  /  short  </b>
* <b class="vue-color grey-bg"> 32  /  int    </b>
* <b class="vue-color grey-bg"> 64  /  long   </b>

参数默认值: <b class="grey-bg"> None </b>

interer_bits 参数优先级最高

当interer_bits不为空时，max_value 和 min_value 参数失效！

interer_bits 初始默认值: None

当参数 max_value 和 min_value 均为空值时，interer_bits自动配置为 32


## 2. max_value

参数描述: <b class="grey-bg"> 整数范围最大值 </b>

参数类型: <b class="pink-color grey-bg"> int </b>

参数默认值: <b class="grey-bg"> None </b>

max_value 初始默认值: None

当参数 interer_bits 为空， 且 min_value 不为空值时，

max_value 自动配置为 min_value值(绝对值)最近的最大范围值，

具体来说:

```python
* 0 - (2 ** 16 - 1) :  2 ** 16
* (2 ** 16) - (2 ** 32 - 1) :  2 ** 32
* (2 ** 32) - (2 ** 64 - 1) :  2 ** 64
```

## 3. min_value

参数描述: <b class="grey-bg"> 整数范围最小值 </b>

参数类型: <b class="pink-color grey-bg"> int </b>

参数默认值: <b class="grey-bg"> None </b>

min_value 初始默认值: None

当参数 interer_bits 为空， 且 max_value 不为空值时，

min_value 自动配置为 max_value值(绝对值)最近的最小范围值，

具体来说:
```python
* 1 - (2 ** 16) :  0
* (2 ** 16 + 1) - (2 ** 32) :  2 ** 16
* (2 ** 32 + 1) - (2 ** 64) :  2 ** 32
```

## 4. is_support_negative

参数描述: <b class="grey-bg"> 是否支持负数 </b>

参数类型: <b class="pink-color grey-bg"> bool </b>

参数默认值: <b class="grey-bg"> False </b>

该参数会影响 <b class="vue-color grey-bg">interer_bits / is_add_boundary_field </b> 最终生成的结果

由参数 <b class="vue-color grey-bg">max_value / min_value </b> 最终生成的结果不受该参数影响

## 5. exclude

参数描述: <b class="grey-bg"> 排除选项 </b>

参数类型: <b class="pink-color grey-bg"> int / list / string </b>

参数默认值: <b class="grey-bg"> [] </b>

exclude用于从生成的结果中排除某些不需要的数据，支持 int 、list 、string类型

* <b class="grey-bg"> int </b>

排除单一整数值

* <b class="grey-bg"> list </b>

排除多个整数值

* <b class="grey-bg"> string </b>

用于排除指定范围的整数值，用 "-" 分割, 如:

```python
10 - 100
```

:::warning 注意
多个 - 连接符，程序只处理首（第一个）尾（最后一个）

如首尾无法构成有效范围，依次转化为 第一个和倒数第 2,3,4... 个，尝试构成有效范围

如均无法构成有效范围，则将字符串按照 - 分割后转化为 list 排除范围
:::

## 6. is_add_boundary_field

参数描述: <b class="grey-bg"> 是否添加到边界域 </b>

参数类型: <b class="pink-color grey-bg"> bool </b>

参数默认值: <b class="grey-bg"> True </b>

用于设置整数参数是否添加到边界域

当用户设置 <b class="vue-color grey-bg">interer_bits / min_value / max_value / exclude </b> 后，当此参数为
<b class="grey-bg"> True </b>时

* <b class="grey-bg"> interer_bits / min_value / max_value </b>
程序自动将极值加减1

* <b class="grey-bg"> exclude </b>
仅支持<b class="pink-color grey-bg"> int / string </b>类型时，自动将指定值 / 范围值 加减1

