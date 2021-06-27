import constants as c
import json


def size(filename='web/tracker.json'):
    with open(filename,"r+") as file:
        new_dict = {
            "bills":0,
            "food":0,
            "other":0
        }
        lst = [[],[],[]]
        file_data = json.load(file)
        for key in file_data.keys():
            desc = file_data[key]["desc"].lower()
            if desc in c.bills:
                new_dict["bills"] += int(file_data[key]["amount"])
                lst[0].append(file_data[key]["desc"])
            elif desc in c.food:
                new_dict["food"] += int(file_data[key]["amount"])
                lst[1].append(file_data[key]["desc"])
            else:
                new_dict["other"] += int(file_data[key]["amount"])
                lst[2].append(file_data[key]["desc"])
    
    sorted_values = sorted(new_dict.items(), key =lambda kv:(kv[1], kv[0]))
    labels = [i[0] for i in sorted_values]
    sizes = [i[1] for i in sorted_values]
    return labels,sizes

size()