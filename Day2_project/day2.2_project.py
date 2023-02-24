#BMI = weight(kg) / height*2(M)
print("Welcome to BMI calculator\n")

#Take the input of weight and height
weight = input("What is your weight in kg: ")
height = input("what is your height in M: ")

#Convert the input given to int and float number
bmi = int(weight) / float(height) ** 2

#Convert the bmi to int to round the total_bmi
total_bmi = int(bmi)

print(total_bmi)
