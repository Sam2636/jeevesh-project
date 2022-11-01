import os
import pandas as pd
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
