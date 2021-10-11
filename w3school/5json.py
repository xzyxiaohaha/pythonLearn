# -*- codeing = utf-8 -*-
# @Time : 2021/10/11 13:14
# @Author : zyxiao
# @File : 5json.py
# @Software : {PyCharm}
import json
x = '{"name":"xiaohaha", "age":22, "city":"haikou"}'
# x =  '{ "name":"Bill", "age":63, "city":"Seatle"}'
y=json.loads(x)
print(y)
print(y["age"])
x = {
    "name": "哈哈",
    "age": 20,
    "city": "北京"
}
y=json.dumps(x)
print(y)

import json

print(json.dumps({"name": "Bill", "age": 63}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

import json

x = {
  "name": "Bill",
  "age": 63,
  "married": True,
  "divorced": False,
  "children": ("Jennifer","Rory","Phoebe"),
  "pets": None,
  "cars": [
    {"model": "Porsche", "mpg": 38.2},
    {"model": "BMW M5", "mpg": 26.9}
  ]
}

print(json.dumps(x))
print(json.dumps(x, indent=4, separators=(". ", " = ")))
print(json.dumps(x, indent=4, sort_keys=True))