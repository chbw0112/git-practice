import json
data = {"name": "Choi", "lan":"kor", "gen":"m"}
with open("json_practice", "w", encoding="utf - 8") as f:
    json.dump(data, f, indent=2)
with open("json_practice", "r", encoding="utf - 8") as f:
    load = json.load(f)
print(load["lan"])