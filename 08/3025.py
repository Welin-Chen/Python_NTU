dict = {'3': 'Spring', '4': 'Spring', '5': 'Spring',
        '6': 'Summer', '7': 'Summer', '8': 'Summer',
        '9': 'Autumn', '10': 'Autumn', '11': 'Autumn',
        '12': 'Winter', '1': 'Winter', '2': 'Winter'
        }

n = input()
if(int(n) < 1 or int(n) > 12):
    print("Month doesn't exist!")
else:
    print(dict[n])
