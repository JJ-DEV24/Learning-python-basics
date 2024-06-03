"""JJ's_Sims is a virtual reality game that allows the user to create three different characters. The user can decide
who their characters interact with and ultimately have full control over their lives

Let the games begin 😎"""


# Characters
class Character_2:
    def __init__(self, name: str, age: int, gender: str, height: str, fav_drink: str, hobby: str):
        self.name = name
        self.age = age
        self.gender = gender
        self.height = height
        self.fav_drink = fav_drink
        self.hobby = hobby
        self.single_pringle = True
        self.drunk = False
        self.at_work = False
    def __str__(self):
        return str(self.name)

class Character:
    def __init__(self, name: str, age: int, gender: str, height: str, fav_drink: str, hobby: str):
        self.name = name
        self.age = age
        self.gender = gender
        self.height = height
        self.fav_drink = fav_drink
        self.hobby = hobby
        self.single_pringle = True
        self.drunk = False
        self.at_work = False

    def __str__(self) -> str:
        return str(self.name)


    def greet_1(self, fellow: Character_2) -> int:
        if fellow and self.single_pringle == True or False:
            print(f'Hello, {fellow}! Did you watch the news last night?')

    def flirt(self, fellow: Character_2):
        if self.single_pringle == True:
            self.single_pringle = False
            fellow.single_pringle = False
            return f"You're the apple of my eye and I've fallen in love with you, {fellow}. Lets get married!"

    def greet_2(self, fellow):
        if self.single_pringle == False:
            print(f"Hi, {fellow}. How's my sugar dumpling doing?")

    def go_to_work(self):
        if self.drunk == False:
            print("Welp, guess it's time to go to work.")
            self.at_work = True
        if self.drunk == True:
            print("Dang it! I had too much to drink last night. Guess I gotta call in sick to work... mwahaha!")
            self.drunk = True
            self.at_work = False

    def drink(self):
        print(f"I.... need... a glass... of... {self.fav_drink}!")
        self.drunk = True

    def start_hobby(self):
        self.drunk = False
        if self.at_work == True:
            print(f"Man I wish I could do some {self.hobby} but I'm at work right now...")
        if self.at_work == False:
            if self.hobby != self.hobby:
                print(f"Wow, I've loads of free time on my hands! Time to do some {self.hobby}")
            if self.hobby == self.hobby:
                print(f"Hey, {self.name}, wanna do some {self.hobby} together?")


jess = Character('Jess', 26, 'Female', '5"4', 'moscato wine', 'painting')
pedro = Character_2('Pedro', 30, 'Male', '6"0', 'whisky', 'coding')
sandra = Character_2('Sandra', 34, 'Female', '3"7', 'tonka beans', 'ballet')

print(jess.__dict__)
print(pedro.__dict__)
print(sandra.__dict__)

jess.greet_1(pedro)
print(pedro)
print(pedro.single_pringle)

i_do = jess.flirt(pedro)
print(i_do)
print(jess.single_pringle)
print(pedro.single_pringle)

print(jess.greet_1(sandra))
