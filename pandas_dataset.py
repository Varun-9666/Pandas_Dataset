# -*- coding: utf-8 -*-
"""Pandas dataset.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1l0pVsl5r9LoU3tdtuziFFRuEeCW8ACgh

###### Assessment

###### I am going to provide two .csv files , you are supposed to work on them and have to provide solutions to the following problems

###### import necessary libraries
"""

import pandas as pd

"""###### merge those two csv files (after getting as dataframes, get them as a single dataframe)"""

# Getting data from one file
file1 = pd.read_csv('/content/college_1.csv')
file1

# Getting data from second file
file2 = pd.read_csv('/content/college_2.csv')
file2

# Merging the above two files
df = pd.concat(
    map(pd.read_csv, ['/content/college_1.csv', '/content/college_2.csv']), ignore_index=True)
print(df)

"""###### Take each csv file , split that csv file into multiple categories (example csv files are added in the repo)

###### consider if the codekata score exceeds 15000 points(present week) then make a csv on those observations as Exceeded expectations.csv
"""

a = df[df['CodeKata Score']>15000]
# saving data frame to new csv file
a.to_csv('Exceeded expectations.csv')

"""###### if  10000<codekata score<15000   (Reached_expectations.csv)


"""

b = df[(df['CodeKata Score']>10000) & (df['CodeKata Score']<15000)]
# saving data frame to new csv file
b.to_csv('Reached_expectations.csv')

"""###### if  7000<codekata score<10000   (Needs_Improvement.csv)

"""

c = df[(df['CodeKata Score']>7000) & (df['CodeKata Score']<10000)]
# saving data frame to new csv file
c.to_csv('Needs_Improvement.csv')

"""###### if  codekate score < 7000        (Unsatisfactory.csv)"""

d = df[df['CodeKata Score']<7000]
# saving data frame to new csv file
d.to_csv('Unsatisfactory.csv')