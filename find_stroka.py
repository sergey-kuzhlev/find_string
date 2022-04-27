def find_stroka(a, b):

    if b == "":
        return True

    for i in range(len(a) - len(b) + 1):
        for j in range(len(b)):
            if b[j] != a[i + j]:
                break
            if j == (len(b) - 1):
            	return True           
    return False
        
a = input("a = ")
b = input("b = ")
print(find_stroka(a,b))
