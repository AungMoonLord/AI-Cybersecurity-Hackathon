'''generate_data.py'''
import random
import csv

months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
class TimeGenerator():
    '''generate time forward only'''

    def __init__(self):
        '''constructor'''
        self.year = 2025
        self.month = 12
        self.day = 23
        self.hour = 12
        self.minute = 3
        self.second = 32.3
    
    def get_time(self):
        '''return time'''
        self.second += random.random()
        if self.second >= 60:
            self.second -= 60
            self.minute += 1
        if self.minute >= 60:
            self.minute -= 60
            self.hour += 1
        if self.hour >= 24:
            self.hour -= 24
            self.day += 1

        if (self.year % 4 == 0) and (self.year % 400 == 0 or self.year % 100):
            month_day = self.day > months[self.month-1] + self.month
        else:
            month_day = self.day > months[self.month-1]
        
        if self.day > month_day:
            self.day -= month_day
            self.month += 1
        if self.month > 12:
            self.month -= 12
            self.year += 1

        return f"{self.year}-{self.month}-{self.day}T{self.hour}:{self.minute}:{self.second}Z"


class WeightedRandomizer():
    '''
    Docstring for weighted_rand
    
    :return: Description
    :rtype: Any
    '''
    def __init__(self, pairs : list):
        self.total_weight = 0
        self.pairs = []
        for value, weight in pairs:
            self.total_weight += weight
            self.pairs.append((value, self.total_weight))

    def getrand(self):
        rand_val = random.randint(1, self.total_weight)
        for val, cum_weight in self.pairs:
            if cum_weight >= rand_val:
                return val
        return "Error" 

class Data:
    '''
    Docstring for data
    '''
    def __init__(self, form : str, val : list):
        '''constructor'''
        self.str = []
        self.val = val # a list of function that return a value
        temp = ""
        length = len(form)
        i = 0
        while i < length:
            if i < length - 1 and form[i] == "/" and form[i+1] == "$":
                self.str.append(temp)
                temp = ""
                i += 2
                continue
            temp += form[i]
            i += 1
        pass

    def get_data(self):
        '''get data'''
        i = 0
        j = 0
        result = ""
        while i < len(self.str) or j < len(self.val):

            if i < len(self.str):
                result += self.str[i]
                i += 1

            if j < len(self.val):
                result += str(self.val[j]())
                j += 1

        return result

class Column:
    '''
    Docstring for column
    '''
    def __init__(self, name : str, data : list):
        '''constructor'''
        self.name = name
        self.wr = WeightedRandomizer(data)

    def get_header(self):
        '''return the column header name'''
        return self.name

    def generate_data(self):
        '''generate data coresponding to ratio'''
        return self.wr.getrand().get_data()

class DatasetGenerator:
    '''
    Docstring for dataset_generator
    '''
    def __init__(self):
        '''constructor'''
        self.columns = []

    def generate_csv(self, num : int):
        '''generate csv file'''
        with open("dataset", mode="w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([column.get_header() for column in self.columns])
            for _ in range(num):
                writer.writerow([column.generate_data() for column in self.columns])

    def append_column(self, column : Column):
        '''append_column'''
        self.columns.append(column)

def main():
    '''main'''
    # val = [random.random, lambda: random.randint(1,10), lambda: random.choice(["Hello", "World", "Goodbye"])]
    # test = Data("1. /$ 2. /$ 3. /$", val)
    # for _ in range(5):
    #     print(test.get_data())

    # vals = [('a', 1), ('b', 1), ('c', 8)]
    # wr = WeightedRandomizer(vals)
    # a = 0
    # b = 0
    # c = 0
    # er = 0
    # for _ in range(1000000):
    #     res = wr.getrand()
    #     if res == 'a':
    #         a += 1
    #     elif res == "b":
    #         b += 1
    #     elif res =="c":
    #         c += 1
    #     else:
    #         er += 1
    # print(f"a:{a}\nb:{b}\nc:{c}\nError:{er}")

    #time column
    tg = TimeGenerator()
    time_d = Data("/$",[tg.get_time])
    time = Column("Time", [(time_d, 1)])

    #id column
    

    # print(time_d.get_data())
    # print(time.generate_data())


if __name__ == "__main__":
    main()
