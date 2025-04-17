#Hacker Alias Generator 
print("Alias Generator V1.0 💻")
name = input("What's your name? ")
number = int(input("What's your favourite number? "))
colour = input("What's your favourite colour? (Red,Green,Blue,White,Black) ")

#Conditions
match colour:
    case "Black" | "black" :
        prefix = "Shadow"
    case "Red" | "red" :
        prefix = "Crimson"
    case "Green" | "green" :
        prefix = "Sage"
    case "Blue" | "blue" :
        prefix = "Cyber"
    case "White" | "white":
        prefix = "Ghost"
    case _:
        prefix = "Hacker"

if number < 5:
    suffix = "Malw"
elif number >= 5:
    suffix = "Exe"
else:
    suffix = "Zero"

alias = prefix + name.capitalize() + str(suffix)
print("Your Hacker Alias is: ", alias + "💀")

input("Press enter to exit...")