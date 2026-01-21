from Lib.python_training.utils_jb61 import Utils_jb61

# staring the code

user_1 = {
    "first_name": "John",
    "last_name": "Doe",
    "email": "abc@abc.com",
    "age": 42


}

user_2 = {
    "first_name": "John",
    "last_name": "Wick",
    "email": "john@abccom",
    "age": 16

}
utils = Utils_jb61()
age_1 = utils.age_calculator(user_1["age"])
age_2 = utils.age_calculator(user_2["age"], ref_age=20)
print(f"{age_1} and {age_2}")
utils.email_verification(user_1["email"])
utils.email_verification(user_2["email"])

print("test end")
