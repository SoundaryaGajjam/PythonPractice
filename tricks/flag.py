needle = 'd1'
haystack = ['a','b','c','d']

#bad way
found = False
for letter in haystack:
    if needle == letter:
        print("found")
        found = True
        break
if not found:
    print("not found")

#good way---without using flag var
for letter in haystack:
    if needle == letter:
        print("found")
        break
else:
    print("not found")