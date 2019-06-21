# Import Python packages 
import re 
import os
import glob
import numpy as np
import json
import csv


def get_filepaths_to_process_event_data():
    '''
    Creating list of filepaths to process 
    original event csv data files
    '''
    # Get your current folder and subfolder event data
    filepath = os.getcwd() + '/event_data'
    # Create a for loop to create a list of files and collect each filepath
    for root, dirs, files in os.walk(filepath):

        # join the file path and roots with the subdirectories using glob
        file_path_list = glob.glob(os.path.join(root,'*'))
    return file_path_list


def process_event_data(file_path_list):
    '''
    Processing the files to create the 
    data file csv that will be used for Apache Casssandra tables
    '''

    full_data_rows_list = [] 
    
    # for every filepath in the file path list 
    for f in file_path_list:

    # reading csv file 
        with open(f, 'r', encoding = 'utf8', newline='') as csvfile: 
            # creating a csv reader object 
            csvreader = csv.reader(csvfile) 
            next(csvreader)

     # extracting each data row one by one and append it        
            for line in csvreader:
                #print(line)
                full_data_rows_list.append(line) 
    row_cnt= len(full_data_rows_list)

    # creating a smaller event data csv file called \
    # event_datafile_full csv that will be used to insert \ 
    # data into the Apache Cassandra tables
    csv.register_dialect(
        'myDialect', 
        quoting=csv.QUOTE_ALL,
        skipinitialspace=True
    )

    with open('event_datafile_new.csv', 'w', encoding = 'utf8', newline='') as f:
        writer = csv.writer(f, dialect='myDialect')
        writer.writerow(['artist','firstName','gender','itemInSession','lastName','length',\
                    'level','location','sessionId','song','userId'])
        for row in full_data_rows_list:
            if (row[0] == ''):
                continue
            writer.writerow((row[0], row[2], row[3], row[4], row[5], row[6], row[7], 
                             row[8], row[12], row[13], row[16]))
    
    # check the number of rows in your csv file
    with open('event_datafile_new.csv', 'r', encoding = 'utf8') as f:
        lines_in_csv = (sum(1 for line in f))
    print ('Read in {r} rows and wrote out {l} rows to new event file'.format(
    r=row_cnt, l=lines_in_csv))
    
if __name__ == '__main__':
    fpl = get_filepaths_to_process_event_data()
    process_event_data(fpl)
