import matplotlib.pyplot as plt
import simulator

def segment_report(F0, V0, weight, height, running_distance, external_force_N=0):

    data = simulator.simulate_sprint(F0, V0, weight, height, running_distance, external_force_N)

    segments = simulator.segments(data)

    for segment in segments:
        print(f"Čas na {segment['distance']:.0f} m: {segment['total_time']:.2f} | Čas segmentu: {segment['segment_time']:.2f}")


def max_speed_report(F0, V0, weight, height, running_distance, external_force_N=0):

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


def calibration() 


def add_trial_to_speed_plot(data, name):
    plt.plot(data['distance'], data['speed'], label=name)