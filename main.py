import string
import random

possible_true_values = ['true', '1', 't', 'y', 'yes', 'yeah']
def generate_password(type_of_password, length):
    characters = ""
    if(type_of_password["lower_case"].lower() in possible_true_values):
        characters = string.ascii_lowercase
    if(type_of_password["upper_case"].lower() in possible_true_values):
        characters += string.ascii_uppercase
    if(type_of_password["numbers"].lower() in possible_true_values):
        characters += string.digits
    if(type_of_password["punctuation"].lower() in possible_true_values):
        characters += string.punctuation
    return "".join(random.choice(characters) for _ in range(length))

type_of_password = {}

print("Include (true, 1, t are acceptable values): ")
type_of_password["lower_case"] = input("Lowercase letters: ")
type_of_password["upper_case"] = input("Uppercase letters: ")
type_of_password["numbers"] = input("Numbers: ")
type_of_password["punctuation"] = input("Symbols(e.g. @!#): ")
length = int(input("Enter the length of the password: "))
print(generate_password(type_of_password, length))