# step3_check_problems.py
# Health check: find problems in the OLA data before we clean it

import pandas as pd

print("Opening the OLA data... please wait")
df = pd.read_excel("data/raw/OLA_DataSet.xlsx", sheet_name="July")
print("Done!")
print()

# 1. How many empty boxes in each column?
print("EMPTY BOXES in each column:")
print(df.isnull().sum())
print()

# 2. Are any rides repeated?
print("Repeated rows:", df.duplicated().sum())
print("Repeated Booking IDs:", df["Booking_ID"].duplicated().sum())
print()

# 3. What type of data is in each column?
print("DATA TYPE of each column:")
print(df.dtypes)