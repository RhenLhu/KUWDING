import random
#User interface where user can choose to play or exit the game
def UI():
    print(f"\033[33m=====Welcome to TaleUnder=====")
    print("[1] Play")
    print("[2] Exit\033[0m")

#Intro/Purpose of user
def UI2():
    print("\n\033[33mThis game is simple!\033[0m")
    print("Kill The enemies before they kill you")
    print("Because in this world, it's")
    print("\033[31mKill or Be Killed!")
    print("When your HP drops to 0, You will lose!!\033[0m")
    print("Anyways...")
    print("[1] Start")
    print("[2] Back Out (Exit)")

#After start user will choose a role
def Class():
    print("\nPlease Pick a Class:")
    print("[1] Fighter")
    print("[2] Assassin")
    print("[3] Healer")

#If user chose "go to shop" as a move
def ShopUI():
    print("\nWelcome to the Shop!!")
    print("How Can I Help You?")
    print("[1] Buy")
    print("[2] Exit")

#Shop interface after user chose buy
def show_shop(shop):
    i = 1
    print("\n=== SHOP ===")

#Shows item and the price. After item was bought program will direct to shop items and the prices again
    for item, info in shop.items():
        print(f"[{i}] {item} - {info['Price']} Gold")
        i += 1
        continue
    print(f"[{i}] Exit")


def buy_item(player, shop):

    while True:

        show_shop(shop)
#Showing current gold
        print(f"Current Gold: {player["Gold"]}")

        choice = input("What do you want to buy?: ")
#ITEM CHOICES IN SHOP
        if choice == "1":

            item_name = "Potion"
            price = shop[item_name]["Price"]
#Condition either the gold is enough for the item or not
            if player["Gold"] >= price:

                player["Gold"] -= price
                player["Inventory"]["Potion"] += 1

                print(f"You bought {item_name}!")

            else:
                print("Not enough Gold!")

        elif choice == "2":

            item_name = "True Knife (+Atk)"
            price = shop[item_name]["Price"]
#Condition either the gold is enough for the item or not
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
#Condition either the gold is enough for the item or not
            if player["Gold"] >= price:

                player["Gold"] -= price

                if item_name in player["Inventory"]:
                    print("You already own this item!")
                else:
                    player["Inventory"][item_name] = 1

                print(f"You bought {item_name}!")

            else:
                print("Not enough Gold!")
#Exit shop
        elif choice == "4":
            break

        else:
            print("Invalid choice!")
#After choosing class. Program show interactive choices
def Move():
    print("[1] Enter Dungeon")
    print("[2] Check Stats")
    print("[3] Go to Shop")
    print("[4] Items")

#User's choice of move set while in a battle in dungeon
def Battle():
    print("[1] Fight")
    print("[2] Act")
    print("[3] Item")
    print("[4] Spare")

#Move set [2] shows user's choice of act
def Act():
    print("\n=== Act ===")
    print("[1] Check")
    print("[2] Use Special Skill!!")
    print("[3] Intimidate")
    print("[4] Back")

#Move set [3] shows user's current item/s and the amount
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

#True Knife buff in player class if it is used by user
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

#Heart Locket buff in player class if it is used by user
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

#Battle move set in dungeon [2] choice to abandon the battle or fight
def Spare():
    print("\n=== Spare ===")
    print("[1] Run!")
    print("[2] Back\n")

#Monster spawner at basic levels
def spawn_monster(monsters):
    name, stats = random.choice(list(monsters.items()))
    return name, stats

#Boss spawner at boss fight
def spawn_boss(Bosses):
    Bname, Bstats = random.choice(list(Bosses.items()))
    return Bname, Bstats

#Loop Stats
def player_stats(player):
    for x, y in player.items():
        print(f"{x}: {y}")

#After monster defeated will provide rewards
def rewards(player, Mstats):

    gold = Mstats["Gold"]
    Skill_points = Mstats["Skill Points"]

    player["Gold"] += gold
    player["Skill Points"] += Skill_points

    print(f"You gained {gold} Gold!")
    print(f"You gained {Skill_points} Skill Points!\n")

#After boss defeated will provide rewards
def boss_rewards(player, Bstats):

    gold = Bstats["Gold"]
    Skill_points = Bstats["Skill Points"]

    player["Gold"] += gold
    player["Skill Points"] += Skill_points

    print(f"You gained {gold} Gold!")
    print(f"You gained {Skill_points} Skill Points!\n")

#Player's attack damage to monster. The first move set [1]Fight
def player_atk(Mhp, Patk):
    Pdamage = Patk - Mdef
    Mhp -= Pdamage
    print(f"You attacked {Mname} and inflicted {Pdamage} damage")
    print(f"{Mname} HP is now {Mhp}\n")
    return Mhp

#Monsters attack damage to player based on Player's health and defense
def enemy_atk(Php, Matk):
    damage = random.randint(5, Matk)
    final_damage = damage - Pdef
    itspi = player["Hp"]
    Php -= final_damage
    Php = max(0, min(Php, itspi))
    print(f"The monster dealt {final_damage} damage to you!")
    print(f"Your HP has dropped to {Php}\n")
    return Php

#Player's attack damage to boss
def player_atk_boss(Bhp, Patk):
    Pdamage = Patk - Mdef
    Bhp -= Pdamage
    print(f"You attacked {Bname} and inflicted {Pdamage} damage")
    print(f"{Bname} HP is now {Bhp}\n")
    return Bhp

#Boss attack damage based on Player's health and defense
def boss_atk(Php, Batk):
    damage = random.randint(5, Batk)
    final_damage = damage - Pdef
    itspi = player["Hp"]
    Php -= final_damage
    Php = max(0, min(Php, itspi))
    print(f"The monster dealt {final_damage} damage to you!")
    print(f"Your HP has dropped to {Php}\n")
    return Php

#Player Status
player = {
    "Name": "Pliyer",
    "Class": "class",
    "Hp": 25,
    "Atk": 18,
    "Def": 5,
    "Gold": 50,
    "Skill Points": 0,
    "Inventory" : {
    "Potion": 3
    }
}
#Type of Class and their difference advantages
cl = {
        "cl1": {
        "Class" : "Fighter",
        "Hp" : 40,
        "Def" : 10
    },
        "cl2": {
        "Class" : "Assassin",
        "Hp" : 30,
        "Atk" : 27
    },
        "cl3": {
        "Class" : "Healer",
        "Hp" : 70,
        "Atk" : 14,
        "Def" : 7
        }
}
#Available items and their price inside shop/ UI shop
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
#Types of monsters/ Enemies with their different stats and rewards
monsters = {
    "TiggorF": {"Hp": 35, "Atk": 15, "Def": 5,"Gold": 24,"Skill Points": 16},
    "NusmihW": {"Hp": 25, "Atk": 17, "Def": 2,"Gold": 69,"Skill Points": 12},
    "XooL": {"Hp": 55, "Atk": 16, "Def": 8,"Gold": 42,"Skill Points": 19},
    "PsogiM": {"Hp": 45, "Atk": 16, "Def": 6,"Gold": 24,"Skill Points": 14}
}
#Types of bosses with their different stats and rewards
Bosses = {
    "Toriel": {"Hp": 100, "Atk": 22, "Def": 6,"Gold": 1000,"Skill Points": 1000},
    "Asgore": {"Hp": 160, "Atk": 23, "Def": 12,"Gold": 5000,"Skill Points": 10000},
    "Undyne": {"Hp": 130, "Atk": 22, "Def": 8,"Gold": 2500,"Skill Points": 7500},
    "Sans": {"Hp": 120, "Atk": 21, "Def": 7,"Gold": 2000,"Skill Points": 5500}
}
#Viriable for types of places, player status, current stage, and max skills in a battle
Places = ["Ruins", "Waterfall", "End"]
Php = player["Hp"]
Patk = player["Atk"]
Pdef = player["Def"]
stage = 0
max_kills = 5
#First UI
while True:
    UI()
    choice = input("Select your action: ")
#If [1]Play is chosen by the player it will continue and ask for player name
    while True:
        if choice == "1":
            print("\nYou are now playing the game")
            Pn = input("Please enter Player name: ").capitalize()
            print(f"\nWelcome To The Game, {Pn}!")
            player.update({"Name": Pn})
#Progam calls the UI2/Intro as game ask if player wants continue, and if player press [1] Start. The game will continue true
            UI2()
            act = input("Shall we start the Adventure? [1/2]: ")
            if act == "1":
#User/Player class choices
                Class()
                class_choice = input("What do you prefer? [1/2/3]: ")

                while True:
#1st Class(Fighter)
                    if class_choice == "1":
                                           
                        player.update({"Class": cl["cl1"]["Class"]})
                        player.update({"Hp": cl["cl1"]["Hp"]})
                        player.update({"Def": cl["cl1"]["Def"]})
                        Pdef = player["Def"]
                        Php = player["Hp"]
                        print("\nPerfect! Now then...")
#After choosing class, Game proceeds to interactive move set
                        Move()
                        move = input("What should be your next Move? [1/2/3/4]: ")
#If user selected to [1]Enter Dungeon user will proceed to battle
                        if move == "1":
                            print(f"\nYou've now entered the {Places[stage]}")
#If 2 stages are cleared and player entered dungeon again surely there will be boss battle
                            if stage >= 2:
                                print(f"\n=====BOSS BATTLE=====")
#Game will spawn a random boss from the Bosses with their stats
                                Bname, Bstats = spawn_boss(Bosses)
                                Bhp = Bstats["Hp"]
                                Batk = Bstats["Atk"]
                                Bdef = Bstats["Def"]
#After program/game chose the boss, the game lets the user know who/what is the boss
                                while True:
                                    print(f"\nYou have encountered {Bname}")
#This is the move set of the player
                                    Battle()
                                    battle = input("What should be your next Move? [1/2/3/4]: ")
#If player chose [1] fight the program it self process the damages from the player and the monthers health/defense
                                    if battle == "1":
                                        Bhp = player_atk_boss(Bhp, Patk)
                                        Php = boss_atk(Php, Batk)

                                        player["Hp"] = Php
#If player defeated boss game will announce "Boss is defeated" and it will automatically end
                                        if Bhp <= 0:
                                            print(f"\n{Bname} is defeated!")

                                            boss_rewards(player, Bstats)

                                            print("\033[32mBoss Fight Cleared!\033[0m")
                                            print("\033[32mTHANK YOU FOR PLAYING!!!\033[0m")
                                            quit()
#If player did not defeated monster/boss game will automatically end with defeated announcement
                                        if Php <= 0:
                                            print("\033[31mYou died!\033[0m")
                                            print("Skill Issue! :p")
                                            quit()
#2nd Move set or [2]Act shows the monster/boss stats and player special skills
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
#The 3rd move set or [3]Item this shows current player items
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
#4th battle or [4]Spare gives the player a choice whether to run or continue the fight 
                                    elif battle == "4":
                                        Spare()
                                        spare_choice = input("What to do? [1/2]: ")
                                        
                                        if spare_choice == "1":
                                            
                                            print("You Ran away!")
                                            print("Your progress won't be saved :p")
                                            break
                                        
                                        elif spare_choice == "2":
                                            continue
#Same actions but diffent enemies
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
#Enemy counter works until it reach the max kills that is setted by in game or the program 
                                            kills += 1
                                            print(f"\033[33mMonsters defeated: {kills}/{max_kills}\033[0m")

                                            if kills >= max_kills:
                                                print("\033[32mDungeon Cleared!\033[0m")
                                                stage += 1
                                                max_kills += 2
                                                break
#Monster Spawner
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
#Fighter's special skill
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
                                                print(f"You intimidated {Mname}!")
                                                print(f"{Mname}'s atk Dropped!")
                                                Matk = max(1, int(Matk * 0.9))
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
#2nd Class(Assassin)
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
#Assassin's special skill
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
                                                print(f"You intimidated {Mname}!")
                                                print(f"{Mname}'s atk Dropped!")
                                                Matk = max(1, int(Matk * 0.9))
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
#3rd Class choice(Healer)
                    elif class_choice == "3":
                        player.update({"Class": cl["cl3"]["Class"]})
                        player.update({"Hp": cl["cl3"]["Hp"]})
                        player.update({"Atk": cl["cl3"]["Atk"]})
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
#Healer special skill
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
                                                print(f"You intimidated {Mname}!")
                                                print(f"{Mname}'s atk Dropped!")
                                                Matk = max(1, int(Matk * 0.9))
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