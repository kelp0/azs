Работу выполниили: Скороходов М. 80%, Лысенко М. 60%, Ячин Д. 30%
import random
azs = open('azs.txt','r')
inp = open('input.txt','r')
azs_l = azs.readlines()
prices = {'АИ-80': 45, 'АИ-92': 44, 'АИ-95': 50, 'АИ-98': 52}
petrol = {'АИ-80': 0, 'АИ-92': 0, 'АИ-95': 0, 'АИ-98': 0}
cars_not_served = 0

#Информация по заправке
for i in range(len(azs_l)):
    azs_l[i] = azs_l[i].split()
    azs_l[i][0] = int(azs_l[i][0])
    azs_l[i][1] = int(azs_l[i][1])
inp_l = list(map(lambda x: x.strip(), inp.readlines()))

#Информация по клиентам
for i in range(len(inp_l)):
    inp_l[i] = inp_l[i].split()
    inp_l[i][1] = int(inp_l[i][1])
azs_filling = {azs_l[i][0]: 0 for i in range(len(azs_l))}
azs_free = {azs_l[i][0]: azs_l[i][1] for i in range(len(azs_l))}

#Получаем время
def timing(times, minutes=0):
    times = times.split(':')
    hours = int(times[0])
    mins = int(times[1])
    minutes = hours*60 + mins
    return minutes

#Переводим время в нужную величину
def time_manage(minutes):
    s = ''
    hours = minutes // 60
    l_minutes = minutes - hours * 60
    if len(str(hours)) == 1:
        s += '0' + str(hours)
    else:
        s += str(hours)
    if len(str(l_minutes)) == 1:
        s += ':' + '0' + str(l_minutes)
    else:
        s += ':' + str(l_minutes)
    return s


def new(i, type_petrol, number_of_gas):
    print('В ' + str(i[0]) + ' новый клиент: ' + str(i[0]) + ' ' + type_petrol + ' ' + str(
        i[1]) + ' ' + str(fill_final_time) + ' встал в очередь к автомату №' + str(
        number_of_gas))
    azs_filling[number_of_gas] += 1
    petrol[type_petrol] += i[1]

time_orders = []
for minute in range(1, (24 * 60) + 1):
    for l in time_orders:
        for k in time_orders:
            if k[1] == minute:
                print('В ' + time_manage(k[1]) + ' клиент ' + time_manage(k[0]) + ' ' + k[2] + ' ' + str(
                    k[3]) + ' ' + str(k[4]) + ' заправил свой автомобиль и покинул АЗС.')
                azs_filling[k[5]] -= 1
                time_orders.remove(k)
                for i in range(len(azs_l)):
                    print('Автомат №' + str(azs_l[i][0]) + ' максимальная очередь: ' + str(azs_l[i][1]) + ' Марки бензина: ' + ' '.join(azs_l[i][2::]) + ' ->' + azs_filling[i + 1] * '*')
    for i in inp_l:
        c = 0
        time = i[0]
        time_in_minutes = timing(time)
        litres = i[1]
        add = random.randint(-1, 1)
        if litres % 10 == 0:
            if litres // 10 + add != 0:
                fill_final_time = litres // 10 + add
            elif litres // 10 + add == 0:
                fill_final_time = 1
        elif litres % 10 != 0:
            if litres // 10 + add != 0:
                fill_final_time = litres // 10 + add + 1
            elif litres // 10 + add == 0:
                fill_final_time = 1
        type_petrol = i[2]
        if minute == time_in_minutes:
            for gas in azs_l:
                for j in gas[2::]:
                    if type_petrol == j:
                        if azs_free[gas[0]] > azs_filling[gas[0]] and c == 0:
                            num_of_gas = gas[0]
                            new(i, type_petrol, gas[0])
                            c += 1
                            break
            if c == 0:
                cars_not_served += 1
                print('В ' + time + ' новый клиент: ' + time + ' ' + type_petrol + ' ' + str(litres) + ' ' + str(
                    fill_final_time) + ' не смог заправить автомобиль и покинул АЗС.')
            else:
                extra = [time_in_minutes, time_in_minutes + fill_final_time, type_petrol, litres, fill_final_time,
                         num_of_gas]
                time_orders.append(extra)
            for i in range(len(azs_l)):
                print('Автомат №' + str(azs_l[i][0]) + ' максимальная очередь: ' + str(azs_l[i][1]) + ' Марки бензина: ' + ' '.join(azs_l[i][2::]) + ' ->' + azs_filling[i + 1] * '*')

print("Количество литров, проданное за сутки по каждой марке бензина:", petrol)
b = {k: v * petrol[k] for k, v in prices.items() if k in petrol}
print("Продажи по каждой марке бензина:", b)
print("Суммарная прибыль:", sum(b.values()))
print("Количество машин, покивнуших АЗС без заправки:", cars_not_served)
