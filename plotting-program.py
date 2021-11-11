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

