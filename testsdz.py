def read_package(workout_type: str, data: list):
    """Прочитать данные полученные от датчиков."""
    packages_dict = {workout_type: data}

packages = [
    ('SWM', [720, 1, 80, 25, 40]),
    ('RUN', [15000, 1, 75]),
    ('WLK', [9000, 1, 75, 180])]

packages_dict = {'SWM': [720, 1, 80, 25, 40]}
#for workout_type, data in packages:
#    training = read_package(workout_type, data)

print(*packages_dict['SWM'])


#pack_dict = dict(packages)
#wlk_values = name_trainig, count_steps, time_hours, weight = list((pack_dict['WLK'])[0:5])
#print(name_trainig)
#print(pack_dict.keys())
#i = 'WLK'
#def padict(i):
#    if i in pack_dict.keys():
#        y = int(list(pack_dict[i])[0])
#        return y
#print(padict(i))
#padict('RUN')
#for i in padick:
#    if i == 'SWM':
#        print('Swimming')
#    elif i == 'RUN':
#        print('Running')
#    elif i == 'WLK':
#        print('Walking')
#    else:
#        pass

#print(type(padick))
#print(padick)
#print(pack_dict.keys())

