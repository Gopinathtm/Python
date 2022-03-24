#Dictionary in list
favourite_number = {'subin': 7,
                    'gopi': 3,
                    'karthi': 4,
                    'mani': 6}
favourite_food = {'subin': 'biriyani',
                    'gopi': 'chapathi',
                    'karthi': 'chutnet',
                    'mani': 'roll'}
favourite_company = {'subin': 'zf',
                    'gopi': 'google',
                    'karthi': 'tvs',
                    'mani': 'koel', }
peoples_favourite = [favourite_number, favourite_company, favourite_food]
for x in peoples_favourite:
    print(x)
#output
"""
{'subin': 7, 'gopi': 3, 'karthi': 4, 'mani': 6}
{'subin': 'zf', 'gopi': 'google', 'karthi': 'tvs', 'mani': 'koel'}
{'subin': 'biriyani', 'gopi': 'chapathi', 'karthi': 'chutnet', 'mani': 'roll'}
"""
