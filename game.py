print ("****Welcome****")
a=0
n=3
print ("Can you Guess the number in 3 ties?\nIf yes then try by entering number between 0-10:")
while a<n:
    x=int (input ())
    if x==7:
        print("You got the correct number\n")
        break
    else:
        print ("tyr again\n")
        a=a+1
if a==n and !=7:
    print ("The correct no was 7")
