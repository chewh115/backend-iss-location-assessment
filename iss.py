#!/usr/bin/env python

"""This module seeks to find out information about the ISS, including who's
    currently on board, where it is on a map,
    and when it will next pass Indianapolis"""

__author__ = 'chewh115, with Indy latitude help from Janell and Kano'

import requests
import time
import turtle


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
    return latitude, longitude


def show_on_map(coordinates):
    """Draws the location of ISS on a map"""
    world_map = turtle.Screen()
    world_map.setup(width=720, height=360)
    world_map.bgpic('map.gif')
    world_map.setworldcoordinates(-180, -90, 180, 90)
    world_map.register_shape('iss.gif')
    iss_station = turtle.Turtle()
    iss_station.shape('iss.gif')
    iss_station.penup()
    iss_station.goto(float(coordinates[1]), float(coordinates[0]))
    over_indy(world_map)
    world_map.exitonclick()
    return world_map


def over_indy(turtle_screen):
    lat = 39.7684
    lon = -86.1581
    indy_pass = requests.get(
        f'http://api.open-notify.org/iss-pass.json?lat={lat}&lon={lon}&n=1')
    pass_time = time.ctime(indy_pass.json()['response'][0]['risetime'])
    indy_pass = turtle.Turtle()
    indy_pass.penup()
    indy_pass.shape('circle')
    indy_pass.color('yellow')
    indy_pass.goto(lon, lat)
    indy_pass.write(pass_time, align='right', font=20)


def main():
    get_names_of_astros()
    coordinates = get_iss_coordinates()
    show_on_map(coordinates)


if __name__ == '__main__':
    main()
