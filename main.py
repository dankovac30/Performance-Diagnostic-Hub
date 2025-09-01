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

profile = [F0, V0, weight, height, running_distance, external_force]

# saved profiles
jara1 = [7.68, 10.51, 74, 1.84 , 100, 0] # 9.99
jara2 = [7.65, 10.36, 74, 1.84 , 100, 0] # 9.86
strasky1 = [7.65, 10.22, 84, 1.84 , 100, 0] # 9.78
strasky2 = [7.85, 10.36, 84, 1.84 , 100, 0] # 9.91
salcmanova1 = [6.69, 9.33, 66, 1.84 , 100, 0] # 8.88
salcmanova2 = [7.07, 9.05, 66, 1.84 , 100, 0] # 8.65
salcmanova3 = [6.78, 8.69, 66, 1.84 , 100, 0] # 8.33
salcmanova4 = [6.79, 8.79, 66, 1.84 , 100, 0] # 8.42
splechtnova1 = [6.57, 9.45, 71, 1.78 , 100, 0] # 9.01
splechtnova2 = [6.56, 9.43, 71, 1.78 , 100, 0] # 8.99
vanek1 = [7.23, 10.63, 85, 1.95, 100, 0] # 10.08
vanek2 = [7.15, 10.68, 85, 1.95, 100, 0] # 10.12
tlaskal1 = [7.64, 10.15, 68.7, 1.68, 100, 0] #9.68
tlaskal2 = [7.75, 10.41, 68.7, 1.68, 100, 0] #9.92
tlaskal3 = [9, 10.41, 68.7, 1.68, 100, 0] #9.92


test = [8.5, 11, 85, 1.85 , 100, 0]

#profile picker
profile = test


#reporting.segment_report(*profile)

#print('\n')
#reporting.top_speed_report(*profile)

#print('\n')
#reporting.plot_trial_v_distance(*profile)

#print('\n')
#reporting.fastest_f_v_report(*profile)

#print('\n')
#reporting.plot_fastest_f_v(*profile)

#print('\n')
#reporting.calibration(*profile, nonlinearity=0.837)


#reporting.plot_add_trial_to_v_distance('jara1', *jara1)
#reporting.plot_add_trial_to_v_distance('jara2', *jara2)
#plt.show()

#reporting.flying_sections_report(30, *profile)

reporting.complete_report(*profile)

#print(simulator.nonlinearity_finder(9.92, *profile))

#reporting.overspeed_zones_report(9.91, *profile)




#python main.py
 

