import pandas as pd
from pyearth import Earth

df = pd.read_csv('sj_y.csv')

sum = 0
for i in df['total_cases']:
    sum = sum + int(i)

sum = sum / len(df['total_cases'])
print(sum)

bool_list = df['total_cases']-sum > 15
int_data = [int(i) for i in bool_list]


df_x = pd.read_csv('sj.csv')

df_x['is_spike'] = int_data
df_x.to_csv('sj_spike.csv') 

df = pd.read_csv('iq_y.csv')

sum = 0
for i in df['total_cases']:
    sum = sum + int(i)

sum = sum / len(df['total_cases'])
print(sum)

bool_list = df['total_cases']-sum > 15
int_data2 = [int(i) for i in bool_list]

df_x = pd.read_csv('iq.csv')

df_x['is_spike'] = int_data2
df_x.to_csv('iq_spike.csv') 


df = pd.read_csv('dengue_features_train.csv')
df['is_spike'] = int_data+int_data2
df.to_csv('dengue_features_train_spike.csv')