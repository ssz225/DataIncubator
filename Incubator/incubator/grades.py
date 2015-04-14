import pandas as pd
import matplotlib.pyplot as plt


def test_grades(grade_list):
    """Assuming list of grades given already sorted by DESCENDING date order:
    Assign A, B, C, to 1, 0, -1 and compare the most recent grade to its past grade.
    If the most recent grade has a higher value, the function returns 1;
    if the most recent grade is lower, return -1;
    if the grades are equal or if there is only one grade, return 0"""
    grades_key = ['A','B','C']
    values = [1, 0, -1]
    d_grades = dict(zip(grades_key, values))
    grades_int_list = [d_grades[grade] for grade in grade_list]
    
    #if only 1 item in grade_list, then return 0
    if len(grade_list) == 1:
        return 0
    
    current_grade = grades_int_list[0]
    past_grade = grades_int_list[-1]
    
    #return 1 if improving
    if current_grade > past_grade:
        return 1
    #return -1 if declining
    if current_grade < past_grade:
        return -1
    #return 0 i f stayed the same
    if current_grade == past_grade:
        return 0
 
def test_restaurant_grades(camis_id, df):
    #for each restaurant examine if grade improves, declines, or stays the same over time
    grade_list = []
    restaurant_grade = df[df.CAMIS == camis_id].GRADE
    for grade in restaurant_grade:
        grade_list.append(grade)
    test = test_grades(grade_list)
    return test
    #return 1 if improving, return -1 if declining, return 0 if stayed the same
# 
def graph(df, location):
    #convert grade date to date time
    df['GRADE DATE'] = pd.to_datetime(df['GRADE DATE'])
    grouped_df = df.groupby(['GRADE DATE','GRADE']).size().unstack()
    plt.figure(figsize = (20,10))
    plt.plot(grouped_df.index, grouped_df['A'], label = 'Grade A')
    plt.plot(grouped_df.index, grouped_df['B'], label = 'Grade B')
    plt.plot(grouped_df.index, grouped_df['C'], label = 'Grade C')
    plt.title('Number of Restaurants with Each Grade in {} Over Time'.format(location))
    plt.xlabel('Time')
    plt.ylabel('Number of Restaurants')
    plt.legend(loc = 'upper left')
    plt.savefig('grade_improvement_{}.pdf'.format(location))

def main():
    """This program is designed to clean and analyze the restaurant grades data 
    (NYC_Restaurant_Inspection_Results) from the NYC DOHMH. 
    The results drawn using citywide and borough-wide data are: 
    graphs of the distribution of A, B, and C's over the years,
    net improvements in participating restaurants,
    distribution ."""

    #import dataset 
    df = pd.read_csv('NYC_Restaurant_Inspection_Results.csv')
    #remove NaNs
    df = df.dropna()
    #filter to only relevant columns
    df = df[['CAMIS', 'BORO', 'GRADE', 'GRADE DATE', 'CUISINE DESCRIPTION']]
    #filter to only entries with valid grades
    grades = df[(df.GRADE == 'A')|(df.GRADE == 'B')|(df.GRADE == 'C')]
#      
#     #Question 4. print and compute sum of test_restaurant_grades for all restaurant
    sum_all = 0
    unique_CAMIS = grades.CAMIS.unique()
    for CAMIS in unique_CAMIS:
        sum_all = sum_all + test_restaurant_grades(CAMIS, grades)
    print 'Sum of test_restaurant_grades for all restaurants is: ' + str(sum_all)
    graph_nyc = graph(grades, 'nyc')
#  
#       
    #print and compute sum of test_restaurant_grades for each borough
    boro = ['MANHATTAN','QUEENS','BROOKLYN','STATEN ISLAND','BRONX']
    for borough in boro:
        sum_boro = 0
        boro_df = grades[grades.BORO == borough]
        unique_CAMIS = boro_df.CAMIS.unique()
        for CAMIS in unique_CAMIS:
            sum_boro = sum_boro + test_restaurant_grades(CAMIS, boro_df)
        graph(boro_df, '{}'.format(borough))
        print 'The sum of test_restaurant_grades for all restaurants in ' + borough + ' is: ' + str(sum_boro)
       


if __name__=='__main__':
    main()