a,b=0,1

print ("first 10 fibonacci numbers\n")
for _ in range (20): #run up to 20 different numbers
    print (a)
    a,b = b,a+b #in this line the = sign divide eqn into LHS and RHS. This eqn solve from right to left
    #exicute like b=1, a+b=0+1=1 and assign new value to a and b variable