# to read write file>

# # # with open("txt.txt","r") as file:
# # #     read=file.read()
# # #     print (read)
# # # with open ("txt.txt","w")as file:
# # #     file.write("I am a person.")
# # # with open ("txt.txt","a") as file:
# # #     file.write("I am 19.")

# to read binary code of pictures
# # with open ("download.jpg","rb") as file:
# #     x=file.read()
# #     print (x[:20])
# #     file.close
# # with open ("xyz.jpg","wb") as file:
# #     file.write(x)

# # ###Regex
# # it find all the words numbrs only in text except symbols
# import re
# text ="The quick 444455 brown fox #@#$@# jump 12123551 over 445the lazy dog"
# pattern= r"\b\w+\b"
# matches=re.findall(pattern,text)
# print (matches)

#it find the numbre in 0000-000-0000 pattern
# # import re
# # text="Hello World! call me in 4859-454-4545"
# # pattern=r"\d{4}-\d{3}-\d{4}"
# # matches=re.findall(pattern,text)
# # print (matches)


#it find the nepali phone no:
# import re
# text="hello 9802327510,9702327510,96785678,5678765567"
# pattern=r"\b9\d{9}"
# matches=re.findall(pattern,text)
# print (matches)

# import re
# text="Hey nigger! send me email in this address: abc123.24@gmail.com"
# pattern=r"[a-z0-9.]+@[a-z]+\.[a-z]{2,}"
# matches=re.findall(pattern,text)
# print("email: ",matches)

# import re
# word="python"
# with open  ("txt.txt","r") as file:
#     final=file.read()
# matches=re.findall(rf"\b{word}\b",final,re.IGNORECASE)
# print (f"'{word}' found {len(matches)} times. ")