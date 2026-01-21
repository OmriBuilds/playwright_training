import email
from Lib.python_training.sting_examples import index

students = ["Efrat", "Vered", "Moka", "Maxim", "Omri"]
grade = [78, 76, 56, 89, 95]

for name in students:
    print(f"The length of {name} is {len(name)} letters.")

####################################
#average calculater

sum = 0
count = 0
for i in range(1,11):
    sum += i
    count += 1

avg = sum/count
print(f"The sum is {sum} average number is {avg}")

####################################
#average calculater

#emails = ["aaa@aaa.com", "asdasd", "asd@.dfsdf.cd"]

#for mail in emails:
#    index = email.index("@")
#    if index in email:
#        print(f"{email} is a legit email address.")

################################################

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = 0
odds = 0

for number in numbers:
    if number % 2 == 0:
        evens += number
        print(f"{number} is even.")
    elif number % 2 != 0:
        odds += number
        print(f"{number} is odd.")
print(f"The sum of the even numbers is {evens}")
print(f"The sum of the odd numbers is {odds}")

#########################
name = "news"
name2 = "new_york"
if name in name2:
    print(f"The name '{name2}' contains '{name}'.")
if name not in name2:
    print(f"The name '{name2}' does not contain '{name}'.")

#########################

for number in range(10, 100):
    if (number % 7 == 0):
        print(f"{number} is divisible by 7.")
    if ("7" in str(number)):
        print(f"{number} contains '7'.")