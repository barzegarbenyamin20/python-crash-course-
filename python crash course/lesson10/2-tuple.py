numbers = (100, 77)
for i in numbers:
    print("original numbers")
    print("\t",i)

numbers = (233, 7887)
for i in numbers:
    print("modified numbers")
    for i in numbers:
        print("\t", i)