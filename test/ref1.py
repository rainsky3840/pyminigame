import random

overwatch_skins = [
    'Legendary: Oni Genji',
    'Epic: Frostbite Pharah',
    'Rare: Banana Winston',
    'Rare: Cobalt Reinhardt',
    'Epic: Synaesthesia Lucio',
    'Legendary: Lone Wolf Hanzo',
    'Rare: Rose Widowmaker',
    'Rare: Celestial Mercy',
    'Epic: Carbon Fiber D.VA',
    'Legendary: Dr. Junkenstein Junkrat',
    'Epic: Nihon Genji',
    'Rare: Blood Reaper',
    'Rare: Ebony McCree',
    'Epic: Demon Hanzo',
    'Rare: Peridot Ana',
    'Rare: Lemonlime D.VA',
    'Epic: Taegeukgi D.VA',
    'Legendary: Mei-rry Mei',
    'Legendary: Augmented Sombra',
    'Rare: Technomancer Symmetra',
    'Rare: Mud Roadhog'
]

frequency = {
    'Legendary': 2,
    'Rare': 1,
    'Epic': 4
}
# type is to the left of the first colon
types = [skin.split(':')[0] for skin in overwatch_skins]
# map types onto weightings
weightings = [frequency[type] for type in types]

print("Welcome to the Overwatch Loot Box Simulator!")
print(random.choices(overwatch_skins, weightings, k=4))