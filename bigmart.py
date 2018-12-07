import pandas as pd
train = pd.read_csv('Train.csv')
train.columns
unique = train['Item_Identifier'].value_counts()

def fillnan (value):
    if (value == 'nan'):
        

train.groupby(['Item_Identifier','Item_Weight']).mode()       
