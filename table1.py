import json
import pandas as pd

# Open file with the website URLs of the different law firms and store them as a list
with open('variables.json') as f:
    data = json.load(f)
list_websites = data.keys()
list_websites = list(list_websites)

# Perform the earlier discussed
# Here should be the reference to ethnicity identification functions
# Make the output file a csv file called "ethnicity_analysis.csv"

# Define ethnicities in a dictionary and make a list of different ethnicities for counting
dict_ethnicities = {"white":[], "black":[], "latino hispanic":[], "asian":[], "middle eastern":[]}
white, black, latino_hispanic, asian, middle_eastern = [],[],[],[],[]

# loop over website URLs and count ethnicity per URL
for i in list_websites:
    ind = i.index("//")
    website_link = i[ind + 2:]
    df = pd.read_csv(website_link + "ethnicity_analysis.csv")
    frequency_eth = df['Ethnicity'].value_counts()
    frequency_gender = df['Gender'].value_counts()
    for i in dict_ethnicities:
        try:
            dict_ethnicities[i].append(frequency_eth[i])
        except KeyError as e:
            print("ETHNICITY", i,"NOT FOUND")
            dict_ethnicities[i].append(0)

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
sourceFile = open('table1.txt', 'w')
print(df, file = sourceFile)
sourceFile.close()
df.to_csv("table1.csv")

