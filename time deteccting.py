import time

while True:
    try:
        numbers_of_vehicles = eval(input("Enter the number of vehicles (e.g., [{4:0},{2:1},{3:1},{5:1}]): "))
        numbers_of_vehicles.sort(key=lambda x: list(x.values())[0], reverse=True)
    except (SyntaxError, NameError, TypeError):
        print("Please enter a valid list of dictionaries.")
        continue

    for vehicle in numbers_of_vehicles:
        key = list(vehicle.keys())[0]  
        value = list(vehicle.values())[0]  

        if 1 <= key <= 5:
            print('ROAD b c d ARE IN HOLD', end='')
            print('\rTHIS SIDE ROAD VEHICLES ARE ready to go in 2 sec')
            for i in reversed(range(3)):
                print(f'\rYELLOW LIGHT STOPS IN {i}', end='')
                time.sleep(1)
            print('\r', end='')
            for i in reversed(range(key * 2)):  
                print(f'\rThe green light stops in {i}', end='')
                time.sleep(1)
            print('\r', end='')

        elif 6 <= key <= 10:
            print('ROAD A C D ARE IN HOLD', end='')
            print("\rTHIS SIDE ROAD VEHICLES ARE ready to go in 2 sec")
            for i in reversed(range(3)):
                print(f'\rYELLOW LIGHT STOPS IN {i}', end='')
                time.sleep(1)
            print('\r', end='')
            for i in reversed(range(key * 2)):
                print(f'\rThe green light stops in {i}', end='')
                time.sleep(1)
            print('\r', end='')

        elif 11 <= key <= 15:
            print('ROAD A C D ARE IN HOLD', end='')
            print("\rTHIS SIDE ROAD VEHICLES ARE ready to go in 2 sec")
            for i in reversed(range(3)):
                print(f'\rYELLOW LIGHT STOPS IN {i}', end='')
                time.sleep(1)
            print('\r', end='')
            for i in reversed(range(key * 2)):
                print(f'\rThe green light stops in {i}', end='')
                time.sleep(1)
            print('\r', end='')

        elif 16 <= key <= 20:
            print('ROAD A B D ARE IN HOLD', end='')
            print("\rTHIS ROAD VEHICLES ARE ready to go in 2 sec")
            for i in reversed(range(3)):
                print(f'\rYELLOW LIGHT STOPS IN {i}', end='')
                time.sleep(1)
            print('\r', end='')
            for i in reversed(range(key * 2)):
                print(f'\rThe green light stops in {i}', end='')
                time.sleep(1)
            print('\r', end='')

    break  
