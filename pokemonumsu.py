#ÇAĞATAY ATEŞ
#19010011056
import random
import os

pokemon = {}
def pokemoncreate():
    starter = 1
    starter2 = 1
    while starter == 1:
        pokeclass = []

        name = input("Would you want a give her/him name? you can do it: \n")
        if (name in pokemon):
            while starter == 1:
                name = input("This name already taken choose new name: \n")
                if(name in pokemon):
                    starter = 1
                else:
                    break

        temp = int(input("choose your pokemon \n 1-Pikachu 2-Charmander 3-Bulbasaur 4-Squirtle\n"))
        if (temp == 1):
            pokeclass.append("Pikachu")
            gender = int(input("You choose Pikachu. İt's gender is \n 1-Male 2-Female \n"))

            while starter2 == 1:
                if (gender == 1):
                    pokeclass.append("Male")
                    weightandheight = input("Enter weight and height: like (a(cm) , b(kg)) \n ")
                    pokeclass.append(weightandheight)
                    pokemon[name] = pokeclass
                    print(pokemon)
                    starter = 10
                    break

                elif (gender == 2):
                    pokeclass.append("Female")
                    weightandheight = input("Enter weight and height: like (a(cm) , b(kg)) \n ")
                    pokeclass.append(weightandheight)
                    pokemon[name] = pokeclass
                    print(pokemon)
                    starter = 10
                    break

                else:
                    print("press wrong number try again: ")
                    gender = int(input("You choose Pikachu. İt's gender is  \n 1-Male 2-Female \n"))

        elif (temp == 2):
            pokeclass.append("Charmander")
            gender = int(input("You choose Charmander. İt's gender is  \n 1-Male 2-Female \n"))

            while starter2 == 1:
                if (gender == 1):
                    pokeclass.append("Male")
                    weightandheight = input("Enter weight and height: like (a(cm) , b(kg)) \n ")
                    pokeclass.append(weightandheight)
                    pokemon[name] = pokeclass
                    print(pokemon)
                    starter = 10
                    break

                elif (gender == 2):
                    pokeclass.append("Female")
                    weightandheight = input("Enter weight and height: like (a(cm) , b(kg)) \n ")
                    pokeclass.append(weightandheight)
                    pokemon[name] = pokeclass
                    print(pokemon)
                    starter = 10
                    break

                else:
                    print("press wrong number try again: ")
                    gender = int(input("You choose Pikachu. İt's gender is  \n 1-Male 2-Female \n"))

        elif (temp == 3):
            pokeclass.append("Bulbsaur")
            gender = int(input("You choose Bulbasaur. İt's gender is  \n 1-Male 2-Female \n"))

            while starter2 == 1:
                if (gender == 1):
                    pokeclass.append("Male")
                    weightandheight = input("Enter weight and height: like (a(cm) , b(kg)) \n ")
                    pokeclass.append(weightandheight)
                    pokemon[name] = pokeclass
                    print(pokemon)
                    starter = 10
                    break

                elif (gender == 2):
                    pokeclass.append("Female")
                    weightandheight = input("Enter weight and height: like (a(cm) , b(kg)) \n ")
                    pokeclass.append(weightandheight)
                    pokemon[name] = pokeclass
                    print(pokemon)
                    starter = 10
                    break

                else:
                    print("press wrong number try again: ")
                    gender = int(input("You choose Bulbasaur. İt's gender is  \n 1-Male 2-Female \n"))


        elif (temp == 4):
            pokeclass.append("Squirtle")
            gender = int(input("You choose Squirtle. İt's gender is  \n 1-Male 2-Female \n"))

            while starter2 == 1:
                if (gender == 1):
                    pokeclass.append("Male")
                    weightandheight = input("Enter weight and height: like (a(cm) , b(kg)) \n ")
                    pokeclass.append(weightandheight)
                    pokemon[name] = pokeclass
                    print(pokemon)
                    starter = 10
                    break

                elif (gender == 2):
                    pokeclass.append("Female")
                    weightandheight = input("Enter weight and height: like (a(cm) , b(kg)) \n ")
                    pokeclass.append(weightandheight)
                    pokemon[name] = pokeclass
                    print(pokemon)
                    starter = 10
                    break

                else:
                    print("press wrong number try again: ")
                gender = int(input("You choose Squirtle. İt's gender is  \n 1-Male 2-Female \n"))

    text = open("Pokemon.txt", "a")
    text.write(str(pokemon))
    text.close()

def pokemondelete():
    starter = 1
    while starter == 1:
        print(pokemon)
        temp = input("Choose pokemon name for delete progress:\n")
        pokemon.pop(temp)
        starter = int(input("Press 1 to continue or press anything to exit\n"))

def pokemonupdate():
    print("Write the name of you want to update pokemon\n(name must be correct)\n")
    temp = pokemoncreate()
    pokemon.update(temp)

def pokemonseach():
    temp = input("Write the name you want to find data:\n")
    print("{}".format(pokemon[temp]))

def pokemonduel():
    attacks = []
    attacksop = []
    print(pokemon.items())

    name = input("write name your choosen pokemon:\n")
    temp = pokemon[name]

    if("Pikachu" in temp):
            attacks = ("Tackle", "Thunder Bolt")
    if("Charmander" in temp):
            attacks = ("Scratch", "Fire Breath")
    if("Squirtle" in temp):
            attacks = ("Tackle", "Water Gun")
    if("Bulbasaur" in temp):
            attacks = ("Headbut", "Razor Leaf" )

    oppenentname = input("write your oppenent name: \n")
    tempoppenent = pokemon[oppenentname]

    if ("Pikachu" in tempoppenent):
        attacksop = ("Tackle" , "Thunder Bolt")
    if ("Charmander" in tempoppenent):
        attacksop = ("Scratch" , "Fire Breath")
    if ("Squirtle" in tempoppenent):
        attacksop = ("Tackle" , "Water Gun")
    if ("Bulbasaur" in tempoppenent):
        attacksop = ("Headbut" , "Razor Leaf")

    health1 = 50
    health2 = 50
    int(health1)
    int(health2)
    def fightscene(health2, health1, attacks):
        starter = 1
        while starter == 1:
            os.system('cls')

            def battle(a , b):
                print("\n{}  {}\n ".format(oppenentname , a))
                print("\n")
                print("\n")
                print("\n")
                print("\n")
                print(" {} \n".format(attacks[0]))
                print(" {} \n".format(attacks[1]))
                print("{}  {}".format(name , b))

            battle(health2, health1)

            attack = int(input("ilk sarldırı içim 0 ikincisi için 1 girin\n"))
            damage = random.randint(5, 15)
            health2 = health2 - damage
            print("You choose {} it gaves {} damage".format(attacks[attack], damage))
            damage2 = random.randint(5 , 15)
            health1 = health1 - damage2
            x = random.randint(0, 1)
            print("Oppenent choose {} it gaves {} damage".format(attacksop[x], damage2))


            if (health2 <= 0):
                print("match finihed you Won")
                starter = 10
                return starter
            if (health1 <= 0):
                print("match finihed you Failed")
                starter = 10
                return starter



    fightscene(health2, health1, attacks)


start = 1                              # menü
while start == 1:
    gametype = int(input("Pokemon Game\n \n1- Pokemon Creating\n2- Pokemon Fights\n3- Exit\n"))

    if (gametype == 1):
        temp = int(input("1- Create Pokemon\n2- Delete Pokemon\n3- Update Pokemon\n4- Find Your Pokemon\n"))
        if(temp == 1):
            pokemoncreate()
        if(temp == 2):
            pokemondelete()
        if(temp == 3):
            pokemonupdate()
        if(temp == 4):
            pokemonseach()
    if(gametype == 2):
        pokemonduel()
    if(gametype == 3):
        starter = 10
        break