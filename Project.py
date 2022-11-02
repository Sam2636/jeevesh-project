import os
import pandas as pd
from csv import DictWriter
 
# list of column names
field_names = ["Types of cars","Brand","Price"]
table_one = {
    'Types of cars':["SUV","SEDAN","COMPACT","LIMO","EV"],
    'Brand':["LAND ROVER","BENZ","MINI","HUMMER","TESLA"],
    'Price':[100000,200000,300000,400000,500000]
}

output=pd.DataFrame(table_one)
output.to_csv("cars.csv",index= False)
print(table_one)

print(output.shape)
print(output.info)
print(output.describe)
print(output.head)
print(output.tail)
print(output.head(2))
print(output.tail(2))
x=output.iat[1,2]
print(x)

def adding_data():
    print("do you want to add data? yes or no")
    entry=input()
    if entry=="yes":
        car_type=input("Enter the car type : ")
        brand=input("Enter the brand : ")
        price=input("Enter the Price : ")
        add_data={
            'Types of cars':car_type,
            'Brand':brand,
            'Price':price
        }
        with open('cars.csv', 'a') as f_object:
 
            # Pass the file object and a list
            # of column names to DictWriter()
            # You will get a object of DictWriter
            dictwriter_object = DictWriter(f_object, fieldnames=field_names)
        
            # Pass the dictionary as an argument to the Writerow()
            dictwriter_object.writerow(add_data)
        
            # Close the file object
            f_object.close()
adding_data()




def first():
    print("get val for your preferd top row")
    val=int(input())
    print(output.head(val))
    
first()

def bottom():
    print("get val for your preferd top row")
    val=int(input())
    print(output.tail(val))
    
bottom()

def basic():
    print("Do you want basic stat? yes or no")
    ok=input()
    if ok=="yes":
        print(output.shape)
        print(output.info)
        print(output.describe)


basic()