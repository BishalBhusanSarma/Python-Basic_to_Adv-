import json
x = {"name": "Thanos", "spouse":"black widow", "age": 567}

y = json.dumps(x)

z = "name"
if z in y:
    print("found:",z)
else:
    print("not found")


print(json.dumps({"name": "hello", "age": 54}))