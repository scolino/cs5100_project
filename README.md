# Using Supervised Machine Learning and Genetic Algorithm Variable Selection to Predict Institutionals Graduation Rates

### Methods:
* Run Decision Tree and Multiple Linear Regression on IPEDS data to predict graduation rate. These results will act as our basaeline.
* Test various parameters for the Decision Tree
* Test various parameters for the GA for both ML algorithms.

### Coding References:

https://www.kaggle.com/code/tanmayunhale/genetic-algorithm-for-feature-selection

https://kushalmukherjee.medium.com/a-brief-introduction-to-genetic-algorithm-and-its-use-in-feature-selection-using-deap-81c7e2a3d3b9

https://towardsdatascience.com/introduction-to-genetic-algorithms-including-example-code-e396e98d8bf3


### Data Queries:

*Undergraduate bachalors graduation rates from 4-year universities*

SELECT HD2021.INSTNM, HD2021.STABBR, HD2021.ZIP, HD2021.OBEREG, gr.GBA6RTT, gr.GBA6RTM, gr.GBA6RTW
FROM DRVGR2021 AS gr LEFT JOIN HD2021 ON gr.UNITID = HD2021.UNITID
WHERE HD2021.ICLEVEL = 1;

Notes: This query get the bachalors degree graduation rates from the 2015 cohort of full-time first-time (undergraduate) students. Graduation rates will be the response in our study.

*Predictive Features*


### Data Files:

**cs5100_project.csv**: Graduation rate data corrisponding to the first query.
**fall_enrollment.csv**: Enrollment counts used to filter school in data set.
**main_data.csv** & **main_data2.csv**: Predictive features queried from the 2016-2017 data.
**teaching_faculty.csv**: Predictive feature regarding instuctor diversity.
**final_data.csv**: Final data on which the algorithms of interest were implimented. This data is creates from *1_data_cleaning.ipynb*.

### Code Files:

**1_data_cleaning.ipynb**: Pre-processes and joins the IPEDS data for the study.
**2_model_building.ipynb**: Builds the models and runs the experiments.
**genetic_algorithm.py**: Class implimentation for the genetic algorithm use in the study.

Note: To run files, data paths need to get updated to the local computer.