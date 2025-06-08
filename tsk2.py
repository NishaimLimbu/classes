list1 =[]
print (list1)
while True:
    x=int(input("enter '1' to add your shopping item and enter '2' to remove the item: "))
    if x==1:
            list1.append(input("add item: "))
            print(list1)
            z=int(input("enter '1' to add your shopping item and enter '2' to remove the item: "))
            if z==1:
                   list1.append(input ("add more: "))
                   print (list1)
                   continue
            elif z==2 :
                    list1.remove(input("remove item: "))
                    print (list1)
            else:
                   break
                   
    elif x==2:
            list1.remove(input("remove item: "))
            print (list1)
            z=int (input ("enter '1' to add your shopping item and enter '2' to remove the item: "))
            if z==2:
                   list1.remove(input ("remove more: "))
                   print (list1)
            elif z==1:
                   list1.append(input ("add more: "))
                   print (list1)
            else :
                   break
    else :
           break
print ("This is you list",list1)