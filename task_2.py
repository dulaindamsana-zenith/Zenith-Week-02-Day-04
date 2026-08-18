rats_for_hackers = [
        "any desk",
        "screen connect",
        "team viewer",
        "remote pc",
        "connect wise",
        "remotely",
        "air droid",
        "mirror droid"
]

"""List Overwrite"""
rats_for_hackers[7] = ""

print(rats_for_hackers)



"""List Indexing (Positive)"""
print(rats_for_hackers[0])



"""List Indexing (Negetive)"""
print(rats_for_hackers[-1])



"""List item adding (only one)"""
rats_for_hackers.append("screen share")

print(rats_for_hackers)



"""List items adding (more)"""
more_rats = ["over air", "double apple"]

rats_for_hackers.extend(more_rats)

print(rats_for_hackers)



"""List item adding (specific place)"""
rats_for_hackers.insert(5, "rust desk")

print(rats_for_hackers)



"""List item removing (by name)"""
rats_for_hackers.remove("screen connect")

print(rats_for_hackers)



"""List item removing (by index)"""
rats_for_hackers.pop(3)

print(rats_for_hackers)



"""List items removing (all)"""
rats_for_hackers.clear()

print(rats_for_hackers)