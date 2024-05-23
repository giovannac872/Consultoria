# -*- coding: utf-8 -*-
import pandas as pd

class PreprocessionInput():
    mean = pd.read_csv('dataframes/mean_data.csv')
    std = pd.read_csv('dataframes/std_data.csv')

    def preprocessing_data(self, data, columns_preprocessing):
        
        data = pd.DataFrame([data])

        for column in data.columns:
            float_value = (float(data[column].iloc[0]))
            data[column] =   (float_value - self.mean[column]) / self.std[column]

        return data
