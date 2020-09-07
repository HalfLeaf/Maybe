---
title: 数据生成模式
lang: zh-CN
publish: true
author: 半片叶
date: 2020-08-23
---

# 数据生成模式

<b class="grey-bg"> pattern </b>  指定数据生成模式，支持如下参数:

* <b class="vue-color grey-bg"> Default </b>   默认值模式
* <b class="vue-color grey-bg"> Fix </b>   固定值模式
* <b class="vue-color grey-bg"> Circle </b>   轮询模式
* <b class="vue-color grey-bg"> Choice </b>   挑选模式
* <b class="vue-color grey-bg"> Random </b>   随机模式
* <b class="vue-color grey-bg"> Previous </b>   恢复前次模式
* <b class="vue-color grey-bg"> Auto </b>   智能选值模式

## Default

<b class="grey-bg"> Default </b>   默认值模式

所有实例对象，都设置有默认值，默认值保存在Maybe数据库的 ins_default_value 集合中，已知的有:

* <b class="vue-color grey-bg"> Int </b>   1
* <b class="vue-color grey-bg"> Folat </b>   1.0
* <b class="vue-color grey-bg"> Bool </b>   True
* <b class="vue-color grey-bg"> String </b>   ""
* <b class="vue-color grey-bg"> List </b>   []
* <b class="vue-color grey-bg"> Dict </b>   {}
* <b class="vue-color grey-bg"> UserAgent </b>
```python
  Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36
```

## Fix
<b class="grey-bg"> Fix </b>   固定值模式

由用户配置的单一固定对象，该对象作为一个整体，每次生成的结果都是该对象

## Circle
<b class="grey-bg"> Circle </b>   轮询模式

由用户指定一组数据，该数据可以是列表或者字典类型，暂不支持其他类型

每次生成的结果按照用户指定的数据顺序，依次生成

当遍历到数据结尾时，将重新从下标索引为0的地方重新开始，直至达到用户设定的用例执行数为止

:::warning 特别注意
字典类型的数据，每次生成的结果是字典的KEY值
:::

## Choice
<b class="grey-bg"> Choice </b>   挑选模式

挑选模式将会从用户指定的一组数据中随机生成一条结果

用户指定的数据，可以是列表或者字典类型，暂不支持其他类型

该模式下，支持用户对每一个数据中的单元，配置权重，权重默认值为<b class="pink-color grey-bg"> 10 </b>

当用户对其中至少一个单元的数据配置了权重，将会自动对整个数据组进行归一化处理

:::warning 特别注意
字典类型的数据，每次生成的结果是字典的KEY值
:::

## Random
<b class="grey-bg"> Random </b>   随机模式

随机模式将会从实例对象的随机库，或者第三方库，构造测试数据

各实例调用的第三方库如下:
* <b class="vue-color grey-bg"> Int </b>   <b class="pink-color grey-bg"> dataFaker </b>
* <b class="vue-color grey-bg"> Folat </b>   <b class="pink-color grey-bg"> dataFaker </b>
* <b class="vue-color grey-bg"> Bool </b>   <b class="pink-color grey-bg"> dataFaker </b>
* <b class="vue-color grey-bg"> String </b>   <b class="pink-color grey-bg"> dataFaker </b>
* <b class="vue-color grey-bg"> List </b>   <b class="pink-color grey-bg"> dataFaker </b>
* <b class="vue-color grey-bg"> Dict </b>   <b class="pink-color grey-bg"> dataFaker </b>
* <b class="vue-color grey-bg"> UserAgent </b>  <b class="pink-color grey-bg"> fake_useragent </b>

## Previous
<b class="grey-bg"> Previous </b>   恢复前次模式

恢复上次模式，可以恢复用户上次执行的现场，用于定位问题使用

当用户选择此模式，将会从数据库中找到上次的执行记录，抽取出执行数据，依次恢复

## Auto
<b class="grey-bg"> Auto </b>   智能选值模式

智能选值模式，将通过智能算法学习用户行为，通过分析用户行为，筛选出用户可能数据集