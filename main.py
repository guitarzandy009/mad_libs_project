#mad libs project by jabrils

#  initialize variables
theMatrix = ""
system = ""
neo = ""
enemy = ""
inside = ""
save = ""
unplugged = ""
fight = ""

profession = ["","","",""]
adj = ["",""]
#  get input from user
print("Welcome user!")
print("Let's play a game of madlibs!")
neo = input("please share with me your name: ")


# Getting the Matrix variable from user
print(f"Hello {neo}! Are you ready?")
theMatrix = input("What is something you want to know more about: ")

# Getting system variable from user
print(f"Oooh! You want to know more about {theMatrix} huh?")
print(f"Okay well first, tell me what you already know about {theMatrix}")
system = input(f"what noun would you categorize {theMatrix} as: ")

# Getting enemy variable from user
enemy = input(f"Give me an opposing noun to {system}: ")

# Getting inside varaible from user
inside = input(f"Now give me any relaxing noun (present tense): ")

# Getting all profession varible from user
print(f"Okay, now I need 4 professions relating to {system}")

for i in range(len(profession)):
    profession[i] = input(f"Profession (plural) {i+1} / {len(profession)}: ")

# Getting the save variable
save = input(f"Give me a helo-related verb (present tense): ")

# Getting the unplugged variable
unplugged = input(f"Now give me a verb that makes you think about relief (past tense): ")

# Getting the adjectives
print(f"Lastly I need 2 dystopian adjectives")

for i in range(len(adj)):
    adj[i] = input(f"Adjective {i+1} / {len(adj)}: ")
    
# Getting the fight variable
fight = input(f"& a verb: ")

#  init story
story = (f"{theMatrix} is a {system}, {neo}. That {system} is our {enemy}. But when you're {inside}, you look around, what do you see? {profession[0]}, {profession[1]}, {profession[2]}, {profession[3]}. The very minds of the people we are trying to {save}. But until we do, these people are still a part of that {system} and that makes them our {enemy}. You have to understand, most of these people are not ready to be {unplugged}. And many of them are so {adj[0]}, so hopelessly {adj[1]} on the {system}, that they will {fight} to protect it.")
#  print story

print (story)
input()
# Timestamp 1:15