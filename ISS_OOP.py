
import urllib.request
import datetime
import json

''' Projects main idea was to practice how to implement and use object oriented programming style.
Code returns astronauts currently on board of International space station, crafts location and next five
pass times over Turku, Finland.'''

class Craft:

    def __init__(self, name):
        self.name = name

    # Get all astronauts on board
    def get_all_astros(self):

        r_astros = urllib.request.urlopen('http://api.open-notify.org/astros.json')
        astro_data = json.loads(r_astros.read())
        astronauts = []

        for astros in astro_data['people']:
            name = list(astros.values())[1]
            astronauts.append(name)

        return f'Astronauts currently on board of ISS: {astronauts}'

    # Gets Iss current location
    def get_iss_location(self):

        r_loc = urllib.request.urlopen('http://api.open-notify.org/iss-now.json')
        loc_data = json.loads(r_loc.read())
        location = loc_data['iss_position']

        return f'ISS current location is: {location}'

    # Gets next 5 pass times over Turku
    def get_passes_over_Turku(self):

        r_pass = urllib.request.urlopen(f'http://api.open-notify.org/iss-pass.json?lat=61&lon=22')
        pass_data = json.loads(r_pass.read())
        pass_times = []

        for risetime in pass_data['response']:
            rt = datetime.datetime.fromtimestamp(list(risetime.values())[1]).isoformat()
            pass_times.append(rt)

        return f'Next 5 ISS pass times over Turku: {pass_times}'


iss = Craft('ISS')
print(iss.get_all_astros())
print(iss.get_iss_location())
print(iss.get_passes_over_Turku())




