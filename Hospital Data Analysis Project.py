# Hospital Data Analysis Project

import pandas as pd
import matplotlib.pyplot as plt

# Hospital Dataset
data = {
    "Patient_ID":[101,102,103,104,105,106,107,108],
    "Age":[25,45,60,30,50,40,35,28],
    "Gender":["Male","Female","Male","Female","Male","Female","Male","Female"],
    "Disease":["Fever","Diabetes","Heart","Fever","Cancer","Fever","Diabetes","Heart"],
    "Doctor":["Dr.A","Dr.B","Dr.C","Dr.A","Dr.D","Dr.A","Dr.B","Dr.C"],
    "Bill_Amount":[2000,5000,12000,2500,20000,3000,6000,11000],
    "Stay_Days":[2,5,7,3,10,4,6,5]
}

# Create DataFrame
df = pd.DataFrame(data)

print("----- Hospital Dataset -----")
print(df)

# Basic Analysis
print("\nTotal Patients:", df.shape[0])
print("Average Age:", df["Age"].mean())
print("Total Hospital Revenue:", df["Bill_Amount"].sum())
print("Average Stay Days:", df["Stay_Days"].mean())

# Disease Distribution
print("\nDisease Count")
print(df["Disease"].value_counts())

# Doctor Performance
print("\nDoctor Patient Count")
print(df["Doctor"].value_counts())

# Highest Bill
print("\nHighest Bill Patient")
print(df.loc[df["Bill_Amount"].idxmax()])

# Visualization
df["Disease"].value_counts().plot(kind="bar")

plt.title("Hospital Disease Distribution")
plt.xlabel("Disease")
plt.ylabel("Number of Patients")

plt.show()