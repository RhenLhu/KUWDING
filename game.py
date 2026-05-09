import random

def UI():
    print(f"\033[33m=====Welcome to TaleUnder=====")
    print("[1] Play")
    print("[2] Exit\033[0m")

def UI2():
    print("\n\033[33mThis game is simple!\033[0m")
    print("Kill The enemies before they kill you")
    print("Because in this world, it's")
    print("\033[31mKill or Be Killed!")
    print("When Your Hp drops to 0, You Lose!!\033[0m")
    print("Anyways...")
    print("[1] Start")
    print("[2] Back Out (Exit)")

def Class():
    print("\nPlease Pick a Class:")
    print("[1] Fighter")
    print("[2] Assassin")
    print("[3] Healer")

def ShopUI():
    print("\nWelcome to The Shop!!")
    print("How Can I help You")
    print("[1] Buy")
    print("[2] Exit")

def show_shop(shop):
    i = 1
    print("\n=== SHOP ===")

    for item, info in shop.items():
        print(f"[{i}] {item} - {info['Price']} Gold")
        i += 1
        continue
    print(f"[{i}] Exit")

def buy_item(player, shop):

    while True:

        show_shop(shop)

        print(f"Current Gold: {player["Gold"]}")

        choice = input("What do you want to buy?: ")

        if choice == "1":

            item_name = "Potion"
            price = shop[item_name]["Price"]

            if player["Gold"] >= price:

                player["Gold"] -= price
                player["Inventory"]["Potion"] += 1

                print(f"You bought {item_name}!")

            else:
                print("Not enough Gold!")

        elif choice == "2":

            item_name = "True Knife (+Atk)"
            price = shop[item_name]["Price"]

            if player["Gold"] >= price:

                player["Gold"] -= price

                if item_name in player["Inventory"]:
                    print("You already own this item!")
                else:
                    player["Inventory"][item_name] = 1

                print(f"You bought {item_name}!")

            else:
                print("Not enough Gold!")

        elif choice == "3":

            item_name = "Heart Locket (+Def)"
            price = shop[item_name]["Price"]

            if player["Gold"] >= price:

                player["Gold"] -= price

                if item_name in player["Inventory"]:
                    print("You already own this item!")
                else:
                    player["Inventory"][item_name] = 1

                print(f"You bought {item_name}!")

            else:
                print("Not enough Gold!")

        elif choice == "4":
            break

        else:
            print("Invalid choice!")

def Move():
    print("[1] Enter Dungeon")
    print("[2] Check Stats")
    print("[3] Go to Shop")
    print("[4] Items")

def Battle():
    print("[1] Fight")
    print("[2] Act")
    print("[3] Item")
    print("[4] Spare")

def Act():
    print("\n=== Act ===")
    print("[1] Check")
    print("[2] Use Special Skill!!")
    print("[3] Intimidate")
    print("[4] Back")

def Item():
    i = 1
    print("\n=== Item ===")

    inventory_items = list(player["Inventory"].items())

    while i <= 3:
        if i <= len(inventory_items):
            item, amount = inventory_items[i - 1]
            print(f"[{i}] {item}: {amount}")
        else:
            print(f"[{i}] ---")
        i += 1

    print("[4] Exit")

def use_item1(player, item_name):    
    global Patk
    if item_name in player["Inventory"]:
    
        if item_name == "True Knife (+Atk)":
            if "Assassin" in player["Class"]:

                player["Atk"] += 40
                cl["cl2"]["Atk"] += 40
                
                Patk = player["Atk"]

                print("You equipped True Knife!")
                print("Attack increased by 40!")

                del player["Inventory"]["True Knife (+Atk)"]

            elif "Healer" in player["Class"]:
                player["Atk"] += 40
                cl["cl3"]["Atk"] += 40
                
                Patk = player["Atk"]

                print("You equipped True Knife!")
                print("Attack increased by 40!")

                del player["Inventory"]["True Knife (+Atk)"]
            
            else:
                player["Atk"] += 40
                Patk = player["Atk"]

                print("You equipped True Knife!")
                print("Attack increased by 40!")

                del player["Inventory"]["True Knife (+Atk)"]

def use_item2(player, item_name):    
    global Pdef
    if item_name in player["Inventory"]:

        if item_name == "Heart Locket (+Def)":
            if "Fighter" in player["Class"]:
                
                player["Def"] += 40
                cl["cl1"]["Def"] += 40      
                
                Pdef = player["Def"]

                print("You equipped Heart Locket!")
                print("Defense increased by 40!")

                del player["Inventory"]["Heart Locket (+Def)"]

            elif "Healer" in player["Class"]:
                
                player["Def"] += 40
                cl["cl3"]["Def"] += 40      
                
                Pdef = player["Def"]

                print("You equipped Heart Locket!")
                print("Defense increased by 40!")

                del player["Inventory"]["Heart Locket (+Def)"]
            
            else:
                player["Def"] += 40   
                
                Pdef = player["Def"]

                print("You equipped Heart Locket!")
                print("Defense increased by 40!")

                del player["Inventory"]["Heart Locket (+Def)"]

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
    Skill_points = Mstats["Skill Points"]

    player["Gold"] += gold
    player["Skill Points"] += Skill_points

    print(f"You gained {gold} Gold!")
    print(f"You gained {Skill_points} Skill Points!\n")

def boss_rewards(player, Bstats):

    gold = Bstats["Gold"]
    Skill_points = Bstats["Skill Points"]

    player["Gold"] += gold
    player["Skill Points"] += Skill_points

    print(f"You gained {gold} Gold!")
    print(f"You gained {Skill_points} Skill Points!\n")

def player_atk(Mhp, Patk):
    Pdamage = Patk - Mdef
    Mhp -= Pdamage
    print(f"You attacked {Mname} and inflicted {Pdamage} damage")
    print(f"{Mname} HP is now {Mhp}\n")
    return Mhp

def player_atk_boss(Bhp, Patk):
    Pdamage = Patk - Mdef
    Bhp -= Pdamage
    print(f"You attacked {Bname} and inflicted {Pdamage} damage")
    print(f"{Bname} HP is now {Bhp}\n")
    return Bhp

def boss_atk(Php, Batk):
    damage = random.randint(5, Batk)
    final_damage = damage - Pdef
    itspi = player["Hp"]
    Php -= final_damage
    Php = max(0, min(Php, itspi))
    print(f"The monster dealt {final_damage} damage to you!")
    print(f"Your HP has dropped to {Php}\n")
    return Php

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
    "Skill Points": 0,
    "Inventory" : {
    "Potion": 3
    }
}

cl = {
        "cl1": {
        "Class" : "Fighter",
        "Hp" : 40,
        "Def" : 10
    },
        "cl2": {
        "Class" : "Assassin",
        "Hp" : 30,
        "Atk" : 25
    },
        "cl3": {
        "Class" : "Healer",
        "hp" : 70,
        "Atk" : 13,
        "Def" : 7
        }
}
shop = {
    "Potion": {
        "Price": 25
    },

    "True Knife (+Atk)": {
        "Price": 700
    },

    "Heart Locket (+Def)": {
        "Price": 650
    }
}

monsters = {
    "TiggorF": {"Hp": 35, "Atk": 15, "Def": 5,"Gold": 20,"Skill Points": 16},
    "NusmihW": {"Hp": 25, "Atk": 17, "Def": 2,"Gold": 50,"Skill Points": 7},
    "XooL": {"Hp": 55, "Atk": 16, "Def": 8,"Gold": 35,"Skill Points": 9},
    "PsogiM": {"Hp": 45, "Atk": 16, "Def": 6,"Gold": 24,"Skill Points": 7}
}

Bosses = {
    "Toriel": {"Hp": 100, "Atk": 22, "Def": 6,"Gold": 1000,"Skill Points": 1000},
    "Asgore": {"Hp": 160, "Atk": 23, "Def": 12,"Gold": 5000,"Skill Points": 10000},
    "Undyne": {"Hp": 130, "Atk": 22, "Def": 8,"Gold": 2500,"Skill Points": 7500},
    "Sans": {"Hp": 120, "Atk": 21, "Def": 7,"Gold": 2000,"Skill Points": 5500}
}

Places = ["Ruins", "" "Waterfall", "End"]

Php = player["Hp"]
Patk = player["Atk"]
Pdef = player["Def"]
stage = 0
max_kills = 4
while True:
    UI()
    choice = input("Select your action: ")

    while True:
        if choice == "1":
            print("\nYou are now playing the game")
            Pn = input("Please enter Player name: ").capitalize()
            print(f"\nWelcome To The Game, {Pn}!")
            player.update({"Name": Pn})

            UI2()
            act = input("Shall we start the Adventure? [1/2]: ")
            if act == "1":
                Class()
                class_choice = input("What do you prefer? [1/2/3]: ")

                while True:
                
                    if class_choice == "1":
                                           
                        player.update({"Class": cl["cl1"]["Class"]})
                        player.update({"Hp": cl["cl1"]["Hp"]})
                        player.update({"Def": cl["cl1"]["Def"]})
                        Pdef = player["Def"]
                        Php = player["Hp"]
                        print("\nPerfect! Now then...")
                        Move()
                        move = input("What should be your next Move? [1/2/3/4]: ")
                        if move == "1":
                            print(f"\nYou've now entered The{Places[stage]}")
                            if stage >= 2:
                                print(f"\n=====BOSS BATTLE=====")

                                Bname, Bstats = spawn_boss(Bosses)
                                Bhp = Bstats["Hp"]
                                Batk = Bstats["Atk"]
                                Bdef = Bstats["Def"]

                                while True:
                                    print(f"\nYou have encountered {Bname}")
                                    Battle()
                                    battle = input("What should be your next Move? [1/2/3/4]: ")

                                    if battle == "1":
                                        Bhp = player_atk_boss(Bhp, Patk)
                                        Php = boss_atk(Php, Batk)

                                        player["Hp"] = Php

                                        if Bhp <= 0:
                                            print(f"\n{Bname} defeated!")

                                            boss_rewards(player, Bstats)

                                            print("\033[32mBoss Fight Cleared!\033[0m")
                                            print("\033[32mTHANK YOU FOR PLAYING!!!\033[0m")
                                            quit()

                                        if Php <= 0:
                                            print("\033[31mYou died!\033[0m")
                                            print("Skill Issue! :p")
                                            quit()

                                    elif battle == "2":
                                        Act()
                                        act_choice = input("What to do? [1/2/3/4]: ")

                                        if act_choice == "1":
                                            print(f"{Bname}:{Bstats}")

                                        elif act_choice == "2":
                                            if player["Skill Points"] >= 100:
                                                dmg = player["Atk"] * 2
                                                print("Power Strike! Massive damage!")
                                                Bhp -= dmg
                                                player["Skill Points"] -= 100
                                                
                                                print(f"You dealt {dmg} damage!")
                                            
                                            else:
                                                print("Not Enough Skill Points!")

                                        elif act_choice == "3":
                                            if player["Skill Points"] >= 50:
                                                print(f"You intimidated {Bname}!")
                                                print(f"{Bname}'s atk Dropped!")
                                                Batk = max(1, int(Batk * 0.9))
                                                player["Skill Points"] -= 50
                                            
                                            else:
                                                print("Not Enough Skill Points!")

                                        elif act_choice == "4":
                                            continue
                                    elif battle == "3":
                                        Item()
                                        item_choice = input("Choose item: ")

                                        if item_choice == "1":
                                            if player["Inventory"]["Potion"] > 0:
                                                player["Hp"] += 10
                                                            
                                                player["Hp"] = min(player["Hp"], 40)
                                                Php = player["Hp"]
                                                player["Inventory"]["Potion"] -= 1
                                        
                                                print("You used a Potion!")
                                                print(f"Your HP is now {player['Hp']}")
                                                print(f"Potions left: {player['Inventory']['Potion']}")

                                            else:
                                                print("No Potions left!")

                                        elif item_choice == "2" or item_choice == "3":

                                                if "True Knife (+Atk)" in player["Inventory"]:
                                                    use_item1(player, "True Knife (+Atk)")

                                                elif "Heart Locket (+Def)" in player["Inventory"]:
                                                    use_item2(player, "Heart Locket (+Def)")

                                        elif item_choice == "4":
                                            continue

                                        else:
                                            print("Invalid!")

                                    elif battle == "4":
                                        Spare()
                                        spare_choice = input("What to do? [1/2]: ")
                                        
                                        if spare_choice == "1":
                                            
                                            print("You Ran away!")
                                            print("Your progress won't be saved :p")
                                            break
                                        
                                        elif spare_choice == "2":
                                            continue
                            else:
                                kills = 0

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
                                            print(f"\033[33mMonsters defeated: {kills}/{max_kills}\033[0m")

                                            if kills >= max_kills:
                                                print("\033[32mDungeon Cleared!\033[0m")
                                                stage += 1
                                                max_kills += 2
                                                break
                                            
                                            Mname, Mstats = spawn_monster(monsters)
                                            Mhp = Mstats["Hp"]
                                            Matk = Mstats["Atk"]
                                            continue

                                        if Php <= 0:
                                            print("\033[31mYou died!\033[0m")
                                            print("Skill Issue! :p")
                                            quit()

                                    elif battle == "2":
                                        Act()
                                        act_choice = input("What to do? [1/2/3/4]: ")

                                        if act_choice == "1":
                                            print(f"{Mname}:{Mstats}")

                                        elif act_choice == "2":
                                            if player["Skill Points"] >= 100:
                                                dmg = player["Atk"] * 2
                                                print("Power Strike! Massive damage!")
                                                Mhp -= dmg
                                                player["Skill Points"] -= 100
                                                
                                                print(f"You dealt {dmg} damage!")
                                            
                                            else:
                                                print("Not Enough Skill Points!")

                                        elif act_choice == "3":
                                            if player["Skill Points"] >= 50:
                                                print(f"You intimidated {Bname}!")
                                                print(f"{Bname}'s atk Dropped!")
                                                Batk = max(1, int(Batk * 0.9))
                                                player["Skill Points"] -= 50
                                            
                                            else:
                                                print("Not Enough Skill Points!")

                                        elif act_choice == "4":
                                            continue
                                    elif battle == "3":
                                        Item()
                                        item_choice = input("Choose item: ")

                                        if item_choice == "1":
                                            if player["Inventory"]["Potion"] > 0:
                                                player["Hp"] += 10
                                                            
                                                player["Hp"] = min(player["Hp"], 40)
                                                Php = player["Hp"]
                                                player["Inventory"]["Potion"] -= 1
                                        
                                                print("You used a Potion!")
                                                print(f"Your HP is now {player['Hp']}")
                                                print(f"Potions left: {player['Inventory']['Potion']}")

                                            else:
                                                print("No Potions left!")

                                        elif item_choice == "2" or item_choice == "3":

                                                if "True Knife (+Atk)" in player["Inventory"]:
                                                    use_item1(player, "True Knife (+Atk)")

                                                elif "Heart Locket (+Def)" in player["Inventory"]:
                                                    use_item2(player, "Heart Locket (+Def)")

                                        elif item_choice == "4":
                                            continue

                                        else:
                                            print("Invalid!")
                                            

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
                            ShopUI()
                            decision = input("Choose! [1/2]: ")
                            if decision == "1":
                                buy_item(player, shop)

                            elif decision == "2":
                                print("Come Again! ^^")
                                continue
                            else:
                                print("Invalid!")

                        elif move == "4":
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

                            elif item_choice == "2" or item_choice == "3":

                                    if "True Knife (+Atk)" in player["Inventory"]:
                                        use_item1(player, "True Knife (+Atk)")

                                    elif "Heart Locket (+Def)" in player["Inventory"]:
                                        use_item2(player, "Heart Locket (+Def)")


                            elif item_choice == "4":
                                continue

                            else:
                                print("Invalid!")



                    elif class_choice == "2":
                        player.update({"Class": cl["cl2"]["Class"]})
                        player.update({"Hp": cl["cl2"]["Hp"]})
                        player.update({"Atk": cl["cl2"]["Atk"]})
                        Patk = player["Atk"]
                        Php = player["Hp"]
                        print("\nPerfect! Now then...")
                        Move()
                        move = input("What should be your next Move? [1/2/3/4]: ")
                        if move == "1":
                            print(f"\nYou've now entered Dungeon {Places[stage]}")
                            if stage >= 2:
                                print(f"\n=====BOSS BATTLE=====")

                                Bname, Bstats = spawn_boss(Bosses)
                                Bhp = Bstats["Hp"]
                                Batk = Bstats["Atk"]
                                Bdef = Bstats["Def"]

                                while True:
                                    print(f"\nYou have encountered {Bname}")
                                    Battle()
                                    battle = input("What should be your next Move? [1/2/3/4]: ")

                                    if battle == "1":
                                        Bhp = player_atk_boss(Bhp, Patk)
                                        Php = boss_atk(Php, Batk)

                                        player["Hp"] = Php

                                        if Bhp <= 0:
                                            print(f"\n{Bname} defeated!")

                                            boss_rewards(player, Bstats)

                                            print("\033[32mBoss Fight Cleared!\033[0m")
                                            print("\033[32mTHANK YOU FOR PLAYING!!!\033[0m")
                                            quit()

                                        if Php <= 0:
                                            print("\033[31mYou died!\033[0m")
                                            print("Skill Issue! :p")
                                            quit()

                                    elif battle == "2":
                                        Act()
                                        act_choice = input("What to do? [1/2/3/4]: ")

                                        if act_choice == "1":
                                            print(f"{Bname}:{Bstats}")

                                        elif act_choice == "2":
                                            if player["Skill Points"] >= 100:
                                                dmg = player["Atk"] * 2
                                                print("Power Strike! Massive damage!")
                                                Bhp -= dmg
                                                player["Skill Points"] -= 100
                                                
                                                print(f"You dealt {dmg} damage!")
                                            
                                            else:
                                                print("Not Enough Skill Points!")

                                        elif act_choice == "3":
                                            if player["Skill Points"] >= 50:
                                                print(f"You intimidated {Bname}!")
                                                print(f"{Bname}'s atk Dropped!")
                                                Batk = max(1, int(Batk * 0.9))
                                                player["Skill Points"] -= 50
                                            
                                            else:
                                                print("Not Enough Skill Points!")

                                        elif act_choice == "4":
                                            continue
                                    elif battle == "3":
                                        Item()
                                        item_choice = input("Choose item: ")

                                        if item_choice == "1":
                                            if player["Inventory"]["Potion"] > 0:
                                                player["Hp"] += 10
                                                            
                                                player["Hp"] = min(player["Hp"], 30)
                                                Php = player["Hp"]
                                                player["Inventory"]["Potion"] -= 1
                                        
                                                print("You used a Potion!")
                                                print(f"Your HP is now {player['Hp']}")
                                                print(f"Potions left: {player['Inventory']['Potion']}")

                                            else:
                                                print("No Potions left!")

                                        elif item_choice == "2" or item_choice == "3":

                                                if "True Knife (+Atk)" in player["Inventory"]:
                                                    use_item1(player, "True Knife (+Atk)")

                                                elif "Heart Locket (+Def)" in player["Inventory"]:
                                                    use_item2(player, "Heart Locket (+Def)")

                                        elif item_choice == "4":
                                            continue

                                        else:
                                            print("Invalid!")

                                    elif battle == "4":
                                        Spare()
                                        spare_choice = input("What to do? [1/2]: ")
                                        
                                        if spare_choice == "1":
                                            
                                            print("You Ran away!")
                                            print("Your progress won't be saved :p")
                                            break
                                        
                                        elif spare_choice == "2":
                                            continue
                            else:
                                kills = 0

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
                                            print(f"\033[33mMonsters defeated: {kills}/{max_kills}\033[0m")

                                            if kills >= max_kills:
                                                print("\033[32mDungeon Cleared!\033[0m")
                                                stage += 1
                                                max_kills += 2
                                                break
                                            
                                            Mname, Mstats = spawn_monster(monsters)
                                            Mhp = Mstats["Hp"]
                                            Matk = Mstats["Atk"]
                                            continue

                                        if Php <= 0:
                                            print("\033[31mYou died!\033[0m")
                                            print("Skill Issue! :p")
                                            quit()

                                    elif battle == "2":
                                        Act()
                                        act_choice = input("What to do? [1/2/3/4]: ")

                                        if act_choice == "1":
                                            print(f"{Mname}:{Mstats}")

                                        elif act_choice == "2":
                                            if player["Skill Points"] >= 100:
                                                dmg = player["Atk"] + 100
                                                print("Execution!")
                                                Mhp -= dmg
                                                print(f"You dealt {dmg} damage!")
                                                player["Skill Points"] -= 100

                                            else:
                                                print("Not Enough Skill Points!")

                                        elif act_choice == "3":
                                            if player["Skill Points"] >= 50:
                                                print(f"You intimidated {Bname}!")
                                                print(f"{Bname}'s atk Dropped!")
                                                Batk = max(1, int(Batk * 0.9))
                                                player["Skill Points"] -= 50
                                            
                                            else:
                                                print("Not Enough Skill Points!")

                                        elif act_choice == "4":
                                            continue
                                    elif battle == "3":
                                        Item()
                                        item_choice = input("Choose item: ")

                                        if item_choice == "1":
                                            if player["Inventory"]["Potion"] > 0:
                                                player["Hp"] += 10
                                                            
                                                player["Hp"] = min(player["Hp"], 30)
                                                Php = player["Hp"]
                                                player["Inventory"]["Potion"] -= 1
                                        
                                                print("You used a Potion!")
                                                print(f"Your HP is now {player['Hp']}")
                                                print(f"Potions left: {player['Inventory']['Potion']}")

                                            else:
                                                print("No Potions left!")

                                        elif item_choice == "2" or item_choice == "3":

                                                if "True Knife (+Atk)" in player["Inventory"]:
                                                    use_item1(player, "True Knife (+Atk)")

                                                elif "Heart Locket (+Def)" in player["Inventory"]:
                                                    use_item2(player, "Heart Locket (+Def)")

                                        elif item_choice == "4":
                                            continue

                                        else:
                                            print("Invalid!")

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
                            ShopUI()
                            decision = input("Choose! [1/2]: ")
                            if decision == "1":
                                buy_item(player, shop)

                            elif decision == "2":
                                print("Come Again! ^^")
                                continue
                            else:
                                print("Invalid!")

                        elif move == "4":
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

                            elif item_choice == "2" or item_choice == "3":

                                    if "True Knife (+Atk)" in player["Inventory"]:
                                        use_item1(player, "True Knife (+Atk)")

                                    elif "Heart Locket (+Def)" in player["Inventory"]:
                                        use_item2(player, "Heart Locket (+Def)")
                            
                            elif item_choice == "4":
                                continue

                            else:
                                print("Invalid!")

                    elif class_choice == "3":
                        player.update({"Class": cl["cl3"]["Class"]})
                        player.update({"Hp": cl["cl3"]["Hp"]})
                        player.update({"Def": cl["cl3"]["Def"]})
                        Patk = player["Atk"]
                        Pdef = player["Def"]
                        Php = player["Hp"]
                        player["Inventory"]["Potion"] = 7
                        print("\nPerfect! Now then...")
                        Move()
                        move = input("What should be your next Move? [1/2/3/4]: ")
                        if move == "1":
                            print(f"\nYou've now entered Dungeon {Places[stage]}")
                            if stage >= 2:
                                print(f"\n=====BOSS BATTLE=====")

                                Bname, Bstats = spawn_boss(Bosses)
                                Bhp = Bstats["Hp"]
                                Batk = Bstats["Atk"]
                                Bdef = Bstats["Def"]

                                while True:
                                    print(f"\nYou have encountered {Bname}")
                                    Battle()
                                    battle = input("What should be your next Move? [1/2/3/4]: ")

                                    if battle == "1":
                                        Bhp = player_atk_boss(Bhp, Patk)
                                        Php = boss_atk(Php, Batk)

                                        player["Hp"] = Php

                                        if Bhp <= 0:
                                            print(f"\n{Bname} defeated!")

                                            boss_rewards(player, Bstats)

                                            print("\033[32mBoss Fight Cleared!\033[0m")
                                            print("\033[32mTHANK YOU FOR PLAYING!!!\033[0m")
                                            quit()

                                        if Php <= 0:
                                            print("\033[31mYou died!\033[0m")
                                            print("Skill Issue! :p")
                                            quit()

                                    elif battle == "2":
                                        Act()
                                        act_choice = input("What to do? [1/2/3/4]: ")

                                        if act_choice == "1":
                                            print(f"{Bname}:{Bstats}")

                                        elif act_choice == "2":
                                            if player["Skill Points"] >= 100:
                                                dmg = player["Atk"] * 2
                                                print("Power Strike! Massive damage!")
                                                Bhp -= dmg
                                                player["Skill Points"] -= 100
                                                
                                                print(f"You dealt {dmg} damage!")
                                            
                                            else:
                                                print("Not Enough Skill Points!")

                                        elif act_choice == "3":
                                            if player["Skill Points"] >= 50:
                                                print(f"You intimidated {Bname}!")
                                                print(f"{Bname}'s atk Dropped!")
                                                Batk = max(1, int(Batk * 0.9))
                                                player["Skill Points"] -= 50
                                            
                                            else:
                                                print("Not Enough Skill Points!")

                                        elif act_choice == "4":
                                            continue
                                    elif battle == "3":
                                        Item()
                                        item_choice = input("Choose item: ")

                                        if item_choice == "1":
                                            if player["Inventory"]["Potion"] > 0:
                                                player["Hp"] += 10
                                                            
                                                player["Hp"] = min(player["Hp"], 70)
                                                Php = player["Hp"]
                                                player["Inventory"]["Potion"] -= 1
                                        
                                                print("You used a Potion!")
                                                print(f"Your HP is now {player['Hp']}")
                                                print(f"Potions left: {player['Inventory']['Potion']}")

                                            else:
                                                print("No Potions left!")

                                        elif item_choice == "2" or item_choice == "3":

                                                if "True Knife (+Atk)" in player["Inventory"]:
                                                    use_item1(player, "True Knife (+Atk)")

                                                elif "Heart Locket (+Def)" in player["Inventory"]:
                                                    use_item2(player, "Heart Locket (+Def)")

                                        elif item_choice == "4":
                                            continue

                                        else:
                                            print("Invalid!")

                                    elif battle == "4":
                                        Spare()
                                        spare_choice = input("What to do? [1/2]: ")
                                        
                                        if spare_choice == "1":
                                            
                                            print("You Ran away!")
                                            print("Your progress won't be saved :p")
                                            break
                                        
                                        elif spare_choice == "2":
                                            continue
                            else:
                                kills = 0

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
                                            print(f"\033[33mMonsters defeated: {kills}/{max_kills}\033[0m")

                                            if kills >= max_kills:
                                                print("\033[32mDungeon Cleared!\033[0m")
                                                stage += 1
                                                max_kills += 2
                                                break
                                            
                                            Mname, Mstats = spawn_monster(monsters)
                                            Mhp = Mstats["Hp"]
                                            Matk = Mstats["Atk"]
                                            continue

                                        if Php <= 0:
                                            print("\033[31mYou died!\033[0m")
                                            print("Skill Issue! :p")
                                            quit()

                                    elif battle == "2":
                                        Act()
                                        act_choice = input("What to do? [1/2/3/4]: ")

                                        if act_choice == "1":
                                            print(f"{Mname}:{Mstats}")

                                        elif act_choice == "2":
                                            if player["Skill Points"] >= 100:
                                                heal = player["Hp"] * random.choice([1, 2, 3])
                                                print("Flawless Heal!")
                                                player["Hp"] = heal
                                                Php = heal
                                                player["Skill Points"] -= 100
                                                print(f"Your HP is now {player['Hp']}")
                                            else:
                                                print("Not Enough Skill Points!")

                                        elif act_choice == "3":
                                            if player["Skill Points"] >= 50:
                                                print(f"You intimidated {Bname}!")
                                                print(f"{Bname}'s atk Dropped!")
                                                Batk = max(1, int(Batk * 0.9))
                                                player["Skill Points"] -= 50
                                            
                                            else:
                                                print("Not Enough Skill Points!")

                                        elif act_choice == "4":
                                            continue
                                    elif battle == "3":
                                        Item()
                                        item_choice = input("Choose item: ")

                                        if item_choice == "1":
                                            if player["Inventory"]["Potion"] > 0:
                                                player["Hp"] += 10
                                                            
                                                player["Hp"] = min(player["Hp"], 70)
                                                Php = player["Hp"]
                                                player["Inventory"]["Potion"] -= 1
                                        
                                                print("You used a Potion!")
                                                print(f"Your HP is now {player['Hp']}")
                                                print(f"Potions left: {player['Inventory']['Potion']}")

                                            else:
                                                print("No Potions left!")

                                        elif item_choice == "2" or item_choice == "3":

                                                if "True Knife (+Atk)" in player["Inventory"]:
                                                    use_item1(player, "True Knife (+Atk)")

                                                elif "Heart Locket (+Def)" in player["Inventory"]:
                                                    use_item2(player, "Heart Locket (+Def)")

                                        elif item_choice == "4":
                                            continue

                                        else:
                                            print("Invalid!")

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
                            ShopUI()
                            decision = input("Choose! [1/2]: ")
                            if decision == "1":
                                buy_item(player, shop)

                            elif decision == "2":
                                print("Come Again! ^^")
                                continue
                            else:
                                print("Invalid!")

                        elif move == "4":
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

                            elif item_choice == "2" or item_choice == "3":

                                    if "True Knife (+Atk)" in player["Inventory"]:
                                        use_item1(player, "True Knife (+Atk)")

                                    elif "Heart Locket (+Def)" in player["Inventory"]:
                                        use_item2(player, "Heart Locket (+Def)")

                            elif item_choice == "4":
                                continue

                            else:
                                print("Invalid!")
                                
                    else:
                        
                        print("Invalid!")
                        break

            elif act == "2":

                print("You've quit the game")
                quit()

            else:

                print("Invalid!")

        elif choice == "2":

            print("You've quit the game")
            quit()

        else:

            print("Invalid!")
            break
