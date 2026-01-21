class Utils_jb61:

    def age_calculator(self, age, ref_age=18):
        if age>ref_age:
            print(f"age is greater than {ref_age}")
            age_new = age+5
        else:
            print(f"age is less than {ref_age}")
            age_new = age-5

        return age_new


    def email_verification(self, email):
        print("validating email...")
        if "@" and "." in email:
            print("email is valid")
            return True
        else:
            print("email is not valid")
            return False

    def send_mail(self):
        print("sending email...")

    def digit_count(self, num):
        if num in range(100,1000):
            hundreds = num // 100
            tens = (num % 100)//10
            ones = num % 10
            digit_sum = hundreds + tens + ones
            print(digit_sum)
            return digit_sum
        else:
            print("number not valid")
            return "number not valid"


