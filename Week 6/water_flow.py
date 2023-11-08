"""
Author: Bryce Woodland

Write a Python program that could help an engineer design a 
water distribution system. During this prove milestone, you will 
write three program functions and three test functions as described 
in the Steps section below.
"""
WATER_DENSITY = 998.2
GRAVITY = 9.80665
WATER_DYNAMIC_VISCOSITY = 0.0010016

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
    pressure_loss_from_pipe = (-friction_factor * pipe_length * WATER_DENSITY * (fluid_velocity ** 2)) / (2000 * pipe_diameter)

    return pressure_loss_from_pipe

def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
    """Compute and return the pressure loss from fittings
    by using the equation: 
        pressure = -0.04 * WATER_DENSITY * fluid_velocity ** 2 * quantity_fittings / 2000
         
    Parameters
        fluid_velocity: is the velocity of the water flowing through the pipe in meters / second
        quantity_fittings: is the quantity of fittings
    Return: pressure loss from pipe fittings.   
    """
    pressure_loss_from_fittings = -0.04 * WATER_DENSITY * fluid_velocity ** 2 * quantity_fittings / 2000

    return pressure_loss_from_fittings

def reynolds_number(hydraulic_diameter, fluid_velocity):
    """Compute and return the reynolds number
    by using the equation: 
        reynolds_number = WATER_DENSITY * hydraulic_diameter * fluid_velocity / 0.0010016
         
    Parameters
        hydraulic_diameter: diameter of a pipe in meters. For a round pipe, the hydraulic diameter is the same as the pipe’s inner diameter.
        fluid_velocity: is the velocity of the water flowing through the pipe in meters / second
    Return: calculates the Reynolds number .   
    """
    reynolds_number = WATER_DENSITY * hydraulic_diameter * fluid_velocity / WATER_DYNAMIC_VISCOSITY

    return reynolds_number

def pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number, smaller_diameter):
    """Compute and return the pressure loss from pipe reduction
    by using the two equations:
        constant = (0.1 + 50 / reynolds_number) * ((larger_diameter / smaller_diameter) ** 4 - 1) 

        pressure_loss_from_pipe_reduction = (-constant * WATER_DENSITY * velocity ** 2) / 2000
        
         
    Parameters
        reynolds_number: is the Reynolds number that corresponds to the pipe with the larger diameter
        larger_diameter: is the diameter of the larger pipe in meters
        smaller_diameter is the diameter of the smaller pipe in meters
         is the lost pressure kilopascals
        fluid_velocity is the velocity of the water flowing through the larger diameter pipe in meters / second  
    Return: the pressure lost from pipe reduction   
    """
    constant = (0.1 + 50 / reynolds_number) * ((larger_diameter / smaller_diameter) ** 4 - 1)
    pressure_loss_from_pipe_reduction = (-constant * WATER_DENSITY * fluid_velocity ** 2) / 2000

    return pressure_loss_from_pipe_reduction

def convert_kilopascals_to_pounds_per_square_inch(pressure):
    """Compute and return the kilopascals to pounds per square inch
    by using the equation: 
        psi = kilopascals * 0.145038
         
    Parameters
        pressure: take the kilopascals and convert it into pounds per square inch
    Return: the psi from kilopascals
    """
    pounds_per_square_inch = pressure * 0.1450377377

    return pounds_per_square_inch

PVC_SCHED80_INNER_DIAMETER = 0.28687 # (meters)  11.294 inches
PVC_SCHED80_FRICTION_FACTOR = 0.013  # (unitless)
SUPPLY_VELOCITY = 1.65               # (meters / second)

HDPE_SDR11_INNER_DIAMETER = 0.048692 # (meters)  1.917 inches
HDPE_SDR11_FRICTION_FACTOR = 0.018   # (unitless)
HOUSEHOLD_VELOCITY = 1.75            # (meters / second)


def main():
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    length1 = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles = int(input("Number of 90° angles in supply pipe: "))
    length2 = float(input("Length of pipe from supply to house (meters): "))

    water_height = water_column_height(tower_height, tank_height)
    pressure = pressure_gain_from_water_height(water_height)
    

    diameter = PVC_SCHED80_INNER_DIAMETER
    friction = PVC_SCHED80_FRICTION_FACTOR
    velocity = SUPPLY_VELOCITY
    reynolds = reynolds_number(diameter, velocity)
    loss = pressure_loss_from_pipe(diameter, length1, friction, velocity)
    pressure += loss

    loss = pressure_loss_from_fittings(velocity, quantity_angles)
    pressure += loss

    loss = pressure_loss_from_pipe_reduction(diameter,
            velocity, reynolds, HDPE_SDR11_INNER_DIAMETER)
    pressure += loss

    diameter = HDPE_SDR11_INNER_DIAMETER
    friction = HDPE_SDR11_FRICTION_FACTOR
    velocity = HOUSEHOLD_VELOCITY
    loss = pressure_loss_from_pipe(diameter, length2, friction, velocity)
    pressure += loss

    print(f"Pressure at house: {pressure:.1f} kilopascals")

    psi = convert_kilopascals_to_pounds_per_square_inch(pressure)
    print(f"The pressure in psi: {psi:.2f}")

if __name__ == "__main__":
    main()