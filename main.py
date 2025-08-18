import matplotlib.pyplot as plt
import simulator
import reporting



data1 = (9, 13, 80, 1.85 , 100, 0)
data2 = (7.68, 10.51, 74, 1.84 , 100, 0) #Jara
data3 = (7.65, 10.36, 74, 1.84 , 100, 0)
data4 = (7.65, 10.22, 84, 1.84 , 100, 0) #Strasky
data5 = (7.85, 10.36, 84, 1.84 , 100, 0)
data6 = (6.69, 9.33, 66, 1.84 , 100, 0) #Salcmanova
data7 = (6.78, 8.69, 66, 1.84 , 100, 0)
data8 = (6.56, 9.43, 71, 1.78 , 100, 0) #Splechtnova
data0 = (8, 11, 84, 1.84 , 100, 200) #Něco odhad


reporting.segment_report(*data4)
print('\n')

reporting.max_speed_report(*data4)
print('\n')

#reporting.plot_trial_v_distance(*data4)
print('\n')

#reporting.fastest_f_v_report(*data4)
print('\n')

#reporting.plot_fastest_f_v(*data4)
print('\n')






#python main.py