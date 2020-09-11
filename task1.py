import pandas as pd
import csv
import matplotlib.pyplot as plt 

with open("biopic.csv") as f:
    reader = csv.reader(f)
    next(reader)

    data = []
    for row in reader:
        data.append({
            "evidence": [str(cell) for cell in row[:]],
            "label": "No. of subjects 1" if row[6] == "1" else row[6] == "0" "No. of subjects 0"
        })
        
    print(data)

df =  pd.read_csv("biopic.csv") 

  
#plotting points as a scatter plot 
x = df["country"] 
y = df["year_release"] 
plt.scatter(x, y, label= "stars", color= "m",  
            marker= "*", s=30) 
# x-axis label 
plt.xlabel('country') 
# frequency label 
plt.ylabel('year release') 
# function to show the plot 
plt.show() 
