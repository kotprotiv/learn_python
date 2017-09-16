import json

with open('lesson4/data-397-2017-09-06.json', 'r', encoding='windows 1251') as metro_data:
    parsed_json = json.load(metro_data)

    stations_with_repair = []
    for row in parsed_json:
        if len(row['RepairOfEscalators']) > 0:
            stations_with_repair.append(row['NameOfStation'])
            
    distinct_stations_list = []
    for station_name in stations_with_repair:
        if station_name not in distinct_stations_list:
            distinct_stations_list.append(station_name)

print(distinct_stations_list)