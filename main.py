import math
import matplotlib.pyplot as plt
import simulator


data1 = simulator.simulate_sprint(9, 13, 80, 1.85 , 100, 0)
data2 = simulator.simulate_sprint(7.68, 10.51, 74, 1.84 , 100, 0) #Jara
data3 = simulator.simulate_sprint(7.65, 10.36, 74, 1.84 , 100, 0)
data4 = simulator.simulate_sprint(7.65, 10.22, 84, 1.84 , 100, 0) #Strasky
data5 = simulator.simulate_sprint(7.85, 10.36, 84, 1.84 , 100, 0)
data6 = simulator.simulate_sprint(6.69, 9.33, 66, 1.84 , 100, 0) #Salcmanova
data7 = simulator.simulate_sprint(6.78, 8.69, 66, 1.84 , 100, 0)
data8 = simulator.simulate_sprint(6.56, 9.43, 71, 1.78 , 100, 0) #Splechtnova
data0 = simulator.simulate_sprint(8.5, 11, 84, 1.86 , 100, 0) #Něco odhad


vysledek = simulator.segments(data1)


for segment in vysledek:
    print(f"Čas na {segment['distance']:.0f} m: {segment['total_time']:.2f} | Čas segmentu: {segment['segment_time']:.2f}")


print('\n')


vysledek = simulator.top_speed(data1)

print(f'Maximální rychlost: {vysledek['top_speed']:.2f} m/s')
print(f'Vzdálenost: {vysledek['distance_top_speed']:.1f} m')


plt.figure(figsize=(10, 6))
plt.title('Srovnání průběhu rychlosti')
plt.xlabel('Vzdálenost (m)')
plt.ylabel('Rychlost (m/s)')
plt.grid(True)

simulator.add_trial_to_speed_plot(data1, 'data1')
simulator.add_trial_to_speed_plot(data6, 'data6')

plt.legend()
plt.show()



#python main.py