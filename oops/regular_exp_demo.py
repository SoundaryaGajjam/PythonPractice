import  re
str="Take 1 up 1-2-2019 one 2 idea.one idea 45  at a time.only 12-11-2018"
res=re.search(r'o\w',str)
print(res.group()) #group uses only when res is not none

res=re.findall(r'O\w\w',str)#starting frm begining till end & return all substr which mathces the pattern as a list
print(res)

res=re.match(r'T\w\w',str) #searches only begining of the str
print(res.group())

res=re.split(r'\d+',str)
print(res)

res=re.sub(r'one','two',str)    #replace all
print(res)

#match multiple chars - *,+,?,{},
res=re.findall(r'o\w{1,2}',str)
print(res)

res=re.findall(r'\d{1,2}-\d{1,2}-\d{4}',str)#dinding dates
print(res)

res=re.search(r'^T\w*',str)
print(res.group())





