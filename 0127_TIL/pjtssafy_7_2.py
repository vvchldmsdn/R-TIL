class Doggy:
    num_of_dogs = 0
    birth_of_dogs = 0

    def __init__(self, name, dog_type):
        self.name = name
        self.dog_type = dog_type
        Doggy.num_of_dogs += 1
        Doggy.birth_of_dogs += 1

    def bark(self):
        return f'왈왈!'

    def __del__(self):
        Doggy.num_of_dogs -= 1

    @staticmethod
    def get_status():
        return f'Birth: {Doggy.birth_of_dogs}, Current: {Doggy.num_of_dogs}'
