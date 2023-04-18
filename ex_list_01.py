from faker import Faker
fake = Faker('ru_RU')
from pprint import  pprint
lst_country = []
lst_input = []
for i in range(25):
    lst_input.append(fake.name())
    lst_country.append(fake.country())
pprint(lst_country)
pprint(lst_input)
pprint(len(lst_input))