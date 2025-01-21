# Projectile-Motion

This project is a graphical user interface (GUI) application built with Python and Tkinter. It allows users to visualize and calculate the motion of a projectile based on initial velocity, launch angle, and gravitational acceleration. The simulation displays key parameters such as range, flight time, and maximum height. Additionally, the corresponding trajectory graph is dynamically updated and displayed.

Features
User Input Fields: Enter initial velocity (v₀), launch angle, and gravitational acceleration (g).
Dynamic Calculations: Computes the projectile's range, maximum height, and total flight time using a backend module (backend.py).
Graphical Display: Updates the trajectory graph dynamically and displays it within the GUI.
Logo and Interface Design: Includes a logo and intuitive layout for enhanced user experience.

Requirements
Python 3.x
Required Python Libraries:
tkinter
Pillow (for image processing)
backend.py file for projectile motion calculations.

How to Use
Clone the repository and ensure all necessary files (e.g., backend.py, sakeclogo.jpg, output_start.png) are in the same directory.

Install the required Python libraries if not already installed:

pip install pillow

Run the application:
python <script_name>.py
Fill in the form with the initial velocity, angle, and gravitational acceleration.
Click on the RESULT button to compute the projectile motion parameters and update the graph.
Files in the Project

<script_name>.py: The main GUI application script.
backend.py: A helper module to perform projectile motion calculations.
sakeclogo.jpg: The logo displayed in the GUI.
output_start.png: The default graph displayed on startup.
output.jpg: The dynamically updated graph after computations.

Output
Range: Displays the horizontal distance traveled by the projectile.
Flight Time: Shows the total time the projectile stays in motion.
Max Height: Indicates the highest point reached by the projectile.
