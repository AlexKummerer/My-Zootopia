import json


def load_data(file_path):
    """Loads a JSON file"""
    with open(file_path, "r") as handle:
        return json.load(handle)


def read_template(template_path):
    """Read HTML template content"""
    with open(template_path, "r") as file:
        return file.read()


def write_html(file_path, content):
    """Write content to an HTML file"""
    with open(file_path, "w") as file:
        file.write(content)


def generate_animal_information(animal):
    """Generate animal information string"""
    info = ""
    info += '<li class="cards__item">'
    if "name" in animal:
        info += f"<div class='card__title'> {animal['name']}</div>\n"
    info += '<p class="card__text">'
    info += '<ul>'
    if "locations" in animal and animal["locations"]:
        info += f" <li> <strong> Location: </strong> {animal['locations'][0]}</li>\n"
    if "characteristics" in animal:
        characteristics = animal["characteristics"]
        if "diet" in characteristics:
            info += f" <li>  <strong> Diet: </strong> {characteristics['diet']}</li>\n"
        if "type" in characteristics:
            info += f" <li>  <strong>  Type: </strong>  {characteristics['type']}</li>\n"

  
    info += '</ul>'
    info+= "</p>"
    info += '</li>'
    return info


def generate_animals_data_string(animals_data):
    """Generate string with all animals information"""
    output = ""
    for animal in animals_data:
        output += generate_animal_information(animal)
    return output


def replace_placeholder(template_content, placeholder, replacement):
    """Replace placeholder in template with the given replacement"""
    return template_content.replace(placeholder, replacement)


def main():
    animals_data = load_data("animals_data.json")
    template_content = read_template("animals_template.html")

    animals_info_string = generate_animals_data_string(animals_data)
    updated_content = replace_placeholder(
        template_content, "__REPLACE_ANIMALS_INFO__", animals_info_string
    )

    write_html("animals.html", updated_content)
    print("New HTML content written to animals.html")


if __name__ == "__main__":
    main()
