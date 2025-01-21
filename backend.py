import matplotlib.pyplot as plt
import numpy as np

def calculate(u0,theta,g):
    # Time of flight
    t = (2*u0*np.sin(np.deg2rad(theta)))/g

    # Maximum height
    h = (u0**2*(np.sin(np.deg2rad(theta)))**2)/(2*g)

    # Range
    R = (u0**2*np.sin(2*np.deg2rad(theta)))/g

    # Time array
    t_array = np.linspace(0, t, 100)

    # Distance array
    distance = u0*np.cos(np.deg2rad(theta))*t_array

    # Height array
    height = u0*np.sin(np.deg2rad(theta))*t_array - (0.5*g*t_array**2)

    # Plot the graph
    plt.plot(distance, height)
    plt.xlabel('Distance (m)')
    plt.ylabel('Height (m)')
    plt.title('Projectile Motion Graph')

    # Annotate the graph with a line
    plt.annotate(f'Range = {R:.2f} m\nMaximum Height = {h:.2f} m\nTime of Flight = {t:.2f} s',
                xy=(R/2, h/2), xycoords='data',
                xytext=(30, 30), textcoords='offset points',
                arrowprops=dict(arrowstyle="->",
                                connectionstyle="arc3,rad=.2"))

    # Display the graph
    plt.savefig("output.jpg")

    return [R,h,t]
