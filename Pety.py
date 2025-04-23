class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 0  # 0 = full
        self.energy = 10  # 10 = fully rested
        self.happiness = 5  # Default happiness level
        self.tricks = []  # List to store learned tricks

    def eat(self):
        self.hunger = max(0, self.hunger - 3)  # Reduce hunger but not below 0
        self.happiness = min(10, self.happiness + 1)  # Increase happiness but not above 10
        print(f"{self.name} is eating...")

    def sleep(self):
        self.energy = min(10, self.energy + 5)  # Increase energy but not above 10
        print(f"{self.name} is sleeping...")

    def play(self):
        if self.energy >= 2:  # Ensure enough energy to play
            self.energy -= 2
            self.happiness = min(10, self.happiness + 2)  # Increase happiness but not above 10
            self.hunger = min(10, self.hunger + 1)  # Increase hunger but not above 10
            print(f"{self.name} is playing...")
        else:
            print(f"{self.name} is too tired to play!")

    def get_status(self):
        print(f"{self.name}'s current status:")
        print(f"Hunger: {self.hunger}")
        print(f"Energy: {self.energy}")
        print(f"Happiness: {self.happiness}")
        print(f"Tricks: {', '.join(self.tricks) if self.tricks else 'None'}")

    def train(self, trick):
        self.tricks.append(trick)  # Add the trick to the list
        self.happiness = min(10, self.happiness + 1)  # Increase happiness
        print(f"{self.name} learned a new trick: {trick}!")

    def show_tricks(self):
        if self.tricks:
            print(f"{self.name} knows the following tricks: {', '.join(self.tricks)}")
        else:
            print(f"{self.name} hasn't learned any tricks yet.")
            
            
if __name__ == "__main__":
    my_pet = Pet("Nyau")
    my_pet.eat()
    my_pet.play()
    my_pet.get_status()
    my_pet.train("roll over")
    my_pet.show_tricks()            