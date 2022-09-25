Работу выполниили: Скороходов М. 80%, Лысенко М. 60%, Ячин Д. 30%
import random
azs=open('azs.txt','r',encoding='UTF-8')
inp=open('input.txt','r',encoding='UTF-8')
list_azs = azs.readlines()
prices = {'АИ-80': 45, 'АИ-92': 44, 'АИ-95': 50, 'АИ-98': 52}
petrol = {'АИ-80': 0, 'АИ-92': 0, 'АИ-95': 0, 'АИ-98': 0}
cash = 0 
unhappy_cars = 0 


for i in range(len(list_azs)):
    list_azs[i] = list_azs[i].split()
    list_azs[i][0] = int(list_azs[i][0])
    list_azs[i][1] = int(list_azs[i][1])
list_input = list(map(lambda x: x.strip(), inp.readlines()))

for i in range(len(list_input)):
    list_input[i] = list_input[i].split()
    list_input[i][1] = int(list_input[i][1])
azs_stars = {list_azs[i][0]: 0 for i in range(len(list_azs))}
azs_places = {list_azs[i][0]: list_azs[i][1] for i in range(len(list_azs))}


def get_time(times, minutes=0):

    times = times.split(':')
    hours = int(times[0])
    minutes_1 = int(times[1])
    minutes = hours * 60 + minutes_1
    return minutes


def get_time_back(minutes):

    string = ''
    hours = minutes // 60
    minutes_left = minutes - hours * 60
    if len(str(hours)) == 1:
        string += '0' + str(hours)
    else:
        string += str(hours)
    if len(str(minutes_left)) == 1:
        string += ':' + '0' + str(minutes_left)
    else:
        string += ':' + str(minutes_left)
    return string


def filling_with_random(liters):

    adding = random.randint(-1, 1)
    if liters % 10 == 0:
        if liters // 10 + adding != 0:
            return liters // 10 + adding
        elif liters // 10 + adding == 0:
            return 1
    elif liters % 10 != 0:
        if liters // 10 + adding != 0:
            return liters // 10 + adding + 1
        elif liters // 10 + adding == 0:
            return 1


def condition():

    for i in range(len(list_azs)):
        print('Автомат №' + str(list_azs[i][0]) + ' максимальная очередь: '
              + str(list_azs[i][1]) + ' Марки бензина: ' + ' '.join(list_azs[i][2::]) + ' ->' + azs_stars[
                  i + 1] * '*')





def action_coming(i, type_petrol, number_of_gas):

    print('В ' + str(i[0]) + ' новый клиент: ' + str(i[0]) + ' ' + type_petrol + ' ' + str(
        i[1]) + ' ' + str(time_to_replenish) + ' встал в очередь к автомату №' + str(
        number_of_gas))
    azs_stars[number_of_gas] += 1
    petrol[type_petrol] += i[1]


time_orders = []
for minute in range(1, (24 * 60) + 1):
    for l in time_orders:
        for k in time_orders:
            if k[1] == minute:
                print('В ' + get_time_back(k[1]) + ' клиент ' + get_time_back(k[0]) + ' ' + k[2] + ' ' + str(
                    k[3]) + ' ' + str(k[4]) + ' заправил свой автомобиль и покинул АЗС.')
                azs_stars[k[5]] -= 1
                time_orders.remove(k)
                condition()
    for i in list_input:
        c = 0
        time = i[0]
        time_in_minutes = get_time(time)
        litres = i[1]
        time_to_replenish = filling_with_random(litres)
        type_petrol = i[2]
        if minute == time_in_minutes:
            for gas in list_azs:
                for j in gas[2::]:
                    if type_petrol == j:
                        if azs_places[gas[0]] > azs_stars[gas[0]] and c == 0:
                            num_of_gas = gas[0]
                            action_coming(i, type_petrol, gas[0])
                            c += 1
                            break
            if c == 0:
                unhappy_cars += 1
                print('В ' + time + ' новый клиент: ' + time + ' ' + type_petrol + ' ' + str(litres) + ' ' + str(
                    time_to_replenish) + ' не смог заправить автомобиль и покинул АЗС.')
            else:
                extra = [time_in_minutes, time_in_minutes + time_to_replenish, type_petrol, litres, time_to_replenish,
                         num_of_gas]
                time_orders.append(extra)
            condition()


def final_answer(petrol, prices, unhappy_cars):

    print("Количество литров, проданное за сутки по каждой марке бензина:", petrol)
    b = {k: v * petrol[k] for k, v in prices.items() if k in petrol}
    print("Продажи по каждой марке бензина:", b)
    print("Суммарная прибыль:", sum(b.values()))
    print("Количество машин, покивнуших АЗС без заправки:", unhappy_cars)


final_answer(petrol, prices, unhappy_cars)
