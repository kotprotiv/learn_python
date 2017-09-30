import csv
import json
import gpxpy.geo


with open('data-398-2017-09-14.csv', 'r', encoding='windows 1251') as csv_stop:
    reader = csv.reader(csv_stop)
    headers = next(reader)
    headers = headers[0].split(';')
    reader = csv.DictReader(csv_stop, headers, delimiter=';')
    bus_stop_coordinate = {}
    bus_stop_coordinate_list = []
    for row in reader:
        bus_stop_coordinate['name'] = row['"Name"']
        bus_stop_coordinate['longitude'] = row['"Longitude_WGS84"']
        bus_stop_coordinate['latitude'] = row['"Latitude_WGS84"']
        bus_stop_coordinate_list.append(bus_stop_coordinate)
        bus_stop_coordinate = {}

with open('data-397-2017-09-06.json', 'r', encoding='windows 1251') as metro_data:
    parsed_json = json.load(metro_data)

    metro_station_coordinate = {}
    metro_station_coordinate_list = []
    for row in parsed_json:
        metro_station_coordinate['name'] = row['NameOfStation']
        metro_station_coordinate['longitude'] = row['geoData']['coordinates'][0]
        metro_station_coordinate['latitude'] = row['geoData']['coordinates'][1]
        metro_station_coordinate_list.append(metro_station_coordinate)
        metro_station_coordinate = {}

all_by_all_list = []
distance_dict = {}
for bus_stop in bus_stop_coordinate_list:
    for metro_station in metro_station_coordinate_list:
        distance_dict['metro_station'] = metro_station['name']
        distance_dict['bus_stop'] = bus_stop['name']
        distance_dict['distance'] = gpxpy.geo.haversine_distance(
            float(bus_stop['latitude']), float(bus_stop['longitude']),
            float(metro_station['latitude']), float(metro_station['longitude'])
            )
        all_by_all_list.append(distance_dict)
        distance_dict = {}

final_list = []
for combination in all_by_all_list:
    if combination['distance'] <= 500:
        final_list.append(combination)

with open('final_data.csv', 'w', encoding='utf-8') as export_file:
    fields = ['metro_station', 'bus_stop', 'distance']
    writer = csv.DictWriter(export_file, fields, delimiter=';')
    writer.writeheader()
    writer.writerows(final_list)
