from random import randint 

def from_dungeon_level(table, dungeon_level):
    for (value, level) in reversed(table):
        if dungeon_level >= level:
            return value
    return 0

def random_choice_index(chances):
    random_chance = randint(1, sum(chances))

    running_sum = 0
    choice = 0
    for w in chances:
        running_sum += w 

        if random_chance <= running_sum:
            return choice 
        choice += 1

def random_choice_from_dict(choice_dict):
    choices = list(choice_dict.keys())
    chances = list(choice_dict.values())

    return choices[random_choice_index(chances)]



if __name__ == '__main__':
    monster_chances = {'orc': 80, 'troll': 20}
    counts = {}
    for i in range(10000):
        monster_choice = random_choice_from_dict(monster_chances)
        if counts.get(monster_choice):
            counts[monster_choice] += 1
        else:
            counts[monster_choice] = 1
        
    print(counts)