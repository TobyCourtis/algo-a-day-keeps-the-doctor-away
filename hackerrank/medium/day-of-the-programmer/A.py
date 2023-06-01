#!/bin/python3

import os

#
# Complete the 'dayOfProgrammer' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
#

days_in_month = {
    'January': 31,
    'February': 28,  # 29 during leap year, 28 all other years
    'March': 31,
    'April': 30,
    'May': 31,
    'June': 30,
    'July': 31,
    'August': 31,
    'September': 30,
    'October': 31,
    'November': 30,
    'December': 31
}

keys_list = list(days_in_month.keys())


def findDevDayGivenDictionary(days_in_month_dict):
    day = 0
    for month, day_count in days_in_month.items():
        if day + day_count >= 256:
            return (month, 256 - day)
        day += day_count
    return None


def generateDateUsingDict(dict_in):
    out_tuple = findDevDayGivenDictionary(dict_in)
    month_out = keys_list.index(out_tuple[0]) + 1
    if month_out < 10:
        month_out = f"0{month_out}"
    day_out = out_tuple[1]
    return f"{day_out}.{month_out}.{year}"


def dayOfProgrammer(year):
    if year < 1918:
        if year % 4 == 0:
            adjusted_days_in_month = days_in_month
            adjusted_days_in_month['February'] = 29
        else:
            adjusted_days_in_month = days_in_month
            
        return generateDateUsingDict(adjusted_days_in_month)
    elif year == 1918:
        adjusted_days_in_month = days_in_month
        adjusted_days_in_month['February'] = 14

        return generateDateUsingDict(adjusted_days_in_month)
    else:
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            adjusted_days_in_month = days_in_month
            adjusted_days_in_month['February'] = 29
        else:
            adjusted_days_in_month = days_in_month
            
        return generateDateUsingDict(adjusted_days_in_month)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
