def print_names(**names):
    for key,value in names.items():
        print("{} is {}".format(key,value))

people={'name':'Sampath','name1':'Santosh'}
print_names(**people)