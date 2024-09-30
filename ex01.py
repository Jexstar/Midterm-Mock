import numpy as np
import pandas as pd
def ex01():
    #q1
    path = "C:\\Users\\Dell\\OneDrive\\Desktop\\0_1.24 Sem\\Computer tools\\Data\\04-customer-review.csv"
    df = pd.read_csv(path)
    df2 = df.groupby('number of stars')['number of stars'].count()
    print(df2)
    df5 = df[['number of stars']]
    starlist = []
    for x in df5.index:
        starlist.append(df5.at[x, 'number of stars'])
        #starlist.append(str(x))
    print(starlist)
    print("Number of 1 star reviews is" + " " + str(starlist.count(1)))
    print("Number of 2 star reviews is" + " " + str(starlist.count(2)))
    print("Number of 3 star reviews is" + " " + str(starlist.count(3)))
    print("Number of 4 star reviews is" + " " + str(starlist.count(4)))
    print("Number of 5 star reviews is" + " " + str(starlist.count(5)))
    #q2
    df3 = df[['product name']]
    product_list = []
    for x in df3.index:  # x = 0
        #print(x)  # x =0
        product_list.append(df3.at[x, 'product name'])
        #print(product_list)
    product_list2 = list(dict.fromkeys(product_list))  # specifying the keys in dictionary
    #print(product_list2)
    for x in product_list2:
        df4 = df[df['product name'] == x]
    #print(df4)
        average_stars = df4['number of stars'].to_numpy().mean()
        #print("Average stars of" + ' ' + x + ' ' + "is" + ' ' + str(average_stars))



