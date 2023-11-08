'''
Author: Bryce Woodland
'''

import math

def main():

    names = ['#1 Picnic', '#1 Tall', '#2', '#2.5', '#3 Cylinder', 
        '#5', '#6Z', '#8Z short', '#10', '#211', '#300', '#303'
        ]

    radiuses = [6.83, 7.78, 8.73, 10.32, 10.79, 13.02, 5.40, 
          6.83, 15.72, 6.83, 7.62, 8.10
        ]

    heights = [10.16, 11.91, 11.59, 11.91, 17.78, 14.29, 
          8.89, 7.62, 17.78, 12.38, 11.27, 11.11
        ]

    costs = [0.28, 0.43, 0.45, 0.61, 0.86, 0.83, 
        0.22, 0.26, 1.53, 0.34, 0.38, 0.42
        ]
    
    for i in range(len(names)):
        name = names[i]
        radius = radiuses[i]
        height = heights[i]
        cost = costs[i]
    

    # Prints the results for the: #1 Picnic
    # name = '#1 Picnic'
    # radius = 6.83
    # height = 10.16
    # cost = 0.28
    # volume = compute_volume(radius, height)
    # surface_area = compute_surface_area(radius, height)
        storage_efficiency = compute_storage_efficiency(radius, height)
        cost_efficiency = compute_cost_efficiency(radius, height, cost)

        print(f'{name} {storage_efficiency:.2f} {cost_efficiency:.0f}')

    # # Prints the results for the: #1 Tall 
    # name = '#1 Tall'
    # radius = 7.78
    # height = 11.91
    # cost = 0.43
    # volume = compute_volume(radius, height)
    # surface_area = compute_surface_area(radius, height)
    # storage_efficiency = compute_storage_efficiency(volume, surface_area)
    # cost_efficiency = compute_cost_efficiency(volume, cost)

    # print(f'{name} {storage_efficiency:.2f} {cost_efficiency:.2f}')

    # # Prints the results for the: #2
    # name = '#2'
    # radius = 8.73
    # height = 11.59
    # cost = 0.45
    # volume = compute_volume(radius, height)
    # surface_area = compute_surface_area(radius, height)
    # storage_efficiency = compute_storage_efficiency(volume, surface_area)
    # cost_efficiency = compute_cost_efficiency(volume, cost)

    # print(f'{name} {storage_efficiency:.2f} {cost_efficiency:.2f}')

    # # Prints the results for the: #2.5
    # name = '#2.5'
    # radius = 10.32
    # height = 11.91
    # cost = 0.61
    # volume = compute_volume(radius, height)
    # surface_area = compute_surface_area(radius, height)
    # storage_efficiency = compute_storage_efficiency(volume, surface_area)
    # cost_efficiency = compute_cost_efficiency(volume, cost)

    # print(f'{name} {storage_efficiency:.2f} {cost_efficiency:.2f}')

    # # Prints the results for the: #3 Cylinder
    # name = '#3 Cylinder'
    # radius = 10.79
    # height = 17.78
    # cost = 0.86
    # volume = compute_volume(radius, height)
    # surface_area = compute_surface_area(radius, height)
    # storage_efficiency = compute_storage_efficiency(volume, surface_area)
    # cost_efficiency = compute_cost_efficiency(volume, cost)

    # print(f'{name} {storage_efficiency:.2f} {cost_efficiency:.2f}')

    # # Prints the results for the: #5 
    # name = '#5'
    # radius = 13.02
    # height = 14.29
    # cost = 0.83
    # volume = compute_volume(radius, height)
    # surface_area = compute_surface_area(radius, height)
    # storage_efficiency = compute_storage_efficiency(volume, surface_area)
    # cost_efficiency = compute_cost_efficiency(volume, cost)

    # print(f'{name} {storage_efficiency:.2f} {cost_efficiency:.2f}')

    # # Prints the results for the: #6Z
    # name = '#6Z'
    # radius = 5.40
    # height = 8.89
    # cost = 0.22
    # volume = compute_volume(radius, height)
    # surface_area = compute_surface_area(radius, height)
    # storage_efficiency = compute_storage_efficiency(volume, surface_area)
    # cost_efficiency = compute_cost_efficiency(volume, cost)

    # print(f'{name} {storage_efficiency:.2f} {cost_efficiency:.2f}')

    # # Prints the results for the: #8Z 
    # name = '#8Z short'
    # radius = 6.83
    # height = 7.62
    # cost = 0.26
    # volume = compute_volume(radius, height)
    # surface_area = compute_surface_area(radius, height)
    # storage_efficiency = compute_storage_efficiency(volume, surface_area)
    # cost_efficiency = compute_cost_efficiency(volume, cost)

    # print(f'{name} {storage_efficiency:.2f} {cost_efficiency:.2f}')

    # # Prints the results for the: #10
    # name = '#10'
    # radius = 15.72
    # height = 17.78
    # cost = 1.53
    # volume = compute_volume(radius, height)
    # surface_area = compute_surface_area(radius, height)
    # storage_efficiency = compute_storage_efficiency(volume, surface_area)
    # cost_efficiency = compute_cost_efficiency(volume, cost)

    # print(f'{name} {storage_efficiency:.2f} {cost_efficiency:.2f}')

    # # Prints the results for the: #211 
    # name = '#211'
    # radius = 6.83
    # height = 12.38
    # cost = 0.34
    # volume = compute_volume(radius, height)
    # surface_area = compute_surface_area(radius, height)
    # storage_efficiency = compute_storage_efficiency(volume, surface_area)
    # cost_efficiency = compute_cost_efficiency(volume, cost)

    # print(f'{name} {storage_efficiency:.2f} {cost_efficiency:.2f}')

    # # Prints the results for the: #300 
    # name = '#300'
    # radius = 7.62
    # height = 11.27
    # cost = 0.38
    # volume = compute_volume(radius, height)
    # surface_area = compute_surface_area(radius, height)
    # storage_efficiency = compute_storage_efficiency(volume, surface_area)
    # cost_efficiency = compute_cost_efficiency(volume, cost)

    # print(f'{name} {storage_efficiency:.2f} {cost_efficiency:.2f}')

    # # Prints the results for the: #1 Picnic 
    # name = '#303'
    # radius = 8.10
    # height = 11.11
    # cost = 0.42
    # volume = compute_volume(radius, height)
    # surface_area = compute_surface_area(radius, height)
    # storage_efficiency = compute_storage_efficiency(volume, surface_area)
    # cost_efficiency = compute_cost_efficiency(volume, cost)

    # print(f'{name} {storage_efficiency:.2f} {cost_efficiency:.2f}')

def compute_volume(radius, height):
    '''Compute and display the volume of a cylinder
    
    Parameters
        Radius (float): the radius of the cylinder
        Height (int|float): the height of the cylinder
    Return (float): the volume of the cylinder '''
    
    volume = math.pi * radius ** 2 * height

    return volume

def compute_surface_area(radius, height):
    '''Compute and display the surface area of a cylinder
     
    Parameters
        Radius (float): the radius of the cylinder
        Height (int|float): the height of the cylinder
    Return (float): the surface area of the cylinder '''
    
    surface_area = 2 * math.pi * radius * (radius + height)

    return surface_area

def compute_storage_efficiency(volume, surface_area):
    '''Compute and display the storage efficency
    
    Parameters
        volume (float): the volume of the can
        surface area (float): the surface area of the can
    Return (float): the storage efficency of the can
    '''

    storage_efficiency = volume / surface_area

    return storage_efficiency

def compute_cost_efficiency(radius, height, cost):
    '''Compute and display the cost efficiency
    
    Parameters
        volume (float): the volume of the can
        cost (float): the cost of the can
    Return (float): the cost efficiency of the can
    '''
    volume = math.pi * radius ** 2 * height
    cost_efficiency = volume / cost

    return cost_efficiency

main()
