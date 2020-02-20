import pandas as pd

def split_csv(file_x,file_y,test):
    
    if test:
        fy = pd.read_csv(file_y) 
        df_cases = pd.DataFrame(fy)
    
    f = pd.read_csv(file_x)
    df = pd.DataFrame(f)
    city = set(df['city'])
    
    print(city)
    for x in city:
        
        bool_list = df['city'] == x
        dt = df[bool_list]
        
        if test:
            bool_list_cases = df_cases['city'] == x
            df_cases_filter = df_cases[bool_list_cases]
            dt['total_cases'] = df_cases_filter['total_cases']
            
        dt.to_csv(str(x)+'.csv')
        
split_csv('dengue_features_train.csv','dengue_labels_train.csv',True)
f = pd.read_csv('sj.csv')
df = pd.DataFrame(f)
print(df['total_cases'])