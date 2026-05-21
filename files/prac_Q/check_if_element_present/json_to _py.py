import json

x = '{"name": "Thanos", "age": "567", "PH": 8236478648746, "height": 8.5}'
y = json.loads(x)

try:
    assert "age" in json.dumps(y)
    print("found")

except:
    print("not found")