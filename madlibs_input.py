print("Welcome to Python MadLibs! Enter the requested word type, and see the result! Have fun!")
print("The more creative your word choices, the funnier the result will be! So be creative!")
print("If you're stumped, no worries. Just hit return, and a word will be chosen for you.\n")


print("Enter a noun- a person, place or thing.\n")
noun1 = raw_input()
if noun1 == "":
    noun1 = "prom dress"

print("Enter another noun.\n")
noun2 = raw_input()
if noun2 == "":
    noun2 = "hockey puck"

print("Enter one of the 50 states in the U.S.A. For example, Rhode Island.\n")
state1 = raw_input()
if state1 == "":
    state1 = "Rhode Island"

print("Enter a second U.S. state.\n")
state2 = raw_input()
if state2 == "":
    state2 = "New Jersey"

print("Enter another noun. Isn't this exciting?\n")
noun3 = raw_input()
if noun3 == "":
    noun3 = "glue gun"

print("Enter an adjective- a word that describes a noun- like sparkly, splintered, or slippery.\n")
adjective1 = raw_input()
if adjective1 == "":
    adjective1 = "frothy"

print("Enter another noun. Make it a good one!\n")
noun4 = raw_input()
if noun4 == "":
    noun4 = "armadillo"

print("Enter another adjective. You're getting close!\n")
adjective2 = raw_input()
if adjective2 == "":
    adjective2 = "chartruese"

print("Enter another noun. You're really curious now, aren't you?\n")
noun5 = raw_input()
if noun5 == "":
    noun5 = "shampoo"

print("Enter one more noun. You're doing great!\n")
noun6 = raw_input()
if noun6 == "":
    noun6 = "dishtowel"

print("Enter a boy's name.\n")
boy = raw_input()
if boy == "":
    boy = "Donny"

print("Enter a girl's name.\n")
girl = raw_input()
if girl == "":
    girl = "Marie"

print("You did a fantastic job! Here's your MadLib. Enjoy, and thanks for playing!\n")

# song
print("This " + noun1 + " is your " + noun1 + ",")
print("This " + noun2 + " is your " + noun2 + ",")
print("From " + state1 + " to the " + state2 + " " + noun3 + "!")
print("From the " + adjective1 + " " + noun4 + ",")
print("To the " + adjective2 + " " + noun5 + ",")
print("This " + noun6 + " was made for " + boy + " and " + girl + ".")
