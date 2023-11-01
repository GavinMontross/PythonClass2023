weight = int(input("How much do you weigh in lbs?: "))
height = int(input("How tall are you in inches?: "))
age = int(input("How old are you?: "))

male = 66 + (6.2 * weight) + (12.7 * height) - (6.76 * age)
female = 655.1 + (4.35 * weight) + (4.7 * height) - (4.7 * age)
print("If you are a male, you'll need to eat" , (male/214) ,"chocolate bars to maintain your weight.")
print("If you are a female, you'll need to eat" , (female/214) ,"chocolate bars to maintain your weight.")
