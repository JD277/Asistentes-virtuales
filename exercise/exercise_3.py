age = float(input("Enter your age"))
if age < 0:
    raise("Invalid age")
if age <= 2:
    dog_age = age*10.5
else :
    dog_age = (2* 10.5) + (age-2)*4 
print(f"{dog_age} years")