Molecule Simulation
Overview

This Python project uses Pygame to simulate and visualize the movement and interaction of molecules. The simulation features molecules represented as colored circles that bounce off the window edges and collide with each other. It provides a simple yet effective demonstration of basic physics principles in a graphical context.
Features

    Dynamic Movement: Molecules move with random velocities and bounce off the window boundaries.
    Collision Detection: Molecules interact with each other based on basic collision physics, altering their velocities upon impact.
    Customizable: Easy to adjust parameters such as the number of molecules and their properties.

Installation

To run the simulation on your local machine, follow these steps:
Clone the Repository:

git clone https://github.com/your-username/your-repo.git

Navigate to the Project Directory:
cd your-repo

Install Dependencies:
Make sure you have Python installed, then install the required Pygame library:
pip install pygame

Run the Simulation:
Execute the main script to start the simulation:
    python main.py

How It Works

    Molecule Class: Defines the properties and behaviors of each molecule, including position, velocity, and collision handling.
    Physics: Implements simple physics for boundary collisions and interactions between molecules.
    Rendering: Uses Pygame to continuously render the simulation on the screen and update the display.

Key Components

    Molecule Class: Handles molecule properties and methods for updating position and drawing on the screen.
    generate_molecules Function: Generates a list of molecules with random initial properties.
    Main Loop: Handles event processing, updates molecule states, and renders the scene.

Contributions are welcome! If you have suggestions for improvements or find any issues, please:

    Fork the repository.
    Create a new branch for your changes.
    Submit a pull request with a description of your modifications.

License

This project is licensed under the MIT License. See the LICENSE file for details.
Contact

For any questions or feedback, please reach out to renardyassine1@gmail.com.
