#VARIABLES
destinations = ['Paris, France', 'Shanghai, China', 'Los Angeles, USA', 'São Paulo, Brazil', 'Cairo, Egypt']

attractions = [ [], [], [], [], [] ]

#0=name, 1=current location, 2=interests
test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

#FUNCTIONS
def get_destination_index(destination):
  for index in range(len(destinations)):
    if destinations[index] == destination:
      return index
  return -1

def get_traveler_location(traveler):
  traveler_destination = traveler[1]
  traveler_destination_index = get_destination_index(traveler_destination)
  return traveler_destination_index

def add_attraction(destination, attraction):
  try:
    destination_index = get_destination_index(destination)
  except ValueError:
    print("Destination doesn't exist!")
    return
  attractions_for_destination = attractions[destination_index]
  attractions_for_destination.append(attraction)
  return

def find_attractions(destination, interests):
  try:
    destination_index = get_destination_index(destination)
  except ValueError:
    print("Destination doesn't exist!")
    return
  attractions_in_city = attractions[destination_index]
  attractions_with_interest = []
  for attraction in attractions_in_city:
    possible_attraction = attraction
    attraction_tags = attraction[1]
    for interest in interests:
      if interest in attraction_tags:
        attractions_with_interest.append(possible_attraction[0])
  return attractions_with_interest
    
def get_attractions_for_traveler(traveler):
  traveler_destination = traveler[1]
  traveler_interests = traveler[2]
  traveler_attractions = find_attractions(traveler_destination, traveler_interests)
  interests_string = 'Hi ' + traveler[0] + ', we think you\'ll like these places around ' + traveler[1] + ':' 
  modified_traveler_attractions = ['the ' + name for name in traveler_attractions]
  for i in range(len(modified_traveler_attractions)):
    if(i < len(modified_traveler_attractions)-1):
      interests_string += modified_traveler_attractions[i] + ', '
    else:
      interests_string += modified_traveler_attractions[i] + '.'
  return interests_string
  
#DATA
add_attraction('Los Angeles, USA', ['Venice Beach', ['beach']])
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historcical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])

#TESTING
# print(get_destination_index('Los Angeles, USA'))
# print(get_destination_index('Paris, France'))
# test_destination_index = get_traveler_location(test_traveler)
# print(test_destination_index)
# print(attractions)
# print(find_attractions('Los Angeles, USA', ['art']))
# print(get_attractions_for_traveler(['Dereck Smill', 'Paris, France', ['monument']]))
