#!/usr/bin/env python

__author__ = 'chewh115'

import requests
import time


def get_names_of_astros():
    """Gets list of astronauts currently in space, the spacecraft they're on,
    and how many astronauts are in space from website data and prints info"""
    astronaut_info = requests.get('http://api.open-notify.org/astros.json')
    astronauts = astronaut_info.json()
    for astro in astronauts['people']:
        print('{} is currently on the {}'.format(
            astro['name'], astro['craft']))
    print('There are currently {} astronauts in the cosmos.'.format(
        len(astronauts['people'])))


def get_iss_coordinates():
    """Gets current location of the ISS and timestamp that
    information was accessed from website data and prints info"""
    location_info = requests.get(
        'http://api.open-notify.org/iss-now.json').json()
    longitude = location_info['iss_position']['longitude']
    latitude = location_info['iss_position']['latitude']
    timestamp = location_info['timestamp']
    timestamp = time.ctime(timestamp)
    print('As of {}, the ISS\'s longitude is {}, and latitude is {}'.format(
        timestamp, longitude, latitude))


def main():
    get_names_of_astros()
    get_iss_coordinates()


if __name__ == '__main__':
    main()
