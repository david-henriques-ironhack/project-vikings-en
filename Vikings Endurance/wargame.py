
from vikingsClasses import Soldier, Viking, Saxon, War
from helpersClass import Helper, villagers, berserkers, priest_bless
import random
import time


helpers_list = []
enemies_list = []
names = []
intro = True
island = "Eldergrove"


#saxons global
saxon_health = 1
min_sax_att = 1
max_sax_att = 1
saxon_range = 2

#Places variables
eldergrove_island = ["barn", "church", "tavern", "blacksmith", "dock", "hotel", "forest", "donkey", "key"]
inventory_items = []

# Check Global Variables
barn_check = True
spies_check = True
drunk_check = True
armed_check = True
blacksmith_check = True
tree_check = True
church_check = True
tavern_check = True
forest_check = True

# Check Items
axe_check = False
apple_check = False
coins_check = False
wine_check = False
key_check = False







def prompt_names():
    global names
    names = []  # Clear any previous names

    print("Greetings, great warriors! I am Sigrid Flamebearer, the leader of Eldergrove Island. Who are you folks? ")

    # Prompt the user for names
    for i in range(1, 4):
        say_name = input(f"Please choose a name for your Viking {i}: ")
        names.append(say_name)
        intro = False
    print(f"That's very nice to meet you {names[0]}, {names[1]} and {names[2]}!! The Saxons are coming around and they are spying on us. I hope you can give us some help!")
    



def play_game():
    global names, island, enemies_list, saxon_range, barn_check, spies_check, drunk_check, armed_check, blacksmith_check, tree_check, church_check, tavern_check, forest_check, axe_check, apple_check, coins_check, wine_check, key_check

    
    if island == "Eldergrove":
        
        if intro:
            prompt_names()
        else: 
            pass

        while True:
        
            player_action = input(f"""

What would you like to do? 
- Say 'places' to see what's in the {island}, 
- Say 'fight' to fight against Saxons,
- Say 'army' to see how many units you have,
- Say 'inventory' to check your inventory,
- Mention a name of a place to interact)

""").strip().lower()
            if "place" in player_action or "places" in player_action:
                print(f"This island is nice. I can see a {eldergrove_island} from here!")
                
            elif "inventory" in player_action:
                if len(inventory_items) > 0:
                    print(f'You have these items: {inventory_items}')
                else:
                    print("You checked everything. You have nothing!")
                    
                       
            elif "army" in player_action:
                print(f'You still have {len(names)} soldiers')  
                
                
            elif "barn" in player_action:
                if barn_check:
                    if axe_check:
                        print("Nice, the villagers are now equipped and joined your army.")
                        helpers_list.append("villagers")
                        names.extend(["Elgin the Villager", "Ciro the Villager", "Mark the Villager", "Ogar the Villager", "Odor the Villager"])
                        print(f"Current helpers: {helpers_list}")
                        barn_check = False
                        axe_check = False
                        inventory_items.remove("axe") 
                    else:
                        print("Villagers say: We'd love to help you, but unfortunatelly we have no weapons!")                   
                else: 
                    print("There's no one else there!")
                    
            elif "blacksmith" in player_action or "black" in player_action:
                if blacksmith_check: 
                    if coins_check:
                        print("Greg the Blacksmith guy says: Oh nice! You got the right amount of coin for these axes")
                        axe_check = True
                        inventory_items.append("axe")
                        blacksmith_check = False
                        coins_check = False
                        inventory_items.remove("silver coins")
                        print("You got axes into your inventory")
                    else:
                        print("Greg says: I have axes here. But I can't give them for free. Would you have something for me?")
                else:
                    print("Greg says: I only had those axes. I'm going on holidays with the coins you gave me. Goodbye!")
            
            elif "tree" in player_action:
                if tree_check:
                    print("There are ripe apples here. I'd try some")
                    inventory_items.append("apple")
                    tree_check = False
                    apple_check = True
                else:
                    print("I like apples. Maybe I try some more. Why not?")
            
            elif "donkey" in player_action:
                if apple_check:
                    print("Oh! Come here boy!! Wow! The donkey seems very happy with apples")
                else:
                    print("I could do something for this donkey")
                    
            elif "church" in player_action:
                if church_check:
                    if wine_check:
                        print("Priest says: This wine is really good stuff. I will pray for you. God bless your army")
                        helpers_list.append("priest bless")
                        names.extend(["Hagar the Blessed", "Fjoll the Blessed", "Gunner the Blessed", "Orm the Blessed", "Baldur the Blessed"])
                        time.sleep(1)
                        print(f"You got a boost from the priest bless: {helpers_list}")
                        
                        wine_check = False
                        inventory_items.remove("wine")
                        church_check = False
                    else: 
                        print("Priest says: I think I need some incentive to pray! I'm thirsty!")
                else:
                    print("Priest says: I already prayed too much! Hic, ops!")               
                
            elif "tavern" in player_action:
                if tavern_check:
                        print("The party is good here. There's a guy sleeping on the corner. I will steal his booze!")
                        inventory_items.append("wine")
                        time.sleep(1)
                        print("You got some wine in your inventory")
                        wine_check = True
                        tavern_check = False
                else:
                    print("I like parties and booze, but the Saxons are attacking us! We must go!")
            
            
            elif "docks" in player_action or "dock" in player_action:
                print("The saxons are there. I can't access the ship!")
                
                
            elif "forest" in player_action:
                if forest_check:
                    if key_check:
                        print("The Berserkers say: Thanks for releasing us noble gentlemans! We'd love to have some revenge!")
                        helpers_list.append("berserkers")
                        names.extend(["Ragnar the Berserker",
    "Bjorn Ironfist the Berserker",
    "Ulf Bloodaxe the Berserker",
    "Thorgrim the Berserker",
    "Sköll Wolfheart the Berserker",
    "Erik Stormborn the Berserker",
    "Hakon Skullcrusher the Berserker",
    "Styr Thunderclaw the Berserker",
    "Sigurd Firebeard the Berserker",
    "Viggo Ironhide the Berserker",
    "Tormod the Berserker",
    "Kjell Bloodrage the Berserker",
    "Asger Bonebreaker the Berserker"])
                        print(f"Current helpers: {helpers_list}")
                        key_check = False
                        forest_check = False
                    else:
                        print("There's a cage here! The saxons imprisioned all the berserkers of the island!")
                else:
                    print("Ooh! The silence of the forest!")
                    
            elif "hotel" in player_action:
                print("All hotels are closed because of the war!")            
                
                
            elif "fight" in player_action:
                pick_enemy = input("""Against whom do you want to fight? 
The scout could see tree enemies during the night:

- There are 2 spies saxons close to the woods
- There are some drunken saxons that he saw leaving the bar. Them seem a bit tought to beat
- There are armed saxons blocking the docks. We need to be prepared for them, they seem very strong


Type 'spies', 'drunk' or 'armed' to pick your opponent: """)
                
                if "spies" in pick_enemy:
                    if spies_check:
                        enemy_choice("spies")                        
                        print("Prepare for battle.")
                        spies_check = False
                        result = start_battle()
                    else:
                        print("You have already killed the spies. Choose another enemy")  
                elif "drunk" in pick_enemy:
                        if drunk_check:
                            enemy_choice("drunk")
                            saxon_range += 8                        
                            print("Prepare for battle.")
                            drunk_check = False
                            key_check = True
                            result = start_battle()
                            
                        else: 
                            print("You have killed the drunk saxons already. The boose would have killed them, but you arrived earlier. Pick someone else!")
                elif "armed" in pick_enemy:
                        if armed_check:
                            enemy_choice("armed")
                            saxon_range += 8                        
                            print("Prepare for battle.")
                            armed_check = False
                            result = start_battle()
                    
                                   
                if result == "lost":
                    print("You fought bravely, but the war is over. Better luck next time")
                    break  # Exits the game loop if lost
                elif result == "won":
                    if armed_check:
                        if not drunk_check:
                            print("We won and I found some keys with them. It looks like a key for a cage!")
                            inventory_items.append("key")
                            time.sleep(1)
                            print("You got a key into your inventory")
                        else:
                            inventory_items.append("silver coins")
                            coins_check = True     
                            print("Congratulations! You won the battle. You found some silver coins!")
                    else:
                        print("""Congratulations, you have defeated the armed saxons!!


                 ~.
           Ya...___|__..aab     .   .
            Y88a  Y88o  Y88a   (     )
             Y88b  Y88b  Y88b   `.oo'
             :888  :888  :888  ( (`-'
    .---.    d88P  d88P  d88P   `.`.
   / .-._)  d8P''''|''''-Y8P      `.`.
  ( (`._) .-.  .-. |.-.  .-.  .-.   ) )
   \ `---( O )( O )( O )( O )( O )-' /
    `.    `-'  `-'  `-'  `-'  `-'  .' 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                                                                
You can finally run for a new adventure with your Viking ship""")
                        break

        
        
            else:
                print("Invalid choice. I don't understand what you want.")
                time.sleep(1)
        
        
def enemy_choice(enemy):
    global enemies_list
    enemies_list = [] #Clean enemy name list
    enemies_list.append(enemy)

    

def helper_party(helper):
    global viking_health, min_strength, max_strength
    viking_health += helper.health_boost
    min_strength += helper.min_strength
    max_strength += helper.max_strength


    


def start_battle():
        global viking_health, min_strength, max_strength, saxon_range, saxon_health, min_sax_att, max_sax_att, enemies_list
        war = War()
        viking_health = 100  # Base health
        min_strength = 50    # Default min strength
        max_strength = 100   # Default max strength
        

        
  
        




        print( """
          
                Odin Owns You All!
          
            The battle has just begun!!!
                
            
            """)
        time.sleep(1)

        for helper_name in helpers_list:  # Loop through all items in the inventory
                helper = globals().get(helper_name)  # Get the actual item object from its name
        if helper:
            helper_party(helper)
        else:
            viking_health = 100  # Base health
            min_strength = 15    # Default min strength
            max_strength = 100   # Default max strength 

        
        
        if "spies" in enemies_list:
                saxon_health += 100
                min_sax_att += 50
                max_sax_att += 100
        
        if "drunk" in enemies_list:
                saxon_health += 100
                min_sax_att += 50
                max_sax_att += 110
                
        if "armed" in enemies_list:
                saxon_health += 200000
                min_sax_att += 500
                max_sax_att += 10000       
            



        #Create 5 Vikings
        for i in range(len(names)):
                war.addViking(Viking(names[i], viking_health, random.randint(min_strength, max_strength)))

        #Create 5 Saxons
        for _ in range(0,saxon_range):
                war.addSaxon(Saxon(saxon_health,random.randint(min_sax_att,max_sax_att)))
    
        round = 1
        while war.showStatus() == "Vikings and Saxons are still in the thick of battle.":
            print(f"round: {round} // Viking army: {len(war.vikingArmy)} warriors",f"and Saxon army: {len(war.saxonArmy)} warriors")
            max_range = len(war.vikingArmy)
            time.sleep(1)
            viking_attack_message = war.vikingAttack()
            print(viking_attack_message)
            time.sleep(1)
            saxon_attack_message = war.saxonAttack()
            print(saxon_attack_message)
            names_to_remove = []

            for name in names:
                if name in saxon_attack_message:
                    names_to_remove.append(name)
        # Remove names outside the loop to avoid modifying the list during iteration
            for n in names_to_remove:
                if n in names:
                    names.remove(n)
        
        # Print updated names list for debugging
            time.sleep(1)
            print(""" """)
            print(war.showStatus())
            time.sleep(1)
            print(""" """)
            round += 1
        if len(war.vikingArmy) == 0:
            return "lost"
        else:
            return "won"
        time.sleep(1.5)
       

play_game()