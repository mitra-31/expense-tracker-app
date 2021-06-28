
import eel
import datetime
import jsonupdate as ju
import sizes as s
import constants as c
import io
from base64 import b64encode
from PIL import Image 

eel.init("web")  
  
# Exposing the random_python function to javascript
@eel.expose    
def add_amount(amt,desc):
    file = open("web/tracker.json",'r+')
    len_file = len(file.readlines())
    ju.getdata(amt,desc)
    return "Success"
        
    
import matplotlib.pyplot as plt



@eel.expose
def create():
# Data to plot
    labels,sizes,total_amt,from_date,to_date = s.size()
    from_date = "-".join([str(from_date[0]),c.month[from_date[1]-1],str(from_date[2])])
    to_date = "-".join([str(to_date[0]),c.month[to_date[1]-1],str(to_date[2])])
    colors = ['blue',  'green', 'red']
    explode = (0, 0, 0)  # explode 1st slice

    # Plot
    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
    autopct='%1.1f%%', shadow=True, startangle=140)

    plt.axis('equal')
    buffers = io.BytesIO()
    plt.savefig("web/img/pc.png")
    image = Image.open("web/img/pc.png")
    image = image.convert("RGB")
    image.save(buffers,format = "png")
    img_str = b64encode(buffers.getvalue())
    img_src = f"data:image/png;base64, {str(img_str)[2:-1]}"
    return img_src,total_amt,from_date,to_date



eel.start("index.html")