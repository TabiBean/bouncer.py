# #ask for age
# age = input("How old are you: \n")

# if age:
#     age = int(age)
#     #18-21 wristband
#     if age >= 18 and age < 21:
#         print("You can enter, but need a wristband!")
#     #21+ drink, normal entry
#     elif age >= 21:
#         print("You can enter and drink.")
#     #too young
#     else:
#         print("You can't come in, little one :(")
# else:
#     print("Please enter an age!")

#or

age = input("How old are you: \n")
if age:
    age = int(age)
    if age >= 21:
       print("You can enter and drink.") 
    elif age >= 18:
        print("You can enter, but need a wristband!")
    else:
        print("You can't come in, little one :(")
else:
    print("Please enter an age!")
