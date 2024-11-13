import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
   
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("choose a city (chicago, new york city, washington) : ").strip().lower()
        if city in ['chicago' , 'new york city' , 'washington']:
            break
        else:
                print("Oops! please enter a correct city name.")

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input(" choose a month (from january to june) or 'all' : ").strip().lower()
        if month in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
            break
        else:
                print("Oops! enter a correct month or 'all'.")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input ("choose a day of the week or 'all' :").strip().lower()
        if day in ['saturday', 'friday', 'thursday', 'wednesday', 'tuesday', 'monday', 'sunday', 'all']:
            break
        else:
                print("Oops! enter a correct day or 'all'.")

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    df = pd.read_csv(CITY_DATA[city])
    
      
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    
    df['month'] = df['Start Time'].dt.month_name().str.lower()
    df['day_of_week'] = df['Start Time'].dt.day_name().str.lower()

   
    if month != 'all':
        df = df[df['month'] == month]

    
    if day != 'all':
        df = df[df['day_of_week'] == day]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print("Most common time to travel: \n")
    common_month = df['month'].mode()[0]
    print(f"month:{common_month} ")
    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print(f"day:{common_day} ")


    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print("hour: ",df['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_st = df['Start Station'].mode()[0]
    print(f"the most commonly used station is: {common_start_st} ")

    # TO DO: display most commonly used end station 
    common_end_st = df['End Station'].mode()[0]
    print(f"the most commonly used end station is: {common_end_st} ")


    # TO DO: display most frequent combination of start station and end station trip
    df['start-end'] = df['Start Station'] + "to" + df['End Station']
    common_trip = df['start-end'].mode()[0]
    print(f"the most frequent combination of trip is: {common_trip} ")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
 

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    tot_travel_time = df['Trip Duration'].sum()
    print(f"total travel time is: {tot_travel_time} ")

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print(f"mean travel time is: {mean_travel_time} ")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):


    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    if 'User Type' in df.columns:
        user_type = df['User Type'].value_counts()
        print("counts of user types:")
        print (user_type)

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender_count = df['Gender'].value_counts()
        print("counts of gender:")
        print(gender_count)


    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_b_y = int(df['Birth Year'].min())
        recent_b_y = int(df['Birth Year'].max())
        common_b_y = int(df['Birth Year'].mode()[0])
        
        print (" birth year status :")
        print (f"earliest : {earliest_b_y}")
        print (f"most recent : {recent_b_y}")
        print (f"most common birth year : {common_b_y}")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    row = 0
    while True:
        show_data = input("\n Would you like to see 5 lines of raw data? Enter yes or no: ").strip().lower()
        if show_data != 'yes':
            break
        

        print(df.loc[row:row + 5])
        
        row += 5
        
        if row >= len(df):
            print("No more data")
            break     

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

        

if __name__ == "__main__":
	main()
