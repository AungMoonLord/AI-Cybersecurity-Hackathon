'''generate_data.py'''
import random
import linecache
import csv
import os
import string
import math

months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
cur_dir = os.path.dirname(__file__)
tables = ["accounts", "users", "account_type", "locations", "branchs", "countries", "transactions", "transaction_logs"]
characters = string.ascii_letters + string.digits + "_-"

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
            month_day = (months[self.month-1] + 1*(self.month == 2))
        else:
            month_day = months[self.month-1]

        if self.day > month_day:
            self.day -= month_day
            self.month += 1
        if self.month > 12:
            self.month -= 12
            self.year += 1

        return f"{self.year}-{self.month}-{self.day:<0d}T{self.hour}:{self.minute}:{self.second:.06f}Z"

    def get_time_no_inc(self):
        '''return time without incrementing'''
        return f"{self.year}-{self.month}-{self.day:<0d}T{self.hour}:{self.minute}:{self.second:.06f}Z"


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
        '''return random data'''
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
        self.str.append(temp)

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

class Row:
    '''
    Docstring for Row
    '''
    def __init__(self, tg : TimeGenerator, query : Data, is_anormaly : bool):
        '''constructor'''
        self.tg = tg
        self.query = query
        self.is_anormaly = is_anormaly

    def gen_row(self):
        '''genrate a row of randomized data'''
        return (self.tg.get_time() + "\t" + self.query.get_data(), str(self.is_anormaly))

class DatasetGenerator:
    '''
    Docstring for dataset_generator
    '''
    def __init__(self, normal : list, anormaly : list):
        '''
        constructor
        normal and anormaly = list of row
        '''
        self.tg = TimeGenerator()
        self.normal = WeightedRandomizer(normal)
        self.anormaly = WeightedRandomizer(anormaly)

    def generate_csv(self, num : int):
        '''generate csv file'''
        with open(f"{cur_dir}\\dataset.csv", mode="w", newline="", encoding="utf-8") as f:
            for i in range(num):
                print(f"Progress: {i/num*100:.2f}% {'■'*math.ceil(i/num*20)}")
                writer = csv.writer(f)
                if random.random() < 0.5:
                    data = self.normal.getrand()
                else:
                    data = self.anormaly.getrand()
                writer.writerow(data.gen_row())

def get_random_name():
    '''name'''
    return linecache.getline(f"{cur_dir}\\names.txt", random.randint(1, 100000)).strip()

def get_random_table():
    '''table'''
    return random.choice(tables)

def get_random_word():
    '''word'''
    return "".join(random.choices(characters, k=random.randint(5,20)))

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
    normal = []
    abnormal = []
    tg = TimeGenerator()

    #normal data
    get_session_id = lambda : random.randint(1, 99)
    get_money = lambda : random.randint(1, 100000)
    get_account_id = lambda : f"{random.randint(1,49):>02d}{random.randint(0,99999999):>07d}"

    val1 = [get_session_id, get_random_name]
    d1 = Data("/$\tQuery\tselect balance from accounts where account_id = '/$' for update;", val1)
    val2 = [get_session_id, get_money, get_account_id]
    d2 = Data("/$\tQuery\tupdate accounts set balance = balance - /$, last_updated = now() where account_id = '/$';", val2)
    val3 = [get_session_id, get_account_id, get_money, get_account_id, get_account_id]
    d3 = Data("/$\tQuery\tinsert into transactions values (/$, 'DEPOSIT', /$, (SELECT balance FROM Accounts WHERE account_id = /$), /$, NOW(), @ idempotency_key);", val3)
    val4 = [get_session_id]
    d4 = Data("/$\tQuit", val4)
    val5 = [get_session_id, lambda : get_random_name().split()[0]]
    d5 = Data("/$\tConnect\t/$@10.6.1.1", val5)

    normal.append((Row(tg, d1, False), 1))
    normal.append((Row(tg, d2, False), 1))
    normal.append((Row(tg, d3, False), 1))
    normal.append((Row(tg, d4, False), 1))
    normal.append((Row(tg, d5, False), 1))
    

    #anormaly data
    aval1 = [get_session_id, get_random_word, get_random_word, get_random_word, get_random_word, lambda : random.choice( ["1=1", "'='", '"1"="1"', '""=""', "'1'='1'"] )]
    ad1 = Data("/$\tQuery\tselect /$ from /$ where /$ = '/$' or /$", aval1)
    aval2 = [get_session_id, get_random_word]
    ad2 = Data("/$\tQuery\tdrop table /$", aval2)

    abnormal.append((Row(tg, ad1, True), 1))
    abnormal.append((Row(tg, ad2, True), 1))

    num = 900000
    dg = DatasetGenerator(normal, abnormal)
    dg.generate_csv(num)

    # print(ad1.get_data())


if __name__ == "__main__":
    main()
