import pandas as pd

df = pd.read_csv("./www.cleerdin-hamer.nl/ethnicity_analysis.csv")
frequency_eth = df['Ethnicity'].value_counts()
frequency_gender = df['Gender'].value_counts()

print("Ethnicity")
print(frequency_eth)
print("")
print("Gender")
print(frequency_gender)
