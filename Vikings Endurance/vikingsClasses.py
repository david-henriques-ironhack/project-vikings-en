import random

# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength 
    
    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.health -= damage
    

# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name = name

    def battleCry(self):
        return "Odin Owns You All!"

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else: 
            return f"{self.name} has died in act of combat"


# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return f"A Saxon has died in combat"
        

# war

class War():
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, viking):
        self.vikingArmy.append(viking)
    
    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)
    
    def vikingAttack(self):
        if len(self.saxonArmy) > 0 and len(self.vikingArmy) > 0:
            chosen_saxon = random.choice(self.saxonArmy)
            chosen_viking = random.choice(self.vikingArmy)
            output_message = chosen_saxon.receiveDamage(chosen_viking.attack())
            if chosen_saxon.health <= 0:
                self.saxonArmy.remove(chosen_saxon)
            return output_message
        elif len(self.vikingArmy) == 0:
            return "All Vikings have died in combat"

    
    def saxonAttack(self):
        if len(self.saxonArmy) > 0 and len(self.vikingArmy) > 0:
            chosen_saxon = random.choice(self.saxonArmy)
            chosen_viking = random.choice(self.vikingArmy)
            output_message = chosen_viking.receiveDamage(chosen_saxon.attack())
            if chosen_viking.health <= 0:
                self.vikingArmy.remove(chosen_viking)
            return output_message
        elif len(self.saxonArmy) == 0:
            return "All Saxons have died in combat"
        
    
    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won this battle!"
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."
    pass