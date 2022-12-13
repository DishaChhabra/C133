# import pandas as pd
import csv
import plotly.express as px
# data = pd.read_csv('Classes/c131/main.csv')

rows = []

with open("Classes/c131/main.csv" , "r") as f:
    a = csv.reader(f)
    for i in a:
        rows.append(i)

headers = rows[0]
print(headers)


planet_data_rows = rows[1:]
print(planet_data_rows[0])


headers[0] = "row_num"

# ------------------------------------------------------------------------------------------

solar_system_planet_count = {}
for i in planet_data_rows:
    if solar_system_planet_count.get(i[11]):
        solar_system_planet_count[i[11]] += 1
    else:
        solar_system_planet_count[i[11]] = 1
    
# solar_system_planet_count = {
#     "ss1" : 10,
#     "ss2" : 12
# }

# solar_system_planet_count["ss2"] --> 12

max_solar_system = max(solar_system_planet_count, key=solar_system_planet_count.get)

print("---------------------------------------------------------------------")
print("Solar System- " , max_solar_system  , " has maximun planets of " , solar_system_planet_count[max_solar_system] )

# ------------------------------------------------------------------------------------------

temp_planet_data_rows = list(planet_data_rows)
for a in temp_planet_data_rows:
    planet_mass = a[3]
    
    if planet_mass.lower() == "unknown":
        planet_data_rows.remove(a)
        continue
    
    else:
        value = planet_mass.split(" ")[0]
        ref = planet_mass.split(" ")[1]
        if ref == "Jupiters":
            value = float(value) * 317.8

        a[3] = value

    planet_radius = a[7]

    if planet_radius.lower() == 'unknown':
        planet_data_rows.remove(a)
        continue
    else:
        value = planet_radius.split(" ")[0]
        ref = planet_radius.split(" ")[2]
        if ref == 'Jupiter':
            value = float(value) * 11.2

        a[7] = value

print("----------------------------------")
print(len(planet_data_rows))


hd_10180_planets = []
for i in planet_data_rows:
    if max_solar_system == i[11]:
        hd_10180_planets.append(i)


print("----------------------------------")
print(len(hd_10180_planets))

print("----------------------------------")
print(hd_10180_planets)

# ["19.4 Jupiters"].split(" ") --> [19.4 , Jupiters]

# ["1.08 x Jupiter"].split(" ") --> [1.08 , x , Jupiter]

# ------------------------------------------------------------------------------------------

hd_mass = []
hd_names = []
for i in hd_10180_planets:
    hd_mass.append(i[3])
    hd_names.append(i[1])

hd_mass.append(1)
hd_names.append('Earth')

fig = px.bar(x=hd_names, y=hd_mass)
# fig.show()

# ------------------------------------------------------------------------------------------

temp_planet_data_rows = list(planet_data_rows)

for i in temp_planet_data_rows:
    
    if i[1].lower() == "hd 100546 b":
        planet_data_rows.remove(i)

planet_mass = []
planet_names = []
planet_radius = []

for i in planet_data_rows:
    planet_mass.append(i[3])
    planet_names.append(i[1])  
    planet_radius.append(i[7])

planet_gravity = []

for i,n in enumerate(planet_names):
    gravity = (float(planet_mass[i])*5.972e+24) / (float(planet_radius[i])*float(planet_radius[i])*6371000*6371000) * 6.674e-11
    planet_gravity.append(gravity)

fig = px.scatter(x = planet_radius, y=planet_mass, size=planet_gravity)
# fig.show()


low_g_planets = []
for i,g in enumerate(planet_gravity):
    if g < 100:
        low_g_planets.append(planet_data_rows[i])


print("----------------------------------")
print(len(low_g_planets))


# -------------------------------------------------- C 132 -----------------------------------------------------------------------------

planet_type = []
for i in planet_data_rows:
    planet_type.append(i[6])

print("--------------------------------------")
print(list(set(planet_type)))

# Neptune-like => These planets are like neptune! They are big in size and have rings around them. They are also made of Ice.

# Super-Earth => These are the planets that have mass greater than earth but smaller than that of Neptune! (Neptune is 17 times Earth)

# Terrestrial => It is a planet that is composed primarily of silicate rocks or metals (Like Earth, Mars)

# Gas Giant => There are the planets that are composed of Gas (Hydrogen and Helium)



planet_mass = []
planet_radius = []
planet_types = []

for i in low_g_planets:
    planet_mass.append(i[3])
    planet_radius.append(i[7])
    planet_types.append(i[6])

fig = px.scatter(x = planet_radius, y=planet_mass , color = planet_types)
# fig.show()


suitable_planets = []
for i in low_g_planets:
    if i[6].lower() == 'terrestrial'  or i[6].lower() == 'super earth':
        suitable_planets.append(i)

print("--------------------------------------")
print(len(suitable_planets))

#------------------------------------------------C 133------------------

print(headers)

temp = list(suitable_planets)
for i in temp:
    if i[8].lower() == 'unknown':
        suitable_planets.remove(i)
for i in suitable_planets:
    if i[9].split(" ")[1].lower() == 'days':
        i[9] = float(i[9].split(" ")[0])
    else:
        i[9] = float(i[9].split(" ")[0])*365
    i[8] = float(i[8].split(" ")[0])

orb_radius = []
orb_period = []

for i in suitable_planets:
    orb_radius.append(i[8])
    orb_period.append(i[9])

figure = px.scatter(x=orb_radius, y=orb_period)
#figure.show()

au_planets = list(suitable_planets)
temp = list(suitable_planets)

for i in temp:
    if i[8] < 0.38 or i[8] > 2:
        au_planets.remove(i)

print('----------------------------')
print(len(suitable_planets))
print(len(au_planets))

planet_speed = []
for i in suitable_planets:
    dist = 2* 3.14 * i[8]*1.496e+8 #circumference -> 2pir, converting distance from light year to km
    time = i[9]*86400 # to seconds
    speed = dist/time
    planet_speed.append(speed)

supporting_planets = list(suitable_planets)
for a,b in enumerate(supporting_planets):
    if planet_speed[a] > 200:
        supporting_planets.remove(b)

print(len(supporting_planets))
