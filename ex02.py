import numpy as np
import pandas as pd
def ex02():
    #q1
    path = "C:\\Users\\Dell\\OneDrive\\Desktop\\0_1.24 Sem\\Computer tools\\Data\\03-member.csv"
    df = pd.read_csv(path)
    df1 = df.query("city in ('Nancy')")
    #print(df1)
    df2 = df1.query("gender in ('Male')")
   # print(df2)
    number_male = len(df2)
    #print("Number of Males in Nancy is" + ' ' + str(number_male))
    #q2
    df3 = df[['last_name']]
    employee_list = []
    for x in df3.index:  # x = 0
        #print(x)  # x =0
        employee_list.append(df3.at[x, 'last_name'])
        #print(employee_list)
    employee_list2 = list(dict.fromkeys(employee_list))  # specifying the keys in dictionary
    print(employee_list2)
    #print(len(employee_list2))
