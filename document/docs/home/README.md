# Maybe

## 项目定位
* API接口测试工具 ( 单元测试 + 功能测试 + 兼容性测试 ... )
* 测试数据集中管理的数据中台
* 测试数据智能推荐平台
* 测试报告智能分析平台

## 测试数据分类
* <span class="vue-color grey-bg">正确域 : </span>  预期符合接口规范的合理参数
* <span class="vue-color grey-bg">边界域 : </span>  接口定义中边界范围的参数
* <span class="vue-color grey-bg">错误域 : </span>  不符合接口定义范围的参数
* <span class="vue-color grey-bg">安全域 : </span>  涉及到安全测试领域的部分请求参数

## 测试数据实例对象
* <span class="vue-color grey-bg">Python基本数据类型 : </span>  python基本的数据类型，包括:
    * <span class="vue-color grey-bg">Int </span>
    * <span class="vue-color grey-bg">Float </span>
    * <span class="vue-color grey-bg">Bool </span>
    * <span class="vue-color grey-bg">List </span>
    * <span class="vue-color grey-bg">Dict </span>
    * <span class="vue-color grey-bg">String </span>
* <span class="vue-color grey-bg"> 常用属性对象: </span>  常用的可用于随机生成的属性对象，包括:
    * <span class="vue-color grey-bg">UserAgent </span>
    * <span class="vue-color grey-bg">Country </span>
    * <span class="vue-color grey-bg">Citys </span>
    * <span class="vue-color grey-bg">Address </span>
    * <span class="vue-color grey-bg">PhoneNumber </span>
    * <span class="vue-color grey-bg">Email </span>
* <span class="vue-color grey-bg">数据库对象 : </span>  用于连接数据库，获取数据库中指定文档数据
* <span class="vue-color grey-bg">用户自定义对象 : </span>  用户编写的python类，经解析后，接入Maybe系统