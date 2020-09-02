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

:::warning 注意
interer_bits 参数优先级最高

当interer_bits不为空时，max_value 和 min_value 参数失效！

:::

:::danger 注意
interer_bits 初始默认值: None

当参数 max_value 和 min_value 均为空值时，interer_bits自动配置为 32

:::

### 2. max_value

参数描述: <b class="grey-bg"> 整数范围最大值 </b>

参数类型: <b class="pink-color grey-bg"> int </b>

参数默认值: <b class="grey-bg"> None </b>

:::danger 注意
max_value 初始默认值: None

当参数 interer_bits 为空， 且 min_value 不为空值时，

max_value 自动配置为 min_value值(绝对值)最近的最大范围值，

具体来说:

* 0 - (2 ^ 16 - 1) :  2 ^ 16
* (2 ^ 16) - (2 ^ 32 - 1) :  2 ^ 32
* (2 ^ 32) - (2 ^ 64 - 1) :  2 ^ 64

:::

### 3. min_value

参数描述: <b class="grey-bg"> 整数范围最小值 </b>

参数类型: <b class="pink-color grey-bg"> int </b>

参数默认值: <b class="grey-bg"> None </b>

:::danger 注意
min_value 初始默认值: None

当参数 interer_bits 为空， 且 max_value 不为空值时，

min_value 自动配置为 max_value值(绝对值)最近的最小范围值，

具体来说:

* 1 - (2 ^ 16) :  0
* (2 ^ 16 + 1) - (2 ^ 32) :  2 ^ 16
* (2 ^ 32 + 1) - (2 ^ 64) :  2 ^ 32

:::

### 4. exclude

参数描述: <b class="grey-bg"> 排除选项 </b>

参数类型: <b class="pink-color grey-bg"> int / list / string </b>

参数默认值: <b class="grey-bg"> [] </b>

exclude用于从生成的结果中排除某些不想要的数据
