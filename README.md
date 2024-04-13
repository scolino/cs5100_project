# Using Supervised Machine Learning and Genetic Variable Selection to Predict Institutionals Graduation Rates

### Goal:
* Run Decision Tree Models on IPEDS data to predict graduation rate. These results will act as our basaeline.
* Use Genetic Algorithm to find the most relevant features.  Rerun our supervised algorithms using just these features.
* Build a Neural Network to predict graduation rates. 

### References:
https://www.kaggle.com/code/tanmayunhale/genetic-algorithm-for-feature-selection
See lecture 5 slides from class

### Steps
* Test/Train Split


# Data Queries
*Undergraduate bachalors graduation rates from 4-year universities*
SELECT HD2021.INSTNM, HD2021.STABBR, HD2021.ZIP, HD2021.OBEREG, gr.GBA6RTT, gr.GBA6RTM, gr.GBA6RTW
FROM DRVGR2021 AS gr LEFT JOIN HD2021 ON gr.UNITID = HD2021.UNITID
WHERE HD2021.ICLEVEL = 1;

Notes: This query get the bachalors degree graduation rates from the 2015 cohort of first-time (undergraduate) students. Graduation rates will be the response in our study.

*Predictive Features*
