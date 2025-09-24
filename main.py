import matplotlib.pyplot as plt
import simulator
import reporting


F0 = 8.5
V0 = 11.5
weight = 80
height = 1.85
running_distance = 100
external_force = 0
unloaded_speed = 10.5
fly_length = 30

profile = {'F0': F0, 'V0': V0, 'weight': weight, 'height': height, 'running_distance': running_distance, 'external_force_N': external_force, 'unloaded_speed': unloaded_speed, 'fly_length': fly_length}

# saved profiles
jara1 = {'F0': 7.68, 'V0': 10.51, 'weight': 74, 'height': 1.84, 'running_distance': 100, 'external_force_N': 0, 'unloaded_speed': 9.99, 'fly_length': 30}
jara2 = {'F0': 7.65, 'V0': 10.36, 'weight': 74, 'height': 1.84, 'running_distance': 100, 'external_force_N': 0, 'unloaded_speed': 9.86, 'fly_length': 30}
strasky1 = {'F0': 7.65, 'V0': 10.22, 'weight': 84, 'height': 1.84, 'running_distance': 100, 'external_force_N': 0, 'unloaded_speed': 9.78, 'fly_length': 30}
strasky2 = {'F0': 7.85, 'V0': 10.36, 'weight': 84, 'height': 1.84, 'running_distance': 100, 'external_force_N': 0, 'unloaded_speed': 9.91, 'fly_length': 30}
salcmanova1 = {'F0': 6.69, 'V0': 9.33, 'weight': 66, 'height': 1.84, 'running_distance': 100, 'external_force_N': 0, 'unloaded_speed': 8.88, 'fly_length': 30}
salcmanova2 = {'F0': 7.07, 'V0': 9.05, 'weight': 66, 'height': 1.84, 'running_distance': 100, 'external_force_N': 0, 'unloaded_speed': 8.65, 'fly_length': 30}
salcmanova3 = {'F0': 6.78, 'V0': 8.69, 'weight': 66, 'height': 1.84, 'running_distance': 100, 'external_force_N': 0, 'unloaded_speed': 8.33, 'fly_length': 30}
salcmanova4 = {'F0': 6.79, 'V0': 8.79, 'weight': 66, 'height': 1.84, 'running_distance': 100, 'external_force_N': 0, 'unloaded_speed': 8.42, 'fly_length': 30}
splechtnova1 = {'F0': 6.57, 'V0': 9.45, 'weight': 71, 'height': 1.78, 'running_distance': 100, 'external_force_N': 0, 'unloaded_speed': 9.01, 'fly_length': 30}
splechtnova2 = {'F0': 6.56, 'V0': 9.43, 'weight': 71, 'height': 1.78, 'running_distance': 100, 'external_force_N': 0, 'unloaded_speed': 8.99, 'fly_length': 30}
vanek1 = {'F0': 7.23, 'V0': 10.63, 'weight': 85, 'height': 1.95, 'running_distance': 100, 'external_force_N': 0, 'unloaded_speed': 10.08, 'fly_length': 30}
vanek2 = {'F0': 7.15, 'V0': 10.68, 'weight': 85, 'height': 1.95, 'running_distance': 100, 'external_force_N': 0, 'unloaded_speed': 10.12, 'fly_length': 30}
tlaskal1 = {'F0': 7.64, 'V0': 10.15, 'weight': 68.7, 'height': 1.68, 'running_distance': 100, 'external_force_N': 0, 'unloaded_speed': 9.68, 'fly_length': 30}
tlaskal2 = {'F0': 7.75, 'V0': 10.41, 'weight': 68.7, 'height': 1.68, 'running_distance': 100, 'external_force_N': 0, 'unloaded_speed': 9.92, 'fly_length': 30}
tlaskal3 = {'F0': 7.68, 'V0': 10.51, 'weight': 74, 'height': 1.84, 'running_distance': 100, 'external_force_N': 0, 'unloaded_speed': 9.99, 'fly_length': 30}

test = {'F0': 8.34, 'V0': 12, 'weight': 85, 'height': 1.85, 'running_distance': 100, 'external_force_N': 0, 'unloaded_speed': None, 'fly_length': 30}


#profile picker
profile = jara1

analyza = simulator.SprintSimulation(**profile)

reporting.complete_report(analyza)

reporting.segment_report(analyza)

reporting.top_speed_report(analyza)

reporting.flying_sections_report(analyza)

reporting.overspeed_zones_report(analyza)

reporting.plot_add_trial_to_v_distance(analyza)
reporting.plot_trial_v_distance(analyza)

reporting.fastest_f_v_report(analyza)
reporting.plot_fastest_f_v(analyza)

reporting.calibration(analyza)









#python main.py