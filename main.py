from pet import Pet

def main():
     my_pet = Pet(name="Minny", hunger=2, energy=5, happiness=7)
     my_pet.get_status()

     #eating
     my_pet.eat()
     my_pet.get_status()

    #  #sleeping
    #  my_pet.sleep()
    #  my_pet.get_status()

    #  #playing
    #  my_pet.play()
    #  my_pet.get_status()

    #  my_pet.train("sit")
    #  my_pet.train("roll over")
    #  my_pet.show_tricks()


if __name__ == "__main__":
      main()