import json
data = {"animal":"tiger", "gender":"female", "height": 5.2 }
json_str = json.dumps(data, indent=2, ensure_ascii=False)
print(json_str)
j = json.loads(json_str)
print(j)