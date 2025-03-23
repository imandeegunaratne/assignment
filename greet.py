import datetime
import random

def greet():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    current_hour = datetime.datetime.now().hour

    if current_hour < 12:
        greeting = "Good morning"
    elif current_hour < 18:
        greeting = "Good afternoon"
    else:
        greeting = "Good evening"

    print(f"{greeting}, {name}! Welcome to Git.")
    age_message = "Enjoy life!" if age < 18 else "Make the most of your time!"
    print(f"{greeting}, {name}! {age_message}")

quotes = [
    "Believe in yourself!",
    "Never stop learning!",
    "Hard work pays off!"
]
print("Here's a motivational quote for you:", random.choice(quotes))

if __name__ == "__main__":
    greet()

