try:
    no=int(input("Enter a even no : "))
    assert  no%2==0,"odd no"
except AssertionError as e:
    print(e)
print("after assertion")