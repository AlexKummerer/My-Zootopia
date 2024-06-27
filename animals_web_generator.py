import json

def load_data(file_path):
    """Loads a JSON file"""
    with open(file_path, 'r') as handle :
        return json.load(handle)


def print_animal_information(animal):
    """Check and print animal information"""
    if 'name' in animal:
        print('\nName:', animal['name'])
    
    if 'characteristics' in animal:
        characteristics = animal['characteristics']
        if 'diet' in characteristics:
            print('Diet:', characteristics['diet'])
        if 'type' in characteristics:
            print('Type:', characteristics['type'])
    
    if 'locations' in animal and animal['locations']:
        print('Location:', animal['locations'][0])


def print_animals_data(animals_data):
    """print all animals information"""
    
    for animal in animals_data:
        print(animal)
        print_animal_information(animal)


def main():
    animals_data = load_data("animals_data.json")

    print_animals_data(animals_data)


if __name__ == '__main__':
    main()