import matplotlib.pyplot as plt
import simulator
import time


def complete_report(F0, V0, weight, height, running_distance, external_force_N=0):

    data = simulator.simulate_sprint(F0, V0, weight, height, running_distance, external_force_N)

    running_time = data['time'][-1]
    top_speed = simulator.top_speed(data)

    fly_segment = simulator.flying_sections(30, F0, V0, weight, height, running_distance, external_force_N)

    if type(fly_segment) == str:
        fly_time = 'Délka běhu musí být alespoň 100m'
        fly_start = 'N/A'
        fly_finish = 'N/A'

    else:
        fly_time = str(f'{fly_segment['fastest']['time']:.2f} s')
        fly_start = str(f'{fly_segment['fastest']['start']:.0f}')
        fly_finish = str(f'{fly_segment['fastest']['finish']:.0f} m')
        
    time_30_m = 0

    for index in range(len(data['distance'])):
        
        if data['distance'][index] > 30:
            time_30_m = data['time'][index]
            break

    p_max = F0 * V0 / 4
    sfv = F0 / V0


    def slow_print(report_lines, delay=0.07):

        for line in report_lines:
            print(line)
            time.sleep(delay)
    
    report_text = [
        '\n',
        '==================================================',
        ' ==      REPORT VÝKONNOSTNÍ DIAGNOSTIKY        ==',
        '==================================================',
        '\n',
        '--- VSTUPNÍ PARAMETRY SIMULACE ---',
        f'- F0: {F0} N/kg, V0: {V0}',
        f'- Hmotnost: {weight} kg, Výška: {height} cm',
        f'- Běžená vzdálenost: {running_distance} m',
        f'- Externí odpor: {external_force_N} N',
        '\n',
        '--- KLÍČOVÉ UKAZATELE VÝKONU ---',
        f'Celkový čas na {running_distance}m: {running_time:.2f}',
        '\n',
        '--- ČASOVÁ ANALÝZA VÝKONU ---',
        f'Čas na 30m (akcelerace): {time_30_m:.2f} s',
        f'Čas ma 30m (letmý úsek): {fly_time}',
        f'Ve vzdálenosti {fly_start} - {fly_finish}',        
        f'Maximální rychlost: {top_speed['top_speed']:.2f} m/s',
        f'Dosaženo ve vzdálenosti: {top_speed['distance_top_speed']:.1f} m',
        '\n',
        '--- BIOMECHANICKÝ PROFIL ---',
        f'Maximální výkon (Pmax): {p_max:.2f} W/kg ({(p_max * weight):.0f} W)',
        f'F-V Sklon (Sfv): {sfv:.2f}',
        '\n',
        '==================================================',
        'Nyní bude zobrazen graf průběhu rychlosti...',
        '\n',
    ]

    slow_print(report_text)
    

    plt.figure(figsize=(10, 6))
    plt.plot(data['distance'], data['speed'], label='Graf rychlosti a vzdálenosti')
    plt.xlabel('Vzdálenost')
    plt.ylabel('Rychlost')
    plt.grid(True)
    plt.show() 


def segment_report(F0, V0, weight, height, running_distance, external_force_N=0):

    data = simulator.simulate_sprint(F0, V0, weight, height, running_distance, external_force_N)

    segments = simulator.segments(data)

    for segment in segments:
        print(f"Čas na {segment['distance']:.0f} m: {segment['total_time']:.2f} | Čas segmentu: {segment['segment_time']:.2f}")


def top_speed_report(F0, V0, weight, height, running_distance, external_force_N=0, nonlinearity=0.86):

    data = simulator.simulate_sprint(F0, V0, weight, height, running_distance, external_force_N, nonlinearity)

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


def calibration(F0, V0, weight, height, running_distance, external_force_N, nonlinearity=0.86):

    data = simulator.simulate_sprint(F0, V0, weight, height, 100, 0, nonlinearity)

    boudaries = [2.5, 5, 10, 20, 30]
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


def flying_sections_report(fly_length, F0, V0, weight, height, running_distance, external_force_N=0):

    data = simulator.flying_sections(fly_length, F0, V0, weight, height, running_distance, external_force_N)

    if type(data) == str:
        print(data)

    else:
        print(f'Absolutně nejrychlejší úsek (na tisíciny): {fly_length} m za {data['fastest']['time']:.3f} s mezi {data['fastest']['start']:.1f} - {data['fastest']['finish']:.1f} m')
        print(f'První úsek s nejlepším časem (na setiny): {fly_length} m za {data['first_fast']['time']} s mezi {data['first_fast']['start']} - {data['first_fast']['finish']} m')


def overspeed_zones_report(unloaded_speed, F0, V0, weight, height, running_distance, external_force_N=0):

    data = simulator.overspeed_zones(unloaded_speed, F0, V0, weight, height, running_distance, external_force_N)

    for record in data:
        
        print(f'Relativní rychlost: {record['speed_percent']}   Absolutní rychlost: {record['top_speed']:.2f} m/s   Externí síla: {record['external_force']:.0f} N')

