#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self,name="Bark",breed="Mastiff"):
        self.name = name
        self.breed = breed

    def get_name(self):
        return self._name
    
    def set_name(self,new_name):
        if type(new_name) == str and len(new_name) > 1 and len(new_name) < 25:
            self._name = new_name
        else:
            print("Name must be string between 1 and 25 characters.")
    
    def get_breed(self):
        return self._breed
    
    def set_breed(self,new_breed):
        if APPROVED_BREEDS.count(new_breed) > 0:
            self._breed = new_breed
        else:
            print("Breed must be in list of approved breeds.")
    
    name = property(get_name,set_name)
    breed = property(get_breed,set_breed)

fido = Dog("namehere","Mastiff")
print(fido)