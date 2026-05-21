import json
data = {"name":"병우", "grade": "3학년", "전공": "시스템생명공학과"}
json_str = json.dumps(data, ensure_ascii = False, indent=2)
