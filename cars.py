# Using set() to create a set
# languages = set()

# Using curly braces allows you to initialize the set with values
# languages = { 'english', 'mandarin chinese', 'spanish', 'english', 'spanish', 'portugese' }


# print(languages)

# showroom = set()
showroom = { 'Ford Mustang Mach-E', 'Tesla Model X', 'Honda Element', 'Mercedes E320' }

print("SHOWROOM LENGTH: ", len(showroom))
print("SHOWROOM: ", showroom)

showroom.add('Ford Mustang Mach-E')

print("SHOWROOM LENGTH: ", len(showroom))
print("SHOWROOM: ", showroom)

showroom_update = { 'McLaren P1', 'Ford Pinto' }

showroom.update(showroom_update)

print("SHOWROOM LENGTH: ", len(showroom))
print("SHOWROOM: ", showroom)

showroom.discard('Tesla Model X')

print("SHOWROOM LENGTH: ", len(showroom))
print("SHOWROOM: ", showroom)

junkyard = { 'Ford Mustang', 'Tesla Model E', 'McLaren P1', 'Honda Civic', 'Mercedes E320' }

print("JUNKYARD: ", junkyard)

print("OVERLAP: ", showroom.intersection(junkyard))

showroom = showroom.union(junkyard)
print("SHOWROOM: ", showroom)
showroom.discard('Tesla Model E')
print("SHOWROOM: ", showroom)