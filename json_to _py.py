import json

x = '{"name": "Thanos", "age": "567", "PH": 8236478648746, "height": 8.5}'
y = json.loads(x)

assert "Thanddds" in json.dumps(y)