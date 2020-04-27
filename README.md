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
class GModel:
    sss = None


class ZModel:
    aaa = None


class People:
    name = None
    age = None
    girlFriends = None
    zzz = None
    testList = None

    # 这里指定属性类型
    __doc__ = {
        "girlFriends": GModel,
        "zzz": ZModel
    }


# 引用
import jsonModel

data = '[{"testList":[1, 2, 3],"name":"jack","age":13,"girlFriends":[{"sss":"111"},{"sss":"222"}],"zzz":{"aaa":"aaa"}},{"testList":[1, 2, 3],"name":"jone","age":21,"girlFriends":[{"sss":"111"},{"sss":"222"}],"zzz":{"aaa":"aaa"}}]'

# json 转 实体类
res = jsonModel.loads(data, People)

# 实体类 转 json
jsonStr = jsonModel.dumps(res)
```



