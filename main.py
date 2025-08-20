import matplotlib.pyplot as plt
import reporting


F0 = 9
V0 = 13
weight = 80
height = 1.85
running_distance = 100
external_load = 0

profile = [F0, V0, weight, height, running_distance, external_load]

# saved profiles
jara1 = [7.68, 10.51, 74, 1.84 , 100, 0]
jara2 = [7.65, 10.36, 74, 1.84 , 100, 0]
strasky1 = [7.65, 10.22, 84, 1.84 , 100, 0]
strasky2 = [7.85, 10.36, 84, 1.84 , 100, 0]
salcmanova1 = [6.69, 9.33, 66, 1.84 , 100, 0]
salcmanova2 = [6.78, 8.69, 66, 1.84 , 100, 0]
splechtnova1 = [6.56, 9.43, 71, 1.78 , 100, 0]
test = [8, 11, 84, 1.84 , 100, 200]


#reporting.segment_report(*jara1)

#print('\n')
#reporting.top_speed_report(*jara1)

#print('\n')
#reporting.plot_trial_v_distance(*jara1)

#print('\n')
#reporting.fastest_f_v_report(*jara1)

#print('\n')
#reporting.plot_fastest_f_v(*jara1)

#print('\n')
#reporting.calibration(*strasky1)


#reporting.plot_add_trial_to_v_distance('jara1', *jara1)
#reporting.plot_add_trial_to_v_distance('jara2', *jara2)
#plt.show()

#reporting.flying_sections_report(30, *jara1)

reporting.complete_report(*jara1)

#python main.py
 

