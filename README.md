# DataIncubator
Database of NYC Restaurant Inspection Grades: https://data.cityofnewyork.us/Health/DOHMH-New-York-City-Restaurant-Inspection-Results/xx67-kt59

The goal is to assess if the quality of restaurants is improving as a result of the grading system that was introduced in 2010.

Import & Cleaning:
Dataset is imported into a pandas DataFrame. 
Invalid entries (eg. non-A,B,C grades) were removed.
Dropped unuseful columns.

Main methods:
test_restaurant_grades(camis_id) returns 1 if the grades for the restaurant are improving, -1 if they are declining, or 0 if they have stayed the same.

Sum of test_restaurant_grades(camis_id) was calculated over all restaurants in the dataset and for each of the five Boroughs in order to determine overall performance of all restaurants in NYC.

The following six graphs were generated:
1. A graph that shows the total number of restaurants in New York City for each grade over time
2-6. One graph for each of the five Boroughs that shows the total number of restaurants in
the Borough for each grade over time.

Results:
