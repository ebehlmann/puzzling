import csv
import math


def calculate_fuel_for_mass(mass):
    return math.floor(mass / 3) - 2


def calculate_fuel_for_mass_plus_fuel(mass):
    fuel = calculate_fuel_for_mass(mass)
    currently_calculating = fuel
    while True:
        extra = calculate_fuel_for_mass(currently_calculating)
        if extra <= 0:
            break
        fuel = fuel + extra
        currently_calculating = extra
    return fuel


def calculate_total_fuel(input_file):
    total = 0
    with open('input.csv', encoding="utf-8-sig") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            total = total + calculate_fuel_for_mass_plus_fuel(int(row[0]))
    return total


print(calculate_total_fuel('input.csv'))
