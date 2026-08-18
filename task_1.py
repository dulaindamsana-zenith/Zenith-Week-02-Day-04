import random

"""Random's Randint"""
random_int = random.randint(a=1, b=100)

print(random_int)



"""Random's Random"""
random_floating_points = random.random()

print (random_floating_points)



"""Random's Uniform"""
random_float = random.uniform(1, 100)

print(random_float)



"""Random's Choice"""
char = ["Dulain", "Colabage", "Damsana", "DCD"]

random_choice = random.choice(char)

print(random_choice)



"""Random's Choices"""
char = ["Dullain", "Colabage", "Damsana", "DCD"]

random_choices = random.choices(char, k=3)

for i in random_choices:
        print(i)