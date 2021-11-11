import os
import matplotlib.pyplot as plt




class Figure:

    def __init__(self, name, path, xAxis, yAxis):

        self.name = name
        self.path = path 
        self.xAxis = []
        self.yAxis = []
        self.is_shape_drawn = False
        self.plot = _plot


    def draw(self, show=False):
        
        self.plot = plt.plot(self.xAxis, self.yAxis)
        if show:
            plt.show()
        else:
            self.is_shape_drawn = True
            return True

    def save(self):

        if is_shape_drawn:
            plt.savefig(self.path + self.name)
            print(f"Shape is saved at {self.path + self.name}")



def extract_time_stamps(file_name):
   
    # a function that opens a time-stamps.txt file and
    # extracts the time stamp on each line. returns a list.


    time_stamps = []
    with open(file_name, "r") as fname:

        lines = fname.readlines()
        for i in lines:
            time_stamps.append(i.replace(",","")) 

    print(f"time stamp extraction from {file_name} is done!")

    return time_stamps


if __name__ == "main":


    file_path = "time-stamps/output-1-time-stamps.txt"
    should_be_timestamp_list = extract_time_stamps(file_path)
    print(should_be_timestamp_list)
    
    
    
    
    
    
    
    
    
#     time_stamps = [4022.581,
#               1310.080,
#               1204.420,
#               1125.262,
#               1176.953,
#               1189.106,
#               1235.579,
#               1244.626,
#               1254.866,
#               1275.706,
#               1275.318,
#               1366.927,
#               1369.309,
#               1395.356,
#               1441.244,
#               1368.633,
#               1470.346,
#               1426.924,
#               1459.647,
#               1411.237,
#               1543.816,
#               1524.576,
#               1500.342,
#               1585.979,
#               1480.017,
#               1454.645,
#               1502.504,
#               1611.809,
#               1547.827,
#               1514.831,
#               1539.416,
#               1564.095]

# indexes = [1, 4]

# for i in range(len(time_stamps) - 2):
#   indexes.append(indexes[-1] + 2)
  
# speed_up = [((i/time_stamps[0])+1) for i in time_stamps]
# speed_up[0]-=1
# # print(indexes)

## just switch speed_up variable with time_stamps and you'll get the graph of time (in ms) X workers (p)

# fg = plt.plot(indexes,speed_up,marker='o', linestyle='-',linewidth=3.5, color='r', 
# label='Square')
# plt.xlabel('p- workers')
# plt.ylabel('speed up') 
# plt.title('Vacation2 benchmark original version')
# plt.legend() 
# plt.show()

