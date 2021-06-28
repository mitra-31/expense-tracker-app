import constants as c
import json


def size(filename='web/tracker.json'):
    with open(filename,"r+") as file:
        new_dict = {
            "bills":0,
            "food":0,
            "other":0
        }
        lst_labels = [[],[],[]]
        dates = []
        file_data = json.load(file)
        for key in file_data.keys():
            desc = file_data[key]["desc"].lower()
            if desc in c.bills:
                new_dict["bills"] += int(file_data[key]["amount"])
                lst_labels[0].append(file_data[key]["desc"])
                dates.append(file_data[key]["date"])
            elif desc in c.food:
                new_dict["food"] += int(file_data[key]["amount"])
                lst_labels[1].append(file_data[key]["desc"])
                dates.append(file_data[key]["date"])
            else:
                new_dict["other"] += int(file_data[key]["amount"])
                lst_labels[2].append(file_data[key]["desc"])
                dates.append(file_data[key]["date"])
    
    sorted_values = sorted(new_dict.items(), key =lambda kv:(kv[1], kv[0]))
    labels = [i[0] for i in sorted_values]
    sizes = [i[1] for i in sorted_values]
    dates = sorted(list(map(date_convert,dates)))
    return labels,sizes,sum(sizes),dates[0],dates[-1]



def date_convert(date):
    date = date.split("-")
    day = int(date[0])
    month = c.month.index(date[1])+1
    year = int(date[2])
    return (day,month,year)