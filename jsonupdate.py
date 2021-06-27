import eel

 
 
import json
import datetime
 
def date_time():
  return datetime.datetime.now().strftime("%d-%B-%y"),datetime.datetime.now().strftime("%H:%M:%S")
 
def write_json(new_data, filename='web/tracker.json'):
   with open(filename,'r+') as file:
        file_data = json.load(file)
        current = len(file_data)
        #print(current)
        file_data.update({str(current):new_data})
        file.seek(0)
        json.dump(file_data, file, indent = 4) 



def getdata(amt,desc):
      date,time = date_time()
      dict_obj = {}
      dict_obj["amount"] = str(amt)
      dict_obj["desc"] = str(desc)
      dict_obj["date"] = date
      dict_obj["time"] = time
      write_json(dict_obj)
      eel.reload()
