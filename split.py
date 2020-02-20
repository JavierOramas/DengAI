import pandas as pd

def split_csv():
    f = pd.read_csv('dengue_features_test.csv')
    df = pd.DataFrame(f)
    city = set(df['city'])
    print(city)
    for x in city:
        bool_list = df['city'] == x
        dt = df[bool_list]
        dt.to_csv(str(x)+'.csv')
split_csv()