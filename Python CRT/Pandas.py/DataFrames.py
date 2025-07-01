import pandas as pd
Data={
    'Std1':
    {
    'Name':'Jyothi',
    'Branch':'Bio-informatics',
    'ID':'10001',
    'skills':['Python','dsa','sql','c']
    },

    'Std2':
    {
    'Name':'Madhuri',
    'Branch':'Bio-informatics',
    'ID':'10002',
    'skills':['Python','dsa','sql','c']
    }
}
Data=pd.DataFrame(Data)
print(Data)
print(type(Data))