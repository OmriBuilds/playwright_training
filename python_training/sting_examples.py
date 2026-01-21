full_name = "John Doe"
print(len(full_name))
full_name_new = full_name.replace("John ",  "Johnny ")
print(full_name_new)
index = full_name_new.index(" ")
first_name = full_name_new[0:index]
last_name = full_name_new[index+1:len(full_name_new)]

print(f'My full name is {first_name} {last_name}')


