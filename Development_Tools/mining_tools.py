import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def load_data_frames(directory, csvlist, N):
    '''
    input:

    directory: the location of the csv data files
    csvlist: the names of the csv files (including '.csv' suffix)

    output:

    df_list: a list of dataframe handles

    '''

    df_list = []
    for file in csvlist:
        df = pd.read_csv(directory+file)
        df_list.append(df)
    return df_list

''' Main '''

# Get the data

data_path = "..\Opiate_Prescriptions_Overdoses\\"
data_files = ['opioids.csv', 'overdoses.csv', 'prescriber-info.csv']
opiods_df, overdoses_df, prescriber_info_df = \
    load_data_frames(data_path, data_files, len(data_files))
print "...data loaded..."

# See what's going on with the data