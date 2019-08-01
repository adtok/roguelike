import tcod as libtcod

from random import randint

from game_messages import Message 


class BasicMonster:
    def __init__(self, att_range=1):
        self.att_range = att_range 

    def take_turn(self, target, fov_map, game_map, entities):
        results = []

        # print(f"The {self.owner.name} wonders when it will get to move.")
        monster = self.owner
        if libtcod.map_is_in_fov(fov_map, monster.x, monster.y):
            if monster.distance_to(target, manhattan=(self.att_range>1)) >= (1 + self.att_range):
                monster.move_astar(target, entities, game_map)
            
            elif target.fighter.hp > 0:
                attack_results = monster.fighter.attack(target)
                results.extend(attack_results)
        
        return results

# class RangedMonster:
#     def __init__(self, att_range=2):
#         self.att_range = att_range

#     def take_turn(self, target, fov_map, game_map, entities):
#         results = []

#         monster = self.owner
#         if libtcod.map_is_in_fov(fov_map, monster.x, monster.y):
#             if monster.distance_to(target) >= (1 + att_range)

class ConfusedMonster:
    def __init__(self, previous_ai, number_of_turns=10):
        self.previous_ai = previous_ai
        self.number_of_turns = number_of_turns

    def take_turn(self, target, fov_map, game_map, entities):
        results = []

        if self.number_of_turns > 0:
            random_x = self.owner.x + randint(0, 2) - 1
            random_y = self.owner.y + randint(0, 2) - 1

            if random_x != self.owner.x and random_y != self.owner.y:
                self.owner.move_towards(random_x, random_y, game_map, entities)

            self.number_of_turns -= 1
        else:
            self.owner.ai = self.previous_ai
            results.append({'message': Message(f"The {self.owner.name} is no longer confused", libtcod.red)})
        
        return results
            
            