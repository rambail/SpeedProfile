#!/usr/bin/env python
# coding: utf-8


import pandas as pd
import os

class CSVLoader:
    def __init__(self, csv_dir="csv"):
        self.csv_dir = csv_dir  # Directory where CSV files are stored

    def load_parameters_from_csv(self, csv_path):
        """Loads a CSV file and returns data as a dictionary or DataFrame."""
        file_path = os.path.join(self.csv_dir, csv_path)
        df = pd.read_csv(file_path)
        if csv_path == 'train_parameters.csv':
            # Convert specific CSV to a dictionary with key-value pairs
            return df.set_index('Parameter')['Value'].to_dict()
        else:
            # Return DataFrame for other CSV files
            return df

    def load_csv_list(self, csv_files):
        """Loads multiple CSV files based on a list of tuples (filename, label)."""
        data_dict = {}
        for csv_path, label in csv_files:
            data_dict[label] = self.load_parameters_from_csv(csv_path)
        return data_dict
