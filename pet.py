class Pet:
    def __init__ (self, name, hunger, energy, happiness):
        self.name = name
        self.hunger = hunger #hunger level (0 = full, 10 = very hungry)
        self.energy = energy #energy level (0 = tired, 10 = fully rested)
        self.happiness = happiness # (0–10)
        self.tricks = []

    def eat(self): #reduces hunger by 3 points (but not below 0), and increases happiness by 1.
        if self.hunger >= 3:
            self.hunger -= 3
        else:
            self.hunger = 0

        if self.happiness < 10:
            self.happiness += 1
        
    def sleep(self): #increases energy by 5 points (but not above 10).
        if self.energy <= 5:
            self.energy += 5
        else:
            self.energy = 10


    def play(self):  #decreases energy by 2, increases happiness by 2, and increases hunger by 1.
        if self.energy >= 2:
            self.energy -= 2
        else:
            self.energy = 0

        if self.happiness < 9:
            self.happiness += 2
        else:
            self.happiness = 10

        if self.hunger < 10:
            self.hunger += 1

    def get_status(self): #prints the current state of the pet.
        print(f"{self.name}'s Current status is: ")
        print(f"Hunger: {self.hunger}")
        print(f"Energy: {self.energy}")
        print(f"Happiness: {self.happiness}")

    def train(self, trick): #Add a method train(trick) that teaches your pet a new trick and stores it in a list.
        if trick not in self.tricks:
            self.tricks.append(trick)
            print(f"{self.name} learned a new trick: {trick}!")
        else:
            print(f"{self.name} already knows {trick}!")

    
    def show_tricks(self): #Add a method show_tricks() that prints all learned tricks.
        if self.tricks:
            print(f"{self.name} knows these tricks: {', '.join(self.tricks)}")
        else:
            print(f"{self.name} hasn't learned any tricks yet.")
