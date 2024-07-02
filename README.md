# Animals Web Generator

This project generates an HTML file with information about animals fetched from an API. It allows users to enter the name of an animal, view available skin types for the animal, and filter animals by their skin type.

## Project Description

The Animals Web Generator is a tool designed to fetch and display information about various animals. By utilizing an API, it retrieves detailed data about animals, including their names, locations, diets, and types. The project helps users learn more about different animals and their characteristics.

## Installation

To install this project, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/alexkummerer/animals-web-generator.git
    ```
2. Navigate to the project directory:
    ```bash
    cd animals-web-generator
    ```
3. Create a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
4. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

To use this project, follow these steps:

1. Ensure you have your API key. Create a `.env` file in the root directory of the project and add your API key:
    ```env
    API_KEY=your_api_key_here
    ```
2. Create an HTML template file named `animals_template.html` in the root directory with the placeholder `__REPLACE_ANIMALS_INFO__` where the animal information should be inserted.

3. Run the script:
    ```bash
    python animals_web_generator.py
    ```
4. Follow the prompts to enter an animal name and select a skin type.
5. The script will generate an `animals.html` file with the relevant animal information.

## Contributing

We welcome contributions! If you'd like to contribute to this project, please follow these guidelines:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new Pull Request.

## License

This project is licensed under the MIT License.

## Contact

If you have any questions or suggestions, please feel free to contact me at [developer@alexkummerer.de].

By including this README.md file, you make it easier for others to understand and use your project. It acts as a user manual, helping people get started quickly.
