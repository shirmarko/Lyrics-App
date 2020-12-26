from place import Place
class PlacesCreator:
    def __init__(self):
        pass

    def filter_ignore_places(self, places):
        ignore_places = ["Born", "Fighting", "Beach", "River", "America", "USA Born", "City", "Parkway", "Island", "Place",
                        "Sound","Children", "Then", "Like", "World", "Pigs", "Sunset", "Red China", "Third World",
                        "Whisky Bar", "Bar Smiles", "Road"]
        filtered_places = []
        for place in places:
            if not ignore_places.__contains__(place):
                filtered_places.append(place)
        return filtered_places

    
    def create_places_list(self, places, extracted_places, song):
        extracted_places = self.filter_ignore_places(extracted_places) # ignore words that are not places
        for new_place_name in extracted_places:
            exists = False
            for place in places:
                if place.name == new_place_name:
                    place.add_song(song) 
                    exists = True
                    break
            if not exists: # the place was not handled
                p = Place(new_place_name, [])
                p.find_coordinates()
                if p.latitude != 0 or p.longitude != 0:
                    p.add_song(song)
                    places.append(p)
        return places

    