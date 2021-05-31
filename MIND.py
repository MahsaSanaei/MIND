import texthero as hero
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.tree import DecisionTreeClassifier
from sklearn.cluster import KMeans
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.metrics.cluster import adjusted_rand_score, normalized_mutual_info_score, homogeneity_score ,completeness_score, v_measure_score




# load dataset

def load_dataset(filepath):
    dataset = pd.read_csv(filepath, header=None, sep='\t')
    dataset.columns = ['News ID', 'Category', 'SubCategory', 'Title', 'Abstract',
                    'URL', 'Title Entities', 'Abstract Entities']
    return dataset



# preprocessing the data

def data_loader(data):
    
    data.dropna(inplace=True)                  # remmoving Nan values
   
    data.drop_duplicates(['Title', 'Abstract'])          # removing duplicates  
    
    data['clean_title'] = hero.clean(data['Title'])         # cleaning the data
    data['clean_abstract'] = hero.clean(data['Abstract'])
    
    data_preprocessed = data[['Category', 'SubCategory', 'clean_title', 'clean_abstract']]   # selecting columns
    
    return data_preprocessed



# getting x, y of data

def get_data(data, title=False, abstract=False, category=False):
    
    if title and abstract==False:
        x = data['clean_title']
    
    elif abstract and title==False:
        x = data['clean_abstract']
    
    elif title==True and abstract==True:
        
        data['title_abstract'] = data['clean_title'] + data['clean_abstract']
        x = data['title_abstract']
    
    if category:
        y = data['Category']
    
    else:
        y = data['SubCategory']
     
    return x, y



# classification modeling

def classification_modeling(pipeline, x_train, y_train, x_validation, y_validation, x_test, y_test):
    
    pipeline.fit(x_train, y_train)      # train and fit a model
    
    dev_pred = pipeline.predict(x_validation)
    
    test_pred = pipeline.predict(x_test)
    
    print('Results for Validation Set:\n')
    print('accuracy:', accuracy_score(y_validation,dev_pred))         # Print the overall accuracy
    print(classification_report(y_validation,dev_pred))   # Print a classification report
    
    print('\n-------------------------------------------------------------------------------\n')
    
    print('Results for Test Set:\n')
    print('accuracy:', accuracy_score(y_test,test_pred))         # Print the overall accuracy
    print(classification_report(y_test,test_pred))   # Print a classification report
    


    
# clustering modeling

def clustering_modeling(pipeline, x_train, y_train, x_validation, y_validation, x_test, y_test):
    
    pipeline.fit(x_train)   
    
    dev_pred = pipeline.predict(x_validation)
    
    test_pred = pipeline.predict(x_test)
    
    print('Results for Validation Set:\n')
    print('adjusted_rand_score:', adjusted_rand_score(y_validation,dev_pred))         
    print('normalized_mutual_info_score:', normalized_mutual_info_score(y_validation,dev_pred)) 
    print('completeness_score:', completeness_score(y_validation,dev_pred))
    print('homogeneity_score:', homogeneity_score(y_validation,dev_pred))
    print('v_measure_score:', v_measure_score(y_validation,dev_pred))
    
    print('\n-------------------------------------------------------------------------------\n')
    
    print('Results for Test Set:\n')
    print('adjusted_rand_score:', adjusted_rand_score(y_test,test_pred))         
    print('normalized_mutual_info_score:', normalized_mutual_info_score(y_test,test_pred))   
    print('completeness_score:', completeness_score(y_test,test_pred))
    print('homogeneity_score:', homogeneity_score(y_test,test_pred))
    print('v_measure_score:', v_measure_score(y_test,test_pred))
