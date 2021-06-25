import json
import pandas as pd

# Open file with the website URLs of the different law firms and store them as a list
with open('variables.json') as f:
    data = json.load(f)
list_websites = data.keys()
list_websites = list(list_websites)

# Manually corrected ethnicities
white, black, latino_hispanic, asian, middle_eastern = [102, 7, 61, 62, 39], [0 ,0 ,0 ,0 ,1],[3, 0, 3, 3, 0],[5, 0, 1, 0, 0],[1, 0, 0, 0, 0] # ADD THE AMS ADVOCATEN NUMBERS CHECKED
dict_ethnicities = {"white":white, "black":black, "latino hispanic":latino_hispanic, "asian":asian, "middle eastern":middle_eastern}

# Create a dataframe with pandas
df = pd.DataFrame.from_dict(dict_ethnicities)
df["Law Firm"] = ["1", "2", "3", "4", "5"]
df = df.set_index(["Law Firm"])

# Calculate diversity parameters
df["Sum non white"] = df["black"] + df["latino hispanic"] + df["asian"] + df["middle eastern"]
df["Diversity percentage"] = df["Sum non white"]/df["white"]*100
df["Diversity percentage"] = df["Diversity percentage"].round(1)

# Show dataframe
pd.set_option("display.max_rows", None, "display.max_columns", None)
print(df)
df.to_csv("table2.csv")

