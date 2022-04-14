import os

with open('directories.txt', 'a') as d:
    for current_dir, dirs, files in os.walk('main'):
        if list(filter(lambda x: x.endswith('.py'), files)):
            d.write('{}\n'.format(current_dir))