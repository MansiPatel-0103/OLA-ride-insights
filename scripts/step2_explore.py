# step2_explore.py
# Our first look at the OLA data

import pandas as pd

print("Opening the OLA data... please wait")

df = pd.read_excel("data/raw/OLA_DataSet.xlsx", sheet_name="July")

print("Done! The data is open.")
print()

# 1. How big is the table?
print("Number of rides (rows):", df.shape[0])
print("Number of columns:", df.shape[1])
print()

# 2. What are the column names?
print("Column names:")
for column in df.columns:
    print("-", column)
print()

# 3. Look at one ride
print("Here is the first ride in the table:")
print(df.iloc[0])
print()

# 4. What happened to the rides?
print("How many rides of each booking status:")
print(df["Booking_Status"].value_counts())