import tcod as libtcod
from random import randint 

from components.ai import BasicMonster
from components.equipment import EquipmentSlots
from components.equippable import Equippable
from components.fighter import Fighter
from components.item import Item
from components.stairs import Stairs

from game_messages import Message 

from item_functions import cast_confuse, cast_fireball, cast_lightning, heal

from map_objects.rectangle import Rect
from map_objects.tile import Tile 

from random_utils import from_dungeon_level, random_choice_from_dict

from render_functions import RenderOrder
from entity import Entity


def get_monster_chances(dungeon_level):
    monster_chances = {

    }
    
    
    pass

