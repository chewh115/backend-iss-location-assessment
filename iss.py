#!/usr/bin/env python

__author__ = 'chewh115'

import requests


def get_names_of_astros():
    """Gets list of astronauts currently in space, the spacecraft they're on,
    and how many astronauts are in space from website data"""
    r = requests.get('http://api.open-notify.org/astros.json')
    astronauts = r.json()
    for astro in astronauts['people']:
        print('{} is currently on the {}'.format(
            astro['name'], astro['craft']))
    print('There are currently {} astronauts in the cosmos.'.format(
        len(astronauts['people'])))


def main():
    get_names_of_astros()


if __name__ == '__main__':
    main()
