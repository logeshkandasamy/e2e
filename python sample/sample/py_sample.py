import json
details ={"firstName": "Rack's","lastName": "Jackon","gender": "man","age": 24,"address": {"streetAddress": "126","city": "San Jone","state": "CA","postalCode": "394221"},"phoneNumbers": [{"type": "home","number": "7383627627"}]}
with open("sample.json", "r") as f:
    details = (f.read())
    json.dumps(details)
    print(details)
    
#open('sample-json-file.json', 'r').read()  
