import json

json_data = json.loads(input())

families = {element['name']: [] for element in json_data}

for child in initial:
    for parent in families:
        if parent in child['parents']:
            families[parent].append(child['name'])

for element in families:
    families[element] = set(families[element])


def search_children(families, parent, checked=None):
    if checked is None:
        checked = set()
    checked.add(parent)
    for next_one in families[parent] - checked:
        search_children(families, next_one, checked)
    return checked


for parent in sorted(families.keys()):
    print(parent, ':', len(search_children(families, parent)))


