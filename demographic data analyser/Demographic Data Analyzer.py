import pandas as pd

def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    df_men = df[df['sex'] == 'Male']
    average_age_men = round(df_men['age'].mean(),1)

    # What is the percentage of people who have a Bachelor's degree?
    c1 = df['education'].count()
    df_BE = df[df['education'] == 'Bachelors']
    c2 = df_BE['education'].count()
    percentage_bachelors = round((c2/c1)*100,1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    df_adv_edu = df[(df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate')]
    higher_education = df_adv_edu['education'].count()
    df_50K = df_adv_edu[df_adv_edu['salary'] == '>50K']
    c4 = df_50K['salary'].count()  
    # with and without `Bachelors`, `Masters`, or `Doctorate`
    
    df_low_edu = df[(df['education'] != 'Bachelors') & (df['education'] != 'Masters') & (df['education'] != 'Doctorate')]
    lower_education = df_low_edu['education'].count()
    c5 = df_low_edu[df_low_edu['salary'] == '>50K'].salary.count()

    # percentage with salary >50K
    higher_education_rich = round((c4/higher_education*100),1)
    lower_education_rich = round((c5/lower_education*100),1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours =  df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    df_min_hrs = df[(df['hours-per-week'] == min_work_hours)]
    num_min_workers = df_min_hrs['salary'].count()
    c6 = df_min_hrs[df_min_hrs['salary'] =='>50K'].salary.count()

    rich_percentage = round((c6/num_min_workers)* 100,1)
    
    # What country has the highest percentage of people that earn >50K?
    df_rich = df[df['salary'] == '>50K']
    abc = df_rich['native-country'].value_counts()
    cab = df['native-country'].value_counts()
    percent = round((abc/cab*100),1)
    highest_earning_country = percent[percent == percent.max()].index
    highest_earning_country_percentage = percent.max()

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = df_rich[df_rich['native-country']=='India'].occupation.value_counts().index[0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)
        
    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
