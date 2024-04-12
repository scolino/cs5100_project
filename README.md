# Using Supervised Machine Learning to Predict IPEDS Graduation Rates

### Goal:
* Run Linear Regression Models and Decision Tree Models on IPEDS data to predict graduation rate. These results will act as our basaeline.
* Use Genetic Algorithm to find the most relevant features.  Rerun our supervised algorithms using just these features.
* Run as play with classifying (high, med, low)
* Feature Engineering vs NN

### References:
https://www.kaggle.com/code/tanmayunhale/genetic-algorithm-for-feature-selection
See lecture 5 slides from class

### Steps
* Test/Train Split

## Data
# cs5100_project

# Data Queries
*Undergraduate bachalors graduation rates from 4-year universities*
SELECT HD2021.INSTNM, HD2021.STABBR, HD2021.ZIP, HD2021.OBEREG, gr.GBA6RTT, gr.GBA6RTM, gr.GBA6RTW
FROM DRVGR2021 AS gr LEFT JOIN HD2021 ON gr.UNITID = HD2021.UNITID
WHERE HD2021.ICLEVEL = 1;


Notes: This query get the bachalors degree graduation rates from the 2015 cohort of first-time (undergraduate) students. Graduation rates will be the response in our study.
