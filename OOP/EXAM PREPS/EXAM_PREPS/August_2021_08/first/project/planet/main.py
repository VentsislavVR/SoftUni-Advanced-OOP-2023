from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.space_station import SpaceStation

space_station = SpaceStation()

print(space_station.add_astronaut('Biologist','Pesho'))
print(space_station.add_astronaut('Meteorologist','Pesho1'))
print(space_station.add_astronaut('Geodesist','Pesho2'))


print(space_station.add_planet('Mars','item1, item2'))
print(space_station.send_on_mission('Mars'))

print(space_station.report())