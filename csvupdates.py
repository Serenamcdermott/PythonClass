import pandas as pd 
import random 
import string 

input_file = "MonthlyStoreMetrics.csv"
output_file = "results.csv"

df = pd.read_csv(input_file)

random_strings = [''.join(random.choice(string.ascii_letters)
                          for _ in range(10))
                             for _ in range(len(df))]

df.iloc[:, 0] = random_strings 

df.to_csv(output_file, index=False)

print(f"Modified data saved to {output_file}")