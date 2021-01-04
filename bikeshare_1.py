import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york, washington). HINT: Use a while loop to handle invalid inputs
    city = input('would you like to see data for Chicago, New york or Washington? ').lower()
    while city not in (CITY_DATA.keys()):
        print('Wrong selection, try again')
        city = input('would you like to see data for Chicago, New york or Washington? ').lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    time = input('would you like to filter the data by Month, Day, Both or None? ' ).lower()
    while time not in (['month', 'day', 'both', 'none']):
        print('Wrong selection, try again')
        time = input('would you like to filter the data by Month, Day, Both or None? ').lower()

    months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun']   
    if time == 'month' or time == 'both':
        month = input('Which Month: Jan, Feb, Mar, Apr, May or Jun? ').lower()
        while month not in months:
            print('Wrong selection, try again')
            month = input('which month: Jan, Feb, Mar, Apr, May or Jun? ').lower()
    else:
        month = 'all'         

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    if time == 'day' or time == 'both':
        day = input('Which Day: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday? ').title()
        while day not in days:
            print('Wrong selection, try again')
            day = input('Which Day: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday? ').title()
    else:
        day = 'all'        

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city], parse_dates = ['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    if month != 'all':
        months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun' ]
    month = df['month'].mode()[0]
    print(f'the most common month is: {months[month-1]}')
    # TO DO: display the most common day of week
    day = df['day_of_week'].mode()[0]
    print(f'the most commen day is: {day}')

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode( [0])
    print(f'the most common hour is: {common_hour}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print(f'the most commonly used start station is: {common_start_station}')

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print(f'the most commonly used end station is: {common_end_station}')

    # TO DO: display most frequent combination of start station and end station trip
    common_trip = df['Start Station'] + ' to ' + df['End Station']
    print(f'the most frequent combination of start & end station trip is: {common_trip.mode()[0]}')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time =  (df['Trip Duration']).sum()
    minutes = total_travel_time // 60
    hours = minutes // 60
    print(f'total travel time is: {hours} hours') 
    # TO DO: display mean travel time
    avg_travel_time = (df['Trip Duration']).mean()
    minutes = avg_travel_time // 60
    hours = minutes // 60
    print(f'Avg travel time is: {hours} hours or {minutes} minutes')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print(df['User Type'].value_counts())
    print('\n\n')

    # TO DO: Display counts of gender
    if 'Gender' in (df.columns):
        print(df['Gender'].value_counts())
        print('\n\n')

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in (df.columns):
        earliest = df['Birth Year'].min()
        print(f'earliest year is: {earliest:.0f}')
        recent = df['Birth Year'].max()
        print(f'most recent year is: {recent:.0f}')
        common_birth = df['Birth Year'].mode()[0]
        print(f'most common year is: {common_birth:.0f}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):

    print(df.head())
    next = 0
    while True:
        view_raw_data = input('\nwould you like to view next five row of row data? ( yes / no )')
        if view_raw_data.lower() != 'yes':
            return
        next = next + 5
        print(df.iloc[next:next+5])

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? ( yes / no )\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
