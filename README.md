# cs5100_project

# Data Queries
*Undergraduate bachalors graduation rates from 4-year universities*
SELECT HD2021.INSTNM, HD2021.STABBR, HD2021.ZIP, HD2021.OBEREG, gr.GBA6RTT, gr.GBA6RTM, gr.GBA6RTW
FROM DRVGR2021 AS gr LEFT JOIN HD2021 ON gr.UNITID = HD2021.UNITID
WHERE HD2021.ICLEVEL = 1;


Notes: This query get the bachalors degree graduation rates from the 2015 cohort of first-time (undergraduate) students. Graduation rates will be the response in our study.