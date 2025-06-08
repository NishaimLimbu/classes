sentence = input("enter a sentence")
x= sentence.lower().split("!")
print (x)
x_c={}
for z in x :
    if z in x_c:
        x_c[z]= x_c[z]+1
    else :
        x_c[x]=1
print ("word repetation")
for z,