#adding new kayLvalue pairs in dictionary
aliens = []
for alien_number in range (30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
for alien in aliens[:3]:
    if alien ['color'] == 'green':
        alien ['color'] = 'yellow'
        alien ['points'] = 10
        alien ['speed'] = 'medium'

for alien in aliens[:5]:
    print(alien)
print('...')
print(f'\n Total No. of aliens is {len(aliens)}')
#output
"""
{'color': 'yellow', 'points': 10, 'speed': 'medium'}
{'color': 'yellow', 'points': 10, 'speed': 'medium'}
{'color': 'yellow', 'points': 10, 'speed': 'medium'}
{'color': 'green', 'points': 5, 'speed': 'slow'}
{'color': 'green', 'points': 5, 'speed': 'slow'}
...

 Total No. of aliens is 30
"""
