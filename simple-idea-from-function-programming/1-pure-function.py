from datetime import datetime
from functools import partial
from typing import Callable

# Group side effects and use pure functions
# version 1
"""
class Greeting:
    def __init__(self) -> None:
        current_time = datetime.now()
        if current_time.hour < 12:
            self.greeting_intro = "Good morning"
        elif 12 <= current_time.hour < 18:
            self.greeting_intro = "Good afternoon"
        else:
            self.greeting_intro = "Good evening"

    def greet(self, name: str)-> None:
        print(f"{self.greeting_intro}, {name}.")

    def greet_list(self, names: list[str])-> None:
        for name in names:
            self.greet(name)

def main() -> None:
    name = input("Enter your name: ")

    greeting = Greeting()
    greeting.greet(name)

if __name__ == "__main__":
    main()
"""

class Greeting:
    def __init__(self, greeting_intro: str) -> None:
        self.greeting_intro = greeting_intro

    def greet(self, name: str)-> str:
        return f"{self.greeting_intro}, {name}."

    def greet_list(self, names: list[str])-> list[str]:
        return [self.greet(name) for name in names]

def main() -> None:
    # Move `current_time` from initial of class, so it won't execute evety time class created.
    current_time = datetime.now()
    if current_time.hour < 12:
        greeting_intro = "Good morning"
    elif 12 <= current_time.hour < 18:
        greeting_intro = "Good afternoon"
    else:
        greeting_intro = "Good evening"

    name = input("Enter your name: ")

    greeting = Greeting(greeting_intro)
    # Pure function, so they can be test simply and clarly.
    # If you want to debug, you don't have to change the code inside the class.
    greet = greeting.greet(name)
    print(greet)
    greet_list = greeting.greet_list(["a", "b", "c"])
    print(greet_list)

if __name__ == "__main__":
    main()
