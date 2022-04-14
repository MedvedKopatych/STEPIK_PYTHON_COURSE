import requests


with open('dataset_24476_3.txt', 'r') as data_in:
    numbers = data_in.read().splitlines()

for number in numbers:
    api_url = 'http://numbersapi.com/' + number + '/math'
    params = {
        'json': 'true'
    }
    response = requests.get(api_url, params=params)
    if response.status_code == 200:
        answer = response.json()
        if answer['found']:
            print('Interesting')
            with open('API_data_out.txt', 'a') as data_out:
                data_out.write('Interesting\n')
        else:
            print('Boring')
            with open('API_data_out.txt', 'a') as data_out:
                data_out.write('Boring\n')
