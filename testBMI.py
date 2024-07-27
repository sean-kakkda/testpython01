kg = float(input("can you input KG :\n"))
Height = float(input("can you input height in meters\n"))
H=Height**2
BMI = kg//H
#print(" your BMI =" +str(int(BMI)))
#print("Your BMI = ",int(BMI))
#print(f'For Weight = {kg} and Height = {Height} so your BMI = {BMI}')
print("For Weight ={} and Height={} so your BMI={}".format(kg,Height,BMI))