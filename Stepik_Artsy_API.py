import requests
import json
from operator import itemgetter


client_id = 'ff6b5227011c2ab8fc95'
client_secret = 'e77e1db4b743e54065ca1fbe8029a4a0'

r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })

j = json.loads(r.text)

token = j["token"]
headers = {"X-Xapp-Token": token}
api_url = "https://api.artsy.net/api/artists/"
artists = []

with open('dataset_24476_4.txt', 'r') as data_in:
    lines = data_in.read().splitlines()

for line in lines:
    response = requests.get(api_url + line, headers=headers)
    response.encoding = 'utf-8'
    if response.status_code == 200:
        j_in = json.loads(response.text)
        print(j_in)
        artist = {'birthday': j_in['birthday'], 'name': j_in['sortable_name']}
        artists.append(artist)

sorted_artists = sorted(artists, key=itemgetter('birthday', 'name'))
print(sorted_artists)
for item in sorted_artists:
    with open('API_Artsy.txt', 'a', encoding='utf-8') as data_out:
        data_out.write('%s\n' % item['name'])
