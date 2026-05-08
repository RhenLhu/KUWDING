import random

def UI():
    print("Welcome to TaleUnder")
    print("[1] Play")
    print("[2] Exit")

def UI2():
    print("\nThe rules are simple!")
    print("Kill The enemies before they kill you")
    print("Kill or Be Killed!")
    print("When Your Hp drops to 0, You Lose")
    print("[1] Start")
    print("[2] Back Out (Exit)")

def Class():
    print("\nPlease Pick a Class")
    print("[1] Fighter")
    print("[2] Assassin")
    print("[3] Healer")

def ShopUI():
    print("\nWelcome to The Shop!!")
    print("How Can I help You")
    print("[1] Buy")
    print("[2] Sell")
    print("[3] Exit")

def Move():
    print("[1] Enter Dungeon")
    print("[2] Check Stats")
    print("[3] Go to Shop")

def Battle():
    print("[1] Fight")
    print("[2] Act")
    print("[3] Item")
    print("[4] Spare")

def Act():
    print("\n=== Act ===")
    print("[1] Check")
    print("[2] Dodge")
    print("[3] Intimidate")
    print("[4] Back")

def Item():
    print("\n=== Items ===")
    print("[1] Potion (Heals 10 HP)")
    print("[2] Back\n")

def Spare():
    print("\n=== Spare ===")
    print("[1] Run!")
    print("[2] Back\n")

def spawn_monster(monsters):
    name, stats = random.choice(list(monsters.items()))
    return name, stats

def spawn_boss(Bosses):
    Bname, Bstats = random.choice(list(Bosses.items()))
    return Bname, Bstats

def player_stats(player):
    for x, y in player.items():
        print(f"{x}: {y}")

def rewards(player, Mstats):

    gold = Mstats["Gold"]
    exp = Mstats["Exp"]

    player["Gold"] += gold
    player["Exp"] += exp

    print(f"You gained {gold} Gold!")
    print(f"You gained {exp} EXP!\n")

def player_atk(Mhp, Patk):
    Pdamage = Patk - Mdef
    Mhp -= Pdamage
    print(f"You attacked {Mname} and inflicted {Pdamage} damage")
    print(f"{Mname} HP is now {Mhp}\n")
    return Mhp

def enemy_atk(Php, Matk):
    damage = random.randint(5, Matk)
    final_damage = damage - Pdef
    itspi = player["Hp"]
    Php -= final_damage
    Php = max(0, min(Php, itspi))
    print(f"The monster dealt {final_damage} damage to you!")
    print(f"Your HP has dropped to {Php}\n")
    return Php


player = {
    "Name": "Pliyer",
    "Class": "class",
    "Hp": 25,
    "Atk": 18,
    "Def": 5,
    "Gold": 0,
    "Exp": 0,
    "Inventory" : {
    "Potion": 3
    }
}

monsters = {
    "TiggorF": {"Hp": 30, "Atk": 13, "Def": 5,"Gold": 20,"Exp": 10},
    "NusmihW": {"Hp": 10, "Atk": 11, "Def": 2,"Gold": 2,"Exp": 2},
    "XooL": {"Hp": 50, "Atk": 14, "Def": 8,"Gold": 5,"Exp": 7},
    "PsogiM": {"Hp": 40, "Atk": 11, "Def": 6,"Gold": 2,"Exp": 5}
}

Bosses = {
    "Toriel": {"Hp": 80, "Atk": 15, "Def": 6,"Gold": 1000,"Exp": 1000},
    "Asgore": {"Hp": 150, "Atk": 18, "Def": 12,"Gold": 5000,"Exp": 10000},
    "Undyne": {"Hp": 120, "Atk": 17, "Def": 8,"Gold": 2500,"Exp": 7500},
    "Sans": {"Hp": 100, "Atk": 10, "Def": 7,"Gold": 2000,"Exp": 5500}
}

Php = player["Hp"]
Patk = player["Atk"]
Pdef = player["Def"]
stage = 1
max_kills = 4
while True:
    UI()
    choice = input("Select your action: ")

    while True:
        if choice == "1":
            print("\nYou are now playing the game")
            Pn = input("Please enter Player name: ").capitalize()
            print(f"\nWelcome To The Game {Pn}!")
            player.update({"Name": Pn})

            UI2()
            act = input("Shall we start the Adventure? [1/2]: ")

            Class()
            class_choice = input("What do you prefer? [1/2/3]: ")

            while True:
                if act == "1":
                    if class_choice == "1":
                        cl = "Fighter"
                        hp = 25
                        df = 10
                        player.update({"Class": cl})
                        player.update({"Hp": hp})
                        player.update({"Def": df})
                        Pdef = player["Def"]
                        Php = player["Hp"]
                        print("\nPerfect! Now then...")
                        Move()
                        move = input("What should be your next Move? [1/2/3]: ")
                        if move == "1":
                            kills = 0
                            print(f"\nYou've now entered Dungeon {stage}")

                            Mname, Mstats = spawn_monster(monsters)
                            Mhp = Mstats["Hp"]
                            Matk = Mstats["Atk"]
                            Mdef = Mstats["Def"]

                            while True:
                                print(f"\nYou have encountered {Mname}")
                                Battle()
                                battle = input("What should be your next Move? [1/2/3/4]: ")

                                if battle == "1":
                                    Mhp = player_atk(Mhp, Patk)
                                    Php = enemy_atk(Php, Matk)

                                    player["Hp"] = Php

                                    if Mhp <= 0:
                                        print(f"\n{Mname} defeated!")

                                        rewards(player, Mstats)

                                        kills += 1
                                        print(f"Monsters defeated: {kills}/{max_kills}")

                                        if kills >= max_kills:
                                            print("Dungeon Cleared!")
                                            stage += 1
                                            max_kills += 2
                                            break
                                        
                                        Mname, Mstats = spawn_monster(monsters)
                                        Mhp = Mstats["Hp"]
                                        Matk = Mstats["Atk"]
                                        continue

                                    if Php <= 0:
                                        print("You died!")
                                        quit()

                                elif battle == "2":
                                    Act()
                                    act_choice = input("What to do? [1/2/3/4]: ")

                                    if act_choice == "1":
                                        print(f"{Mname}:{Mstats}")

                                    elif act_choice == "2":
                                        print("")

                                    elif act_choice == "3":
                                        print(f"You intimidated {Mname}!")
                                        print(f"{Mname}'s atk Dropped!")
                                        Matk = max(1, int(Matk * 0.9))

                                    elif act_choice == "4":
                                        continue
                                elif battle == "3":
                                    Item()
                                    item_choice = input("Choose item: ")

                                    if item_choice == "1":
                                        if player["Inventory"]["Potion"] > 0:
                                            player["Hp"] += 10
                                            
                                            player["Hp"] = min(player["Hp"], 25)
                                            Php = player["Hp"]
                                            player["Inventory"]["Potion"] -= 1
                        
                                            print("You used a Potion!")
                                            print(f"Your HP is now {player['Hp']}")
                                            print(f"Potions left: {player['Inventory']['Potion']}")

                                        else:
                                            print("No Potions left!")

                                    elif item_choice == "2":
                                        continue

                                elif battle == "4":
                                    Spare()
                                    spare_choice = input("What to do? [1/2]: ")
                                    
                                    if spare_choice == "1":
                                        
                                        print("You Ran away!")
                                        print("Your progress won't be saved :p")
                                        break
                                    
                                    elif spare_choice == "2":
                                        continue


                        elif move == "2":
                            player_stats(player)

                        elif move == "3":
                            pass

                    elif class_choice == "2":
                        cl = "Assassin"
                        hp = 20
                        atk = 25
                        player.update({"Class": cl})
                        player.update({"Hp": hp})
                        player.update({"Atk": atk})
                        Patk = player["Atk"]
                        Php = player["Hp"]
                        print("\nPerfect! Now then...")
                        Move()
                        move = input("What should be your next Move? [1/2/3]: ")
                        if move == "1":
                            kills = 0
                            print(f"\nYou've now entered Dungeon {stage}")

                            Mname, Mstats = spawn_monster(monsters)
                            Mhp = Mstats["Hp"]
                            Matk = Mstats["Atk"]
                            Mdef = Mstats["Def"]

                            while True:
                                print(f"\nYou have encountered {Mname}")
                                Battle()
                                battle = input("What should be your next Move? [1/2/3/4]: ")

                                if battle == "1":
                                    Mhp = player_atk(Mhp, Patk)
                                    Php = enemy_atk(Php, Matk)

                                    player["Hp"] = Php

                                    if Mhp <= 0:
                                        print(f"\n{Mname} defeated!")

                                        rewards(player, Mstats)

                                        kills += 1
                                        print(f"Monsters defeated: {kills}/{max_kills}")

                                        if kills >= max_kills:
                                            print("Dungeon Cleared!")
                                            stage += 1
                                            max_kills += 2
                                            break
                                        
                                        Mname, Mstats = spawn_monster(monsters)
                                        Mhp = Mstats["Hp"]
                                        Matk = Mstats["Atk"]
                                        continue

                                    if Php <= 0:
                                        print("You died!")
                                        quit()

                                elif battle == "2":
                                    Act()
                                    act_choice = input("What to do? [1/2/3/4]: ")

                                    if act_choice == "1":
                                        print(f"{Mname}:{Mstats}")

                                    elif act_choice == "2":
                                        print("")

                                    elif act_choice == "3":
                                        print(f"You intimidated {Mname}!")
                                        print(f"{Mname}'s atk Dropped!")
                                        Matk = max(1, int(Matk * 0.9))

                                    elif act_choice == "4":
                                        continue
                                elif battle == "3":
                                    Item()
                                    item_choice = input("Choose item: ")

                                    if item_choice == "1":
                                        if player["Inventory"]["Potion"] > 0:
                                            player["Hp"] += 10
                                            
                                            player["Hp"] = min(player["Hp"], 20)
                                            Php = player["Hp"]
                                            player["Inventory"]["Potion"] -= 1
                        
                                            print("You used a Potion!")
                                            print(f"Your HP is now {player['Hp']}")
                                            print(f"Potions left: {player['Inventory']['Potion']}")

                                        else:
                                            print("No Potions left!")

                                    elif item_choice == "2":
                                        continue

                                elif battle == "4":
                                    Spare()
                                    spare_choice = input("What to do? [1/2]: ")
                                    
                                    if spare_choice == "1":
                                        
                                        print("You Ran away!")
                                        print("Your progress won't be saved :p")
                                        break
                                    
                                    elif spare_choice == "2":
                                        continue


                        elif move == "2":
                            player_stats(player)

                        elif move == "3":
                            pass

                    elif class_choice == "3":
                        cl = "Healer"
                        hp = 30
                        atk = 13
                        df = 7
                        player.update({"Class": cl})
                        player.update({"Hp": hp})
                        player.update({"Def": df})
                        Patk = player["Atk"]
                        Pdef = player["Def"]
                        Php = player["Hp"]
                        player["Inventory"]["Potion"] = 7
                        print("\nPerfect! Now then...")
                        Move()
                        move = input("What should be your next Move? [1/2/3]: ")
                        if move == "1":
                            kills = 0
                            print(f"\nYou've now entered Dungeon {stage}")

                            Mname, Mstats = spawn_monster(monsters)
                            Mhp = Mstats["Hp"]
                            Matk = Mstats["Atk"]
                            Mdef = Mstats["Def"]

                            while True:
                                print(f"\nYou have encountered {Mname}")
                                Battle()
                                battle = input("What should be your next Move? [1/2/3/4]: ")

                                if battle == "1":
                                    Mhp = player_atk(Mhp, Patk)
                                    Php = enemy_atk(Php, Matk)

                                    player["Hp"] = Php

                                    if Mhp <= 0:
                                        print(f"\n{Mname} defeated!")

                                        rewards(player, Mstats)

                                        kills += 1
                                        print(f"Monsters defeated: {kills}/{max_kills}")

                                        if kills >= max_kills:
                                            print("Dungeon Cleared!")
                                            stage += 1
                                            max_kills += 2
                                            break
                                        
                                        Mname, Mstats = spawn_monster(monsters)
                                        Mhp = Mstats["Hp"]
                                        Matk = Mstats["Atk"]
                                        continue

                                    if Php <= 0:
                                        print("You died!")
                                        quit()

                                elif battle == "2":
                                    Act()
                                    act_choice = input("What to do? [1/2/3/4]: ")

                                    if act_choice == "1":
                                        print(f"{Mname}:{Mstats}")

                                    elif act_choice == "2":
                                        print("")

                                    elif act_choice == "3":
                                        print(f"You intimidated {Mname}!")
                                        print(f"{Mname}'s atk Dropped!")
                                        Matk = max(1, int(Matk * 0.9))

                                    elif act_choice == "4":
                                        continue
                                elif battle == "3":
                                    Item()
                                    item_choice = input("Choose item: ")

                                    if item_choice == "1":
                                        if player["Inventory"]["Potion"] > 0:
                                            player["Hp"] += 25
                                            
                                            player["Hp"] = min(player["Hp"], 30)
                                            Php = player["Hp"]
                                            player["Inventory"]["Potion"] -= 1
                        
                                            print("You used a Potion!")
                                            print(f"Your HP is now {player['Hp']}")
                                            print(f"Potions left: {player['Inventory']['Potion']}")

                                        else:
                                            print("No Potions left!")

                                    elif item_choice == "2":
                                        continue

                                elif battle == "4":
                                    Spare()
                                    spare_choice = input("What to do? [1/2]: ")
                                    
                                    if spare_choice == "1":
                                        
                                        print("You Ran away!")
                                        print("Your progress won't be saved :p")
                                        break
                                    
                                    elif spare_choice == "2":
                                        continue


                        elif move == "2":
                            player_stats(player)

                        elif move == "3":
                            pass

        else:
            print("You've quit the game")
            break
    break
