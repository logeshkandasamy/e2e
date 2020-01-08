import json

my_details = {
    'name' : 'Uma',
    'age' : '23'
}

with open('personal.json', 'w') as json_file:
    json.dump(my_details,json_file)
    
with open('personal.json', 'r') as json_file1:
    data =  json.load(json_file1)
    print(data)
    
data = {}
data['people'] = []
data['people'].append({
    'name': 'Scott',
    'website': 'stackabuse.com',
    'from': 'Nebraska'
})
data['people'].append({
    'name': 'Larry',
    'website': 'google.com',
    'from': 'Michigan'
})
data['people'].append({
    'name': 'Tim',
    'website': 'apple.com',
    'from': 'Alabama'
})

with open('data.txt', 'w') as outfile:
    json.dump(data,outfile)
    
with open('data.json', 'w') as out_file:
    json.dump(data,out_file)
    
with open('data.json', 'r') as out_file1:
    data = json.load(out_file1)
    print(data)
    
with open('data.json', 'r') as out_file2:
    data = json.load(out_file2)
    for p in data['people']:
        print('Name: ' + p['name'])
        print('Website: ' + p['website'])
        print('From: ' + p['from'])
        print('')
