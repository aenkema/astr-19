class FavoriteAnimal:
    
    def __init__(self, animal_name, animal_arms, animal_legs, animal_eyes, animal_tail, animal_fur):
        self.name=str(animal_name)
        self.arms=float(animal_arms)
        self.legs=float(animal_legs)
        self.eyes=int(animal_eyes)
        self.tail=bool(animal_tail)
        self.fur=bool(animal_fur)
        
animalinfo = FavoriteAnimal(animal_name='Giant Phantom Jelly', animal_arms=10, animal_legs=10, animal_eyes=0, animal_tail=False, animal_fur=False)

print("My favorite animal is the", animalinfo.name, type(animalinfo.name))
print("The length of its arms and legs in meters is", animalinfo.arms, type(animalinfo.arms))
print("The length of its arms and legs in meters is", animalinfo.legs, type(animalinfo.legs))
print("The amount of eyes it has is", animalinfo.eyes, type(animalinfo.eyes))
print("Does it have fur?", animalinfo.fur, type(animalinfo.fur))
print("Does it have a tail?", animalinfo.tail, type(animalinfo.tail))