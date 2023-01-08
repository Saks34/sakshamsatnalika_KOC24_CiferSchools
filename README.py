a= input("Enter your email address:")
for i in range (0,len(a)):
    if a[i]=="@":
        b = a[:i]
        print(b)
        c = a[i+1:len(a)]
        print(c.upper())
