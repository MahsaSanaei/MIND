# MIND

This project is about MIND dataset. MIcrosoft News Dataset (MIND) is a large-scale dataset for news recommendation research. It was collected from anonymized behavior logs of Microsoft News website. 

## Steps of Project:

### Step 1: 

* R&D on MIND dataset


### Step 2:

* Some general search about the task


### Step 3: 

* 01-download.ipynb: download the dataset using python


### Step 4: 

* Having a look at the data


### Step 5: 

* Preprocessing


### Step 6:
 
* Implement baseline classification model with Tfidf and Evaluation 

* 02-baseline-classification.ipynb

#### Results:
  
 Validation Set Results:
             
|             |   title     |  abstract  | title-abstract |
| ----------- | ----------- | ---------- | -------------- |
| accuracy    |    0.982    |   0.979    |     0.984      |
| f1score     |    0.96     |   0.97     |     0.97       |

 Test Set Results:
             
|             |   title     |  abstract  | title-abstract |
| ----------- | ----------- | ---------- | -------------- |
| accuracy    |    0.905    |   0.899    |     0.907      |
| f1score     |    0.88     |   0.84     |     0.88       |



### Step 7:
 
* Implement baseline clustering model with Tfidf and Evaluation 

* 02-baseline-clustering.ipynb
 
 #### Results:
  
  Validation Set Results:
             
|                              |   title     |  abstract  | title-abstract |
| ---------------------------- | ----------- | ---------- | -------------- |
| adjusted_rand_score          | -0.029107   | -0.03777   |   -0.0149      |
| normalized_mutual_info_score |  0.098005   |  0.166     |    0.203       |
| completeness_score           |  0.10593    |  0.1794    |    0.2123      |
| homogeneity_score            |  0.09117    |  0.15447   |    0.1956      |
| v_measure_score              |  0.09800    |  0.166     |    0.2036      |

 Test Set Results:
             
|                              |   title     |  abstract  | title-abstract |
| ---------------------------- | ----------- | ---------- | -------------- |
| adjusted_rand_score          | -0.027581   | -0.03039   |   -0.004       |
| normalized_mutual_info_score |  0.096365   |  0.16741   |    0.2054      |
| completeness_score           |  0.10235    |  0.1772    |    0.209       |
| homogeneity_score            |  0.09103    |  0.1586    |    0.201       |
| v_measure_score              |  0.09636    |  0.16741   |    0.205       |


### Step 8: 

* Compare the results of the classification and clustering models

