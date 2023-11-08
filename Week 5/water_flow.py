"""
Author: Bryce Woodland

Write a Python program that could help an engineer design a 
water distribution system. During this prove milestone, you will 
write three program functions and three test functions as described 
in the Steps section below.
"""
WATER_DENSITY = 998.2
GRAVITY = 9.80665

def water_column_height(tower_height, tank_height):
    """Compute and return the water column height by solving
    the equation: 
        height = tower_height + (3 * tank_height) / 4
    
    Parameters 
        Tower height: is the height of the water tower
        tank height: is the height of just the tank
    Return: the final height of the water column
    """
    height_column = tower_height + (3 * tank_height) / 4

    return height_column

def pressure_gain_from_water_height(height):
    """Compute and return the pressure gain from the following
     equation: 
        pressure = WATER_DENSITY * GRAVITY * height / 1000
    
    Parameters 
        height: height of the water column in meters
    Return: the pressure from the water
    """
    pressure = (WATER_DENSITY * GRAVITY * height) / 1000

    return pressure

def pressure_loss_from_pipe(pipe_diameter,
        pipe_length, friction_factor, fluid_velocity):
    """Compute and return the pressure loss from the pipe 
    by using the equation: 
        pressure = -friction_factor * pipe_length * WATER_DENSITY * fluid_velocity ** 2 / 2000 * pipe_diameter
         
    Parameters
        pipe_diameter: the diameter of the pipe
        pipe_length: the length of the pipe
        friction_factor: the pipe's friction factor
        fluid_velocity: the velocity of the water flowing through the pipe in meters / second
    Return: the pressure loss from friction within a pipe.   
    """
    pressure_loss = (-friction_factor * pipe_length * WATER_DENSITY * (fluid_velocity ** 2)) / (2000 * pipe_diameter)

    return pressure_loss