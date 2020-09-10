
#: Display a Breakdown of User Types
#There are different types of users specified in the "User Type" column. Find how many there are of each type and store the counts in a pandas Series in the user_types variable.

#Hint: What pandas function returns a Series with the counts of each unique value in a column?

import pandas as pd

filename = 'chicago.csv'

# load data file into a dataframe
df = pd.read_csv("chicago.csv")

unique_val = df["User Type"].value_counts()


# print value counts for each user type

print(unique_val)
