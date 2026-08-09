import pandas as  pd  
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns

class function:
    def __init__(self):
        self.input_data = input("Enter the Data Path : =")
        self.df = None

    def load_data(self):

        try:
            self.df = pd.read_csv(self.input_data)
            return self.df
        except Exception as e:
            print(f'Error File load {e}')

    def show_data1 (self):
        self.data_head = input('You see Data Head : = ').lower().strip()
    
        if self.data_head == 'y':
            if self.df is not None:
                print(pd.DataFrame(self.df.head()))
            
            
        self.data_tail = input('you see data Tail = ').lower().strip()
        if self.data_tail == 'y':
            if self.df is not None:
                print(pd.DataFrame(self.df.tail()))


def main():
    func = function()
    func.load_data()
    func.show_data1()

main()
                
         
                
         