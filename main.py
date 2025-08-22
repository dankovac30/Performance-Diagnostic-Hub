import matplotlib.pyplot as plt
import simulator
import reporting


F0 = 8.5
V0 = 11.5
weight = 80
height = 1.85
running_distance = 100
external_force = -20
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
test = [8, 11, 84, 1.84 , 100, 200]

#profile picker
profile = jara1


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
#reporting.calibration(*profile)


#reporting.plot_add_trial_to_v_distance('jara1', *jara1)
#reporting.plot_add_trial_to_v_distance('jara2', *jara2)
#plt.show()

#reporting.flying_sections_report(30, *profile)

#reporting.complete_report(*profile)

print('Jára')
print(simulator.nonlinearity_finder(9.99, *jara1))
print(simulator.nonlinearity_finder(9.84, *jara2))
print('\n')
print('Stráský')
print(simulator.nonlinearity_finder(9.78, *strasky1))
print(simulator.nonlinearity_finder(9.91, *strasky2))
print('\n')
print('Salcmanová')
print(simulator.nonlinearity_finder(8.88, *salcmanova1))
print(simulator.nonlinearity_finder(8.65, *salcmanova2))
print(simulator.nonlinearity_finder(8.33, *salcmanova3))
print(simulator.nonlinearity_finder(8.42, *salcmanova4))
print('\n')
print('Šplechtnová')
print(simulator.nonlinearity_finder(9.01, *splechtnova1))
print(simulator.nonlinearity_finder(8.99, *splechtnova2))




#python main.py
 

