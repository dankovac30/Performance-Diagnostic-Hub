import math
import matplotlib.pyplot as plt


def simulate_sprint(F0, V0, weight, height, running_distance, external_force_N=0, nonlinearity=0.86):
    
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


def flying_sections(fly_length, F0, V0, weight, height, running_distance, external_force_N=0):
    
    if fly_length > 60:
        
        return "Nejdelší podporovaný letmý úsek je 60m"
    
    elif running_distance < 100:

        return "Pro výpočet letmého úseku zadejte délku běhu alespoň 100m"

    else:

        data = simulate_sprint(F0, V0, weight, height, running_distance, external_force_N)

        fastest_time = float('inf')
        fastest_start_m = 0
        fastest_finish_m = 0

        fastest_time_rounded = float('inf')
        fastest_start_m_rounded = 0
        fastest_finish_m_rounded = 0


        time_list = data['time']
        distance_list = data['distance']
        number_of_records = len(time_list)

        loop_marker = 0

        for start_index in range(number_of_records):
            
            start_m = distance_list[start_index]
            finish_m = start_m + fly_length

            for finish_index in range(loop_marker, number_of_records):

                if distance_list[finish_index] >= finish_m:
                    
                    finish_m = distance_list[finish_index]
                    real_segment_distance = finish_m - start_m

                    start_time = time_list[start_index]
                    finish_time = time_list[finish_index]
                    segment_time = ((finish_time - start_time) / real_segment_distance) * fly_length
                    segment_time_rounded = round(segment_time, 2)

                    if segment_time < fastest_time:
                        fastest_time = segment_time
                        fastest_start_m = start_m
                        fastest_finish_m = start_m + fly_length

                    if segment_time_rounded < fastest_time_rounded:
                        fastest_time_rounded = segment_time_rounded
                        fastest_start_m_rounded = round(start_m, 0)
                        fastest_finish_m_rounded = fastest_start_m_rounded + fly_length

                    loop_marker = finish_index
                    break
                    
        fly_report = {
            'fastest': {
                'time': fastest_time,
                'start': fastest_start_m,
                'finish': fastest_finish_m
            },
            'first_fast': {
                'time': fastest_time_rounded,
                'start': fastest_start_m_rounded,
                'finish': fastest_finish_m_rounded
            }
        }

    return fly_report


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
    

def nonlinearity_finder(unloaded_speed, F0, V0, weight, height, running_distance, external_force_N=0):

    nonlinearity = 0
    external_force_N = 0

    for i in range(750, 950):
        
        nonlinearity_loop = i / 1000

        data = simulate_sprint(F0, V0, weight, height, 100, external_force_N, nonlinearity_loop)

        speed_loop = top_speed(data)
        
        if round(unloaded_speed, 2) == round(speed_loop['top_speed'], 2):
            nonlinearity = nonlinearity_loop
    
    return nonlinearity


def overspeed_zones(unloaded_speed, F0, V0, weight, height, running_distance, external_force_N=0):

    external_force_N = 0

    nonlinearity = nonlinearity_finder(unloaded_speed, F0, V0, weight, height, running_distance, 0)

    overspeed_zones = []

    for i in range(1, 81):

        external_force_N = -i

        data = simulate_sprint(F0, V0, weight, height, 100, external_force_N, nonlinearity)

        max_speed = top_speed(data)['top_speed']
        speed_gain = max_speed / unloaded_speed

        overspeed_zones.append({
            'external_force_N': external_force_N,
            'top_speed': max_speed,
            'speed_gain': speed_gain
        })
    
    speed_percent = 1.01
    speed_percent_list = []

    for record in overspeed_zones:
        
        if speed_percent > 1.10:
            break

        if record['top_speed'] > speed_percent * unloaded_speed:

            speed_percent_list.append({
                'speed_percent': f'{(((speed_percent - 1) * 100) + 100):.0f} %',
                'external_force': record['external_force_N'],
                'top_speed': record['top_speed']
            })
        
            speed_percent += 0.01

    test = []
    predchozi_zaznam = 0
        
    return speed_percent_list