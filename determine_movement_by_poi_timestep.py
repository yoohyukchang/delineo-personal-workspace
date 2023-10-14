# This is the file generating only necessary info about movement patterns about the people.
# This will be given to the simulations team to use for recognizing the movement of the people.
# This is for POIs.

import json

with open('result_poi.json', 'r') as file:
    poi_deque_movement = json.load(file)


for timestep in poi_deque_movement:
    for poi in poi_deque_movement[timestep]:
        new_list = []
        for inner_list in poi_deque_movement[timestep][poi]:
            for inner_most_list in inner_list:
                inner_most_list.pop('cbg', None)
                inner_most_list.pop('infected', None)
                inner_most_list.pop('sex', None)
                inner_most_list['timestep'] = timestep
                inner_most_list['poi_name'] = poi
                new_list.append(inner_most_list)
        poi_deque_movement[timestep][poi] = new_list


with open('movement_patterns_between_pois.json', 'w') as file:
    json.dump(poi_deque_movement, file)

print("movement patterns between POIs result file created.")