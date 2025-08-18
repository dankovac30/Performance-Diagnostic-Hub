import math
import matplotlib.pyplot as plt


def simulate_sprint(F0, V0, weight, height, running_distance, external_force_N=0):
    
    # initial state
    time = 0
    speed = 0
    covered_distance = 0
    original_V0 = V0
    fatigie_active = False     

    # minimum time increment  
    dt = 0.001

    # air resistance constants
    rho = 1.204
    Cd = 0.89
    A = 0.2025 * (height ** 0.725) * (weight ** 0.425)

    # nonlinearity
    nonlinearity = 0.86    

    # others
    lane = 6
    bend_diameter = 35.28 + 1.22 * lane
    f_v_inclination = F0 / V0
    
    #return
    time_list = []
    distance_list = []
    speed_list = []
    acceleration_list = []


    while covered_distance < running_distance:

        # propulsive force
        actual_incline = (F0/V0) * (1 - (1 - nonlinearity) * (speed/V0))
        f_propulsion = (F0 - actual_incline * speed) * weight
        f_propulsion = max(0, f_propulsion)

        # bend resistance
        if running_distance > 100 and covered_distance < (running_distance - 84.39):
            f_bend = 0.1 * (weight * speed**2) / bend_diameter

        else:
            f_bend = 0

        # air resistance
        f_resistance = 0.5 * rho * A * Cd * (speed ** 2)

        # resultant propulsive force
        f_resultant = f_propulsion - f_resistance - f_bend - external_force_N
        
        # acceleration
        acceleration = f_resultant / weight

        if acceleration < 0.05 and not fatigie_active:
            fatigie_active = True

        if fatigie_active:
            V0 -= (original_V0 / 51) * dt
            F0 = V0 * f_v_inclination

        # return
        time_list.append(time)
        distance_list.append(covered_distance)
        speed_list.append(speed)
        acceleration_list.append(acceleration)
        
   
        # update
        covered_distance += (speed * dt)
        speed += (acceleration * dt)
        speed = max(0.01, speed)
        time += dt
        
        # debug
        #print(f"Time: {cas:.2f}s | Distance: {covered_distance:.2f}m | Speed: {speed:.2f}m/s | Acceleration: {acceleration:.2f}m/s²")

    report = {
        'time': time_list,
        'distance': distance_list,
        'speed': speed_list,
        'acceleration': acceleration_list
    }

    return report


def top_speed(data):
    top_speed = max(data['speed'])
    index_top_speed = data['speed'].index(top_speed)
    distance_top_speed = data['distance'][index_top_speed]
    report = {
        'top_speed': top_speed,
        'distance_top_speed': distance_top_speed
    }

    return report


def segments(data):
    boundary = 10
    previous_time = 0
    segment_list = []
        
    for i, time in enumerate(data['time']):
        if data['distance'][i] >= boundary:

            segment_time = time - previous_time

            segment = {
                'distance': boundary,
                'total_time': time,
                'segment_time': segment_time
            }

            segment_list.append(segment)
            boundary += 10
            previous_time = time

    segment_list.append({'distance': data['distance'][-1], 'total_time': data['time'][-1], 'segment_time': data['time'][-1] - previous_time})

    return segment_list


def f_v_profile_comparison(F0, V0, weight, height, running_distance, external_force_N=0):
    max_power = (F0 * V0) / 4
    
    f_v_slopes_resuls = []

    f_v_slopes_range = []
    min_value = 0.1
    max_value = 2.00
    f_v_slope_increment = 0.01

    while min_value <= max_value:
        f_v_slopes_range.append(min_value)
        min_value += f_v_slope_increment

    for value in f_v_slopes_range:
        V0 = math.sqrt((4*max_power)/value)
        F0 = V0 * value

        data = simulate_sprint(F0, V0, weight, height, running_distance, external_force_N)

        current_f_v = {
            'f_v_slope': value,
            'time': data['time'][-1],
            'F0': F0,
            'V0': V0
        }

        f_v_slopes_resuls.append(current_f_v)


    return f_v_slopes_resuls
    




