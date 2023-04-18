import yaml
from pprint import pprint

with open('trafic.yaml') as f:
    templates = yaml.safe_load(f)

pprint(templates)
total = 0
for i in templates:
    total += i['tr']
pprint(total)
