import math
import matplotlib.pyplot as plt


def simulate_sprint(F0, V0, hmotnost, vyska, vzdalenost, externi_odpor_N=0):
    
    # konstanty pro odpor vzduchu
    rho = 1.204
    Cd = 0.89
    A = 0.2025 * (vyska ** 0.725) * (hmotnost ** 0.425)

    # minimální časový úsek   
    dt = 0.001

    # počáteční stav
    cas = 0
    rychlost = 0
    ubehnuta_vzdalenost = 0
    puvodni_V0 = V0
    unava_aktivovana = False
    
    # další parametry
    draha = 6
    polomer_zatacky = 35.28 + 1.22 * draha
    f_v_sklon = F0 / V0

    # nelinearita
    nelinearita = 0.86
    
    #return
    cas_seznam = []
    vzdalenost_seznam = []
    rychlost_seznam = []
    zrychleni_seznam = []


    while ubehnuta_vzdalenost < vzdalenost:

        # propulzní síla
        aktualni_sklon = (F0/V0) * (1 - (1 - nelinearita) * (rychlost/V0))
        f_propulze = (F0 - aktualni_sklon * rychlost) * hmotnost
        f_propulze = max(0, f_propulze)

        # zpomalení zatáčka
        if vzdalenost > 100 and ubehnuta_vzdalenost < (vzdalenost - 84.39):
            f_zatacky = 0.1 * (hmotnost * rychlost**2) / polomer_zatacky

        else:
            f_zatacky = 0

        
        # odpor vzduchu
        f_odpor = 0.5 * rho * A * Cd * (rychlost ** 2)

      
        # čistá horizontální síla
        f_cista = f_propulze - f_odpor - f_zatacky - externi_odpor_N
        
        # výpočet zrychlení
        zrychleni = f_cista / hmotnost

        if zrychleni < 0.05 and not unava_aktivovana:
            unava_aktivovana = True

        if unava_aktivovana:
            V0 -= (puvodni_V0 / 51) * dt
            F0 = V0 * f_v_sklon

        #return
        cas_seznam.append(cas)
        vzdalenost_seznam.append(ubehnuta_vzdalenost)
        rychlost_seznam.append(rychlost)
        zrychleni_seznam.append(zrychleni)
        
   
        # změna stavu
        ubehnuta_vzdalenost += (rychlost * dt)
        rychlost += (zrychleni * dt)
        cas += dt

        #print(f"Čas: {cas:.2f}s | Vzdálenost: {ubehnuta_vzdalenost:.2f}m | Rychlost: {rychlost:.2f}m/s | Zrychlení: {zrychleni:.2f}m/s²")

    report = {
        'čas': cas_seznam,
        'vzdálenost': vzdalenost_seznam,
        'rychlost': rychlost_seznam,
        'zrychlení': zrychleni_seznam
    }

    return report



def maximalni_rychlost(data):
    max_rychlost = max(data['rychlost'])
    index_max_rychlost = data['rychlost'].index(max_rychlost)
    vzdalenost_max_rychlost = data['vzdálenost'][index_max_rychlost]
    vysledek = {
        'maximální_rychlost': max_rychlost,
        'vzdálenost_max_rychlost': vzdalenost_max_rychlost
    }

    return vysledek


def segmenty(data):
    hranice = 10
    predchozi_cas = 0
    seznam_segmentu = []
        
    for i, cas in enumerate(data['čas']):
        if data['vzdálenost'][i] >= hranice:

            cas_segmentu = cas - predchozi_cas

            segment = {
                'vzdálenost': hranice,
                'celkový_čas': cas,
                'čas_segmentu': cas_segmentu
            }

            seznam_segmentu.append(segment)
            hranice += 10
            predchozi_cas = cas

    seznam_segmentu.append({'vzdálenost': data['vzdálenost'][-1], 'celkový_čas': data['čas'][-1], 'čas_segmentu': data['čas'][-1] - predchozi_cas})

    return seznam_segmentu

def vykresli_graf_rychlosti(data, nazev_grafu = 'Průběh rychlosti'):
    plt.figure(figsize=(10, 6))
    plt.plot(data['vzdálenost'], data['rychlost'])
    plt.title(nazev_grafu)
    plt.grid(True)
    plt.show() 

def pridej_profil_do_grafu(data):
    plt.plot(data['vzdálenost'], data['rychlost'], label=str(data))

data1 = simulate_sprint(9, 13, 80, 1.85 , 100, 0)
data2 = simulate_sprint(7.68, 10.51, 74, 1.84 , 100, 0) #Jara
data3 = simulate_sprint(7.65, 10.36, 74, 1.84 , 100, 0)
data4 = simulate_sprint(7.65, 10.22, 84, 1.84 , 100, 0) #Strasky
data5 = simulate_sprint(7.85, 10.36, 84, 1.84 , 100, 0)
data6 = simulate_sprint(6.69, 9.33, 66, 1.84 , 100, 0) #Salcmanova
data7 = simulate_sprint(6.78, 8.69, 66, 1.84 , 100, 0)
data8 = simulate_sprint(6.56, 9.43, 71, 1.78 , 100, 0) #Splechtnova
data0 = simulate_sprint(8.5, 11, 84, 1.86 , 100, 0) #Něco odhad


vysledek = segmenty(data1)

for segment in vysledek:
    print(f"Čas na {segment['vzdálenost']:.0f} m: {segment['celkový_čas']:.2f} | Čas segmentu: {segment['čas_segmentu']:.2f}")


print('\n')

vysledek = maximalni_rychlost(data1)

print(f'Maximální rychlost: {vysledek['maximální_rychlost']:.2f} m/s')
print(f'Vzdálenost: {vysledek['vzdálenost_max_rychlost']:.1f} m')


plt.figure(figsize=(10, 6))
plt.title('Srovnání průběhu rychlosti')
plt.xlabel('Vzdálenost (m)')
plt.ylabel('Rychlost (m/s)')
plt.grid(True)

pridej_profil_do_grafu(data1)
pridej_profil_do_grafu(data6)

#plt.legend()
plt.show()



#python F-Vtest.py