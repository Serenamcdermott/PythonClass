import pandas as pd

df = pd.DataFrame(

    {
        "Name": [
            "Smith, Mr. John",
             "Cleary, Mrs. Ann",
            "Booth, Mr. Otis",
        ], 
        "Age": [22, 35, 58],
        "Sex": ["male", "female", "male"],
    }
)
print(df)