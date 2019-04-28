# textPer

## 功能
自动生成性能规格和代码

# 使用方法
1. 设置路由，默认是127.0.0.1
2. 网页登陆http://127.0.0.1:8000/index/
3. 填入性能的表名和表ID，这两项要求单选
4. 填入性能名称、对应的性能ID和设备使用的性能ID，性能名称可以填写多个，以常见的分隔符(_/\,.-;:`~|<> )分开，性能ID和设备使用的性能ID如果填入多个，需要与性能名称一一对应，以常见的分隔符分开（_/,.;:`|<> ）,也可以输入范围，如：1-9或者1~9
5. 点击提交
6. 将生成的规格和代码复制到对应的文件中
7. 完善生成的代码中未实现的部分（//TODO:）
