import sys
import json
import requests
if len(sys.argv)!=2:
    sys.exit()
response=requests.get("https://www.google."+sys.argv[1])
print(json.dumps(response.json(),indent=2))