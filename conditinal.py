age=int (input ("Enter age of person:"))
Smoke=(input ("Enter Yes if he/she smokes else No:"))
Exercie=(input ("Enter Yes if he/she do exercise else No:"))
if age>50 and Smoke=="yes" and Exercie=="no":
    print("High Risk of Heart Disease")
elif age>50 or Smoke=="yes" and Exercise=="no":
    print("Midium Risk of Heart Disease")
else:
    print("Low Risk of Heart Disease") 