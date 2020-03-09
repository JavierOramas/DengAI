import pandas as pd
# import numpy as np

def split_csv(file_x,file_y,test):
    
    if test:
        fy = pd.read_csv(file_y) 
        df_cases = pd.DataFrame(fy)
    
    f = pd.read_csv(file_x)
    df = pd.DataFrame(f)
    city = set(df['city'])
    
    f = open('cities.txt','w')
    for i in city:    
        f.write(i+'\n')
        
    for x in city:
        bool_list = df['city'] == x
        dt = df[bool_list]
        dt_y = pd.DataFrame()
        if test:
            bool_list_cases = df_cases['city'] == x
            df_cases_filter = df_cases[bool_list_cases]
            dt_y['total_cases'] = df_cases_filter['total_cases']
        #a = np.array(dt)   
            dt.to_csv(str(x)+'.csv')
            dt_y.to_csv(str(x)+'_y.csv')
        else:
            dt.to_csv(str(x)+'_test.csv')
        
split_csv('dengue_features_train.csv','dengue_labels_train.csv',True)
split_csv('dengue_features_train.csv','',False)

# f = pd.read_csv('sj.csv')
# df = pd.DataFrame(f)
# print(df['total_cases'])

pred = ['1','2','3']
df = ''
df = pd.DataFrame(pred)
f = pd.read_csv('sj.csv')
df2 = pd.DataFrame(f)
df2['new'] = df[0]

print(df2['new'])