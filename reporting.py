import matplotlib.pyplot as plt
import simulator

def segment_report(F0, V0, weight, height, running_distance, external_force_N=0):

    data = simulator.simulate_sprint(F0, V0, weight, height, running_distance, external_force_N)

    segments = simulator.segments(data)

    for segment in segments:
        print(f"Čas na {segment['distance']:.0f} m: {segment['total_time']:.2f} | Čas segmentu: {segment['segment_time']:.2f}")


def top_speed_report(F0, V0, weight, height, running_distance, external_force_N=0):

    data = simulator.simulate_sprint(F0, V0, weight, height, running_distance, external_force_N)

    top_speed = simulator.top_speed(data)

    print(f'Maximální rychlost: {top_speed['top_speed']:.2f} m/s')
    print(f'Vzdálenost: {top_speed['distance_top_speed']:.1f} m')


def fastest_f_v_report(F0, V0, weight, height, running_distance, external_force_N=0):

    data = simulator.f_v_profile_comparison(F0, V0, weight, height, running_distance, external_force_N)

    fastest_f_v = min(data, key= lambda record: record['time'])

    print(f'Vzdálenost: {running_distance} m')
    print(f'Optimální sklon: {fastest_f_v['f_v_slope']:.2f}')
    print(f'Čas: {fastest_f_v['time']:.2f}')
    print(f'F0: {fastest_f_v['F0']:.2f}')
    print(f'V0: {fastest_f_v['V0']:.2f}')


def calibration(F0, V0, weight, height, running_distance, external_force_N):

    data = simulator.simulate_sprint(F0, V0, weight, height, 100, 0)

    boudaries = [2.5, 5, 10, 20, 30, 40]
    boundary_index = 0

    for i, time in enumerate(data['time']):

        if boundary_index >= len(boudaries):
            break

        current_boundary = boudaries[boundary_index]
        
        if data['distance'][i] >= current_boundary:

            print(f'{time:.2f}')

            boundary_index += 1
    

def plot_trial_v_distance(F0, V0, weight, height, running_distance, external_force_N=0):

    data = simulator.simulate_sprint(F0, V0, weight, height, running_distance, external_force_N)

    plt.figure(figsize=(10, 6))
    plt.plot(data['distance'], data['speed'])
    plt.xlabel('Distance')
    plt.ylabel('Speed')
    plt.grid(True)
    plt.show() 


def plot_fastest_f_v(F0, V0, weight, height, running_distance, external_force_N=0):

    data = simulator.f_v_profile_comparison(F0, V0, weight, height, running_distance, external_force_N)

    f_v_slope_list = [record['f_v_slope'] for record in data]
    time_list = [record['time'] for record in data]

    plt.figure(figsize=(10, 6))
    plt.plot(f_v_slope_list, time_list)
    plt.xlabel('F/V Slope')
    plt.ylabel('Time')
    plt.grid(True)
    plt.show() 


def plot_add_trial_to_v_distance(name, F0, V0, weight, height, running_distance, external_force_N=0):
    
    data = simulator.simulate_sprint(F0, V0, weight, height, running_distance, external_force_N)

    plt.plot(data['distance'], data['speed'], label=name)
    plt.xlabel('distance')
    plt.ylabel('speed')
    plt.grid(True)


def flying_sections(fly_length, F0, V0, weight, height, running_distance, external_force_N=0):

    if fly_length > running_distance:
        
        print("Error: Letmý úsek je delší než celková délka úseku")
    
    else:

        data = simulator.simulate_sprint(F0, V0, weight, height, running_distance, external_force_N)

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

    print(f'Absolutně nejrychlejší úsek (na tisíciny): {fly_length} m za {fastest_time:.3f} s mezi {fastest_start_m:.1f} - {fastest_finish_m:.1f} m')
    print(f'První úsek s nejlepším časem (na setiny): {fly_length} m za {fastest_time_rounded} s mezi {fastest_start_m_rounded} - {fastest_finish_m_rounded} m')




