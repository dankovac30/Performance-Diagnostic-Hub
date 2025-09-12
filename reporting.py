import matplotlib.pyplot as plt
import simulator
import time


def complete_report(data):
    
    original_fly_length = data.fly_length

    data.fly_length = 30

    report = data.run_sprint()

    running_time = report['time'][-1]

    top_speed = data.top_speed()

    fly_segment = data.flying_sections()

    data.fly_length = original_fly_length

    fly_time = str(f'{fly_segment['fastest']['time']:.2f} s')
    fly_start = str(f'{fly_segment['fastest']['start']:.0f}')
    fly_finish = str(f'{fly_segment['fastest']['finish']:.0f} m')
        
    time_30_m = 0

    for index in range(len(report['distance'])):
        
        if report['distance'][index] > 30:
            time_30_m = report['time'][index]
            break

    p_max = data.F0 * data.V0 / 4
    sfv = data.F0 / data.V0


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
        f'- F0: {data.F0} N/kg, V0: {data.V0}',
        f'- Hmotnost: {data.weight} kg, Výška: {data.height} cm',
        f'- Běžená vzdálenost: {data.running_distance} m',
        f'- Externí odpor: {data.external_force_N} N',
        '\n',
        '--- KLÍČOVÉ UKAZATELE VÝKONU ---',
        f'Celkový čas na {data.running_distance}m: {running_time:.2f}',
        '\n',
        '--- ČASOVÁ ANALÝZA VÝKONU ---',
        f'Čas na 30m (akcelerace): {time_30_m:.2f} s',
        f'Čas ma 30m (letmý úsek): {fly_time}',
        f'Ve vzdálenosti {fly_start} - {fly_finish}',        
        f'Maximální rychlost: {top_speed['top_speed']:.2f} m/s',
        f'Dosaženo ve vzdálenosti: {top_speed['distance_top_speed']:.1f} m',
        '\n',
        '--- BIOMECHANICKÝ PROFIL ---',
        f'Maximální výkon (Pmax): {p_max:.2f} W/kg ({(p_max * data.weight):.0f} W)',
        f'F-V Sklon (Sfv): {sfv:.2f}',
        '\n',
        '==================================================',
        'Nyní bude zobrazen graf průběhu rychlosti...',
        '\n',
    ]

    slow_print(report_text)
    

    plt.figure(figsize=(10, 6))
    plt.plot(report['distance'], report['speed'], label='Graf rychlosti a vzdálenosti')
    plt.xlabel('Vzdálenost')
    plt.ylabel('Rychlost')
    plt.grid(True)
    plt.show() 


def segment_report(data):

    segments = data.segments()

    for segment in segments:
        print(f"Čas na {segment['distance']:.0f} m: {segment['total_time']:.2f} | Čas segmentu: {segment['segment_time']:.2f}")


def top_speed_report(data):

    top_speed = data.top_speed()

    print(f'Maximální rychlost: {top_speed['top_speed']:.2f} m/s')
    print(f'Vzdálenost: {top_speed['distance_top_speed']:.1f} m')


def fastest_f_v_report(data):

    report = data.f_v_profile_comparison()

    fastest_f_v = min(report, key= lambda record: record['time'])

    print(f'Vzdálenost: {data.running_distance} m')
    print(f'Optimální sklon: {fastest_f_v['f_v_slope']:.2f}')
    print(f'Čas: {fastest_f_v['time']:.2f}')
    print(f'F0: {fastest_f_v['F0']:.2f}')
    print(f'V0: {fastest_f_v['V0']:.2f}')


def calibration(data):

    report = data.run_sprint()

    boudaries = [2.5, 5, 10, 20, 30]
    boundary_index = 0

    for i, time in enumerate(report['time']):

        if boundary_index >= len(boudaries):
            break

        current_boundary = boudaries[boundary_index]
        
        if report['distance'][i] >= current_boundary:

            print(f'{time:.2f}')

            boundary_index += 1
    

def plot_trial_v_distance(data):

    report = data.run_sprint()

    plt.figure(figsize=(10, 6))
    plt.plot(report['distance'], report['speed'])
    plt.xlabel('Distance')
    plt.ylabel('Speed')
    plt.grid(True)
    plt.show() 


def plot_fastest_f_v(data):

    report = data.f_v_profile_comparison()

    f_v_slope_list = [record['f_v_slope'] for record in report]
    time_list = [record['time'] for record in report]

    plt.figure(figsize=(10, 6))
    plt.plot(f_v_slope_list, time_list)
    plt.xlabel('F/V Slope')
    plt.ylabel('Time')
    plt.grid(True)
    plt.show() 


def plot_add_trial_to_v_distance(data):
    
    report = data.run_sprint()

    plt.plot(report['distance'], report['speed'])
    plt.xlabel('distance')
    plt.ylabel('speed')
    plt.grid(True)


def flying_sections_report(data):

    report = data.flying_sections()

    if type(report) == str:
        print(report)

    else:
        print(f'Absolutně nejrychlejší úsek (na tisíciny): {data.fly_length} m za {report['fastest']['time']:.3f} s mezi {report['fastest']['start']:.1f} - {report['fastest']['finish']:.1f} m')
        print(f'První úsek s nejlepším časem (na setiny): {data.fly_length} m za {report['first_fast']['time']} s mezi {report['first_fast']['start']} - {report['first_fast']['finish']} m')


def overspeed_zones_report(data):

    report = data.overspeed_zones()

    for record in report:
        
        print(f'Relativní rychlost: {record['speed_percent']}   Absolutní rychlost: {record['top_speed']:.2f} m/s   Externí síla: {record['external_force']:.0f} N')

