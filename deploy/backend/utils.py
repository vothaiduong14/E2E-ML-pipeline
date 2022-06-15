import pandas as pd
from sklearn.preprocessing import MinMaxScaler

BINARY_COLS = ['Gender']
CATEGORIC_COLS = ['Region_Code', 'Policy_Sales_Channel']
NUMERIC_COLS = ['Age', 'Vintage', 'Annual_Premium']

class DataProcessor:
    def __init__(self, df):
        self.df = df

    def process_data(self):
        self._encode_binary(BINARY_COLS)
        self._convert_categorical(CATEGORIC_COLS)
        self._rename_column()
        self._scale_data(NUMERIC_COLS)
        # Drop ID column
        self.df = self.df.drop('id',axis=1)
        

    def _encode_binary(self, columns):
        '''
        This encode binary columns to 0 and 1
        Need to check for unique values in the input data
        '''
        for col in columns:
            unique_vals = self.df[col].unique()
            self.df[col] = self.df[col].map({unique_vals[0]:0, unique_vals[1]:1})

    def _convert_categorical(self, columns):
        '''
        This convert categorical columns to numeric representation
        '''
        for col in columns:
            self.df[col] = self.df[col].apply(lambda x: str(int(x)))

        # One hot encoding of categorical variables (with drop first)
        self.df = pd.get_dummies(self.df, drop_first=True)

    def _rename_column(self):
        '''
        This rename columns
        '''
        replace_dict = {' ': '_', '<': 'lt', '>': 'gt'}
        for col in self.df.columns:
            new_col = col
            for key, val in replace_dict.items():
                new_col = new_col.replace(key, val)

            if new_col != col:
                self.df.rename(columns={col: new_col}, inplace=True)


    def _scale_data(self, numeric_cols):
        '''
        This scale data
        '''
        scaler = MinMaxScaler()
        self.df[numeric_cols] = scaler.fit_transform(self.df[numeric_cols])

    def split_train_test(self):
        # Split into train and test
        train = self.df.sample(frac=0.8, random_state=0)
        test = self.df.drop(train.index)
        return train, test