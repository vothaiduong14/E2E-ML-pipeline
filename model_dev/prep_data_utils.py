import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler


def preprocess_data(df):
    # Encode gender
    df['Gender'] = df['Gender'].map({'Male':0, 'Female':1})
    
    # Convert Region_code and Policy_Sales_Channel into categoricals (Object)
    df['Region_Code'] = df['Region_Code'].apply(lambda x: str(int(x)))
    df['Policy_Sales_Channel'] = df['Policy_Sales_Channel'].apply(lambda x: str(int(x)))
    
    # One hot encoding of categorical variables (with drop first)
    df = pd.get_dummies(df, drop_first=True)
    
    # Rename vehicle columns
    df = df.rename(columns={"Vehicle_Age_< 1 Year": "Vehicle_Age_lt_1Y", 
                            "Vehicle_Age_> 2 Years": "Vehicle_Age_gt_2Y"})
    df['Vehicle_Age_lt_1Y'] = df['Vehicle_Age_lt_1Y'].astype('int')
    df['Vehicle_Age_gt_2Y'] = df['Vehicle_Age_gt_2Y'].astype('int')
    
    # Drop ID column
    df = df.drop('id',axis=1)
    return df

def split_train_test(df):
    # Split into train and test
    train = df.sample(frac=0.8, random_state=0)
    test = df.drop(train.index)
    return train, test

def scale_data(df, numerical_features):
    # Scale data
    scaler = MinMaxScaler()
    df[numerical_features] = scaler.fit_transform(df[numerical_features])
    return df

    