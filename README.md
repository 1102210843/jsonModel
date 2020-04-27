# jsonModel

json数据转为实体类的工具

# python版本
2.7 ~ 3.8

# 安装
包被上传到[pypi](https://pypi.org/project/pyjsonmodel/)

使用pip安装：
```
$ pip install pyjsonmodel
```
或 更新包
```
$ pip install pyjsonmodel --update
```

# 使用方法

```python
# 模型
class People:
    name = None
    age = None

# 引用
import jsonModel

data = '[{"name":"jack","age":13},{"name":"jone","age":21}]'

# json 转 实体类
res = jsonModel.loads(data, People)

# 实体类 转 json
jsonStr = jsonModel.dumps(res)
```


