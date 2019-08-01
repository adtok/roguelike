import tcod as libtcod
import json
from random import randint

from components.ai import BasicMonster
from components.fighter import Fighter 
from entity import Entity 

from random_utils import from_dungeon_level #, get_chance_from_table
from render_functions import RenderOrder


import json

color_mappings = {
    'green' : libtcod.green,
    'desaturated_green': libtcod.desaturated_green,
    'red': libtcod.red,
    'yellow': libtcod.yellow,
}

from_table = lambda table: from_dungeon_level(table, dungeon_level)
def from_table(table): return from_dungeon_level(table, 2)

def generate_floor_entities(dungeon_level, filename='floor_data.json'):
    '''Generates ONLY monster chances and creation functions (for now, items to be added)'''

    # Simplify from_dungeon_level function
    from_table = lambda table: from_dungeon_level(table, dungeon_level)
    
    # Load data from json file
    with open(filename, 'r') as fi:
        data = json.load(fi).get('data') # may get rid of the "comment" in the data file later, using to keep things straight
    
    # generate monsters
    max_monsters_per_room = from_table(data.get('max_monsters_per_room'))
    max_items_per_room = from_table(data.get('max_items_per_room'))

    monster_chances = {}
    monster_generator = {}
    for monster in data.get('monsters'):
        chance = from_table(monster.get('chances'))
        if chance and chance > 0:
            name = monster.get('name')
            monster_chances[name] = chance 
            monster_generator[name] = new_monster(monster) # Assign generator function

    return monster_chances, monster_generator


def new_monster(monster_json, colors=color_mappings):
    # return a function to generate a monster from the json
    entity_json = monster_json.get('entity')
    name = monster_json.get('name')

    char = entity_json.get('char')
    color = color_mappings.get(entity_json.get('color'))

    fighter_json = entity_json.get('fighter')
    hp = fighter_json.get('hp')
    defense = fighter_json.get('defense')
    power = fighter_json.get('power')
    xp = fighter_json.get('xp')
    att_range = fighter_json.get('att_range')

    if att_range is None:
        att_range = 1

    def create(x,y):
        ai_component = BasicMonster(att_range=att_range) # TODO - handle other AIs
        fighter_component = Fighter(hp=hp, defense=defense, power=power, xp=xp)
        monster = Entity(x, y, char, color, name, blocks=True, render_order=RenderOrder.ACTOR, 
                         fighter=fighter_component, ai=ai_component)
        return monster
    return create


if __name__ == '__main__':
    with open('floor_data.json', 'r') as fi:
        data = json.load(fi).get('data')

    orc = data.get('monsters')[0]
    funcs = {"orc": new_monster(1,1,orc)}
    orcs = [funcs['orc']() for i in range(3)]
    print(orcs)
