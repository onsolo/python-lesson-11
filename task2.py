# Имеются данные о площади и стоимости 15 домов.
# Риелтору требуется узнать в каких домах стоимость квадратного метра меньше 50000 рублей.
# Предоставьте ему графические данные о стоимости квадратного метра каждого дома и
# список подходящих ему домов, отсортированных по площади.
# Данные о домах сформируйте случайным образом. Площади от 100 до 300 кв. метров, цены от 3 до 20 млн

from matplotlib import pyplot as plt
import random

housesArea = [random.randint(100, 300) for i in range(0, 15)]
housesPrise = [random.randint(3000000, 20000000) for i in range(0, 15)]
x = []
oneMeterPrise = []
lowPrise = []
sortedHouses = []

for i in range(0, 15):
    x.append(i+1)

for i in range(len(housesArea)):
    oneMeterPrise.append(round(housesPrise[i] / housesArea[i]))

for i in range(len(oneMeterPrise)):
    if oneMeterPrise[i] < 50000:
        lowPrise.append(oneMeterPrise[i])
        sortedHouses.append(housesArea[i])

print('Дома со стоимостью квадратного метра меньше 50000 рублей:')
for i in range(len(lowPrise)):
    print(f'Площадь {sortedHouses[i]}, стоимость квадратного метра {lowPrise[i]}')

plt.xlabel('Номер дома')
plt.ylabel('Стоимость квадратного метра')
plt.grid(which='major')

plot2 = list(50000 for a in range(1, 16))
plt.plot(x, plot2)
plt.plot(x, oneMeterPrise, 'go')
plt.show()
