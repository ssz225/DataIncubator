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
It appears that overall, the grades for NYC restaurants have increased.
The overall grades for each borough have also increased.
While the number of restaurants earning A's have increased dramatically since 2011, 
the number of B's and C's have remained relatively stable since 2011.
The general shape of the distribution across time is mimicked across all boroughs. 
The number of A's (and overall activity in awarding of grades) appear to peak every 
year around May across all boroughs. Low activity points generally land in the fall months.
There was a gap in grading activity in November 2012.

The sum of test_restaurant_grades for all restaurants is: 2086
The sum of test_restaurant_grades for all restaurants in MANHATTAN is: 754
The sum of test_restaurant_grades for all restaurants in QUEENS is: 500
The sum of test_restaurant_grades for all restaurants in BROOKLYN is: 542
The sum of test_restaurant_grades for all restaurants in STATEN ISLAND is: 54
The sum of test_restaurant_grades for all restaurants in BRONX is: 232

The dataset also includes information on the reasoning behind the grades and provides
insights on which violations were triggered. This information provides insight on which
issues are most widespread in the restaurant industry in NYC, which can be useful in 
forming policies to address these issues in order of commonality to improve restaurant quality.

Grouping by the Cuisine Description, it is possible to see that perhaps restaurants
serving certain cuisine types are in need of more scrutiny in quality than others.
