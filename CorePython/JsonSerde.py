import json

person='''
    {
    "age":23,
    "name":"Sampath",
    "Location":"Hyderbad",
    "company":"cgi"
}
'''


person_dict = json.loads(person)
print(type(person_dict))
print(person_dict.get("age"))

person_str = json.dumps(person_dict)

print(type(person_str))