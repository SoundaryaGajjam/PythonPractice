ages = {
    'Mary' : 34,
    'John' : 20,
    'Dick' : 55
}
'''
if 'Dick' in ages:
    age = ages['Dick']
else:
    age = 'Unknown'
'''
# using dictionary get()
age = ages.get('Dick',"Unknown")
print('Dick is %s years old' %age)