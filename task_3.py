import random

victims = ["vishwa umayanga", "buwanajith randira", "rajan wikrama", "deniel peirogi", "nuwan tharindu", "sachintha nimesh"]
victim_device = ["Laptop", "Computer", "Mobile Phone"]
which_virus = ["Malware", "Ransomeware", "Adware", "DDoS", "WannaCry", "Mydoom", "Stuxnet"]
how_many = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

target = random.choice(victims)
target_device = random.choice(victim_device)
inserting_virus = random.choice(which_virus)
exact_count = random.choice(how_many)

print(f"Hacker Dulain confirmed the '{target}' is our target victim today!")
print(f"Let's get the access to the {target}'s {target_device}")

if exact_count > 1:
        print(f"Then insert {exact_count} {inserting_virus}s to the {target}'s {target_device}")

else:
        print(f"Then insert {exact_count} {inserting_virus} to the {target}'s {target_device}")
