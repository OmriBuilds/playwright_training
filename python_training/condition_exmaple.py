num_1 = 10
num_2 = 20
##

if num_1 > num_2:
    print(f'{num_2} + 100 = {num_2+100}')
else:
    print(f'{num_1} + 100 = {num_1+100}')

print("#################################")

for i in range (1,10):
    if i * i > 20:
        print(f"{i} * {i} is higher than 20")

print("#################################")

for i in range(1,10):
    if i * i == i * 4:
        print(f"{i} is the magic number")
        break

print("#################################")

sentence = "Hi, my name is Leo Messi"
index = sentence.index("s")
for i in range(index+2):
    print(sentence[0:i])

print("#################################")
##################################################

full_name = "Omri_Arbiv"
index = full_name.index("_")
first_name = full_name[0:index]
last_name = full_name[index+1:]
if len(first_name) > len(last_name):
    print(f"In the name {first_name} {last_name}, the first name is a longer string than the last name.")
elif len(first_name) == len(last_name):
    print(f"In the name {first_name} {last_name}, the first name and the last name are equal length.")
else:
    print(f"In the name '{first_name} {last_name}', the last name is a longer string than the first name.")

print("#################################")
#################################################

grade = int(input("What is your grade? "))

if grade >= 0 and grade < 50:
    grade = grade + 10
    print(f"Your grade is {grade} after recieving 10 points bonus for scoring lower than 50.")
elif grade >= 50 and grade < 80:
    print(f"You scored {grade}. No bonus points recieved.")
elif grade >= 80 and grade <= 100:
    grade = grade + 20
    if grade > 100:
        grade = 100
    print(f"You scored {grade} after recieving 20 points bonus for scoring higher than 80.")
else:
    print("Grade must be between 0 - 100.")
