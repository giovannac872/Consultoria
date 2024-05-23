# -*- coding: utf-8 -*-
import os
import joblib
import pickle
import pandas as pd
from api.utils import PreprocessionInput


class Services():

    preprocessing_input = PreprocessionInput()
    
    def predict_individual_model(self, data):
        preprocess_columns = ['comprimento_sepala', 'largura_sepala', 'comprimento_petala', 'largura_petala']
    
        data_preprocess = self.preprocessing_input.preprocessing_data(data, preprocess_columns)

        model_knn = joblib.load('api/iris.pkl')

        return model_knn.predict(data_preprocess)