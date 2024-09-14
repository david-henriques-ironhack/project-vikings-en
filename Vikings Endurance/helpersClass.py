

class Helper:
    def __init__(self, name, health_boost, min_strength, max_strength):
        self.name = name
        self.health_boost = health_boost
        self.min_strength = min_strength
        self.max_strength = max_strength

                
        
#Vikings        
villagers = Helper(
    name="villagers",
    health_boost=100,
    min_strength=150,
    max_strength=200,
)


berserkers = Helper(
    name="berserkers",
    health_boost=10000,
    min_strength=124567,
    max_strength=200000,
)

priest_bless = Helper(
    name="priest bless",
    health_boost=0,
    min_strength=0,
    max_strength=0,
)

