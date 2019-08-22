try:
    print("try")
    try:
        print("inner try")
    except:
        print("inner except")
    finally:
        print("inner finally")
    #print(10/0)
except:
    print("except")
else:
    print("else")

finally:
    print("finally")