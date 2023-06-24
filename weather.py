import csv
from datetime import datetime


DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celcius."
    """
    return f"{temp}{DEGREE_SYBMOL}"


def convert_date(iso_string):
    """Converts and ISO formatted date into a human readable format.

    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    
    dt = datetime.fromisoformat(iso_string)
    my_date= dt.strftime('%A %d %B %Y')
    return my_date


def convert_f_to_c(temp_in_farenheit):
    """Converts an temperature from farenheit to celcius.

    Args:
        temp_in_farenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees celcius, rounded to 1dp.
    """
    farenheit_number= float(temp_in_farenheit)
    temp_in_celsius  = (farenheit_number - 32) * .5556
    temp_in_celsius = round(temp_in_celsius , 1)
    return  temp_in_celsius 



def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    data_number=[]
    for number in weather_data:
        number=float(number)
        data_number.append(number)

    sum_data = sum(data_number)
    length_data = len( data_number)
    mean_weather_data= sum_data/length_data
    return mean_weather_data


def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    with open (csv_file, encoding="utf-8") as my_file:
        csv_reader = csv.reader(my_file)
        next(csv_reader)
        weather_data=[]
        for line in csv_reader:
            if len(line)>0:
                weather_data.append([line[0],int(line[1]), int(line[2]) ])
        return weather_data


def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minium value and it's position in the list.
    """
    if(weather_data == []):
        return ()
    data_number=[]
    for number in weather_data:
        number=float(number)
        data_number.append(number)
    min_number = min(data_number)
    res = [i for i,val in enumerate(data_number) if val==min_number]
    min_index=res[-1]
    return min_number, min_index


def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list.
    """
    if(weather_data == []):
        return ()
    data_numbers=[]
    for number in weather_data:
        number=float(number)
        data_numbers.append(number)
    max_number = max(data_numbers)
    res = [i for i,val in enumerate(data_numbers) if max_number ==val]
    max_index=res[-1]
    return max_number, max_index


def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    """Outputs a summary for the given weather data.
    """

    data_length= len(weather_data)

########### TEMPERATURE ##########################
    min_numbers = []
    for number in weather_data:
        min_numbers.append(number[1])
    min_temp, min_index= find_min(min_numbers)
    final_min_temp= convert_f_to_c(min_temp)
    
    date_min_list=[]
    for number in weather_data:
        date_min_list.append(number[0])
    index_temp = date_min_list[min_index]
    print(index_temp)
    final_date_min= convert_date(index_temp)


    max_numbers = []
    for number in weather_data:
        max_numbers.append(number[2])
    max_temp, max_index= find_max(max_numbers)
    final_max_temp= convert_f_to_c(max_temp)
    
    date_max_list=[]
    for number in weather_data:
        date_max_list.append(number[0])
    index_temp = date_max_list[max_index]
    print(index_temp)
    final_date_max= convert_date(index_temp)

########### AVERAGE ##########################
    min_average = []
    for number in weather_data:
        min_average.append(number[1])
    min_avg= calculate_mean(min_average)
    final_avg= convert_f_to_c(min_avg)

    max_average = []
    for number in weather_data:
        max_average.append(number[2])
    max_avg= calculate_mean(max_average)
    final_avg_max= convert_f_to_c(max_avg)


    return (
        f"{data_length} Day Overview\n"
        f"  The lowest temperature will be {final_min_temp}{DEGREE_SYBMOL}, and will occur on {final_date_min}.\n"
        f"  The highest temperature will be {final_max_temp}{DEGREE_SYBMOL}, and will occur on {final_date_max}.\n"
        f"  The average low this week is {final_avg}{DEGREE_SYBMOL}.\n"
        f"  The average high this week is {final_avg_max}{DEGREE_SYBMOL}.\n"
    )



def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    summary = ""
    for row in weather_data:
        date = row[0]
        min = row[1]
        max = row[2]

        summary+= f"---- {convert_date(date)} ----\n"
        summary+= f"  Minimum Temperature: {format_temperature(convert_f_to_c(min))}\n"
        summary+= f"  Maximum Temperature: {format_temperature(convert_f_to_c(max))}\n\n"

    return summary
