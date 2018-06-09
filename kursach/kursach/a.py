import datetime
import codecs
import json

filename = 'C:/Users/django/kursach/static/dataBase.json'
file = codecs.open(filename, mode='r', encoding="utf_8_sig")
k = json.load(file)
file.close()

openings = []
weeks = {}

for organ in k["organization"]:
    for employee in organ["employees"]:
        openings = (employee["vacation"]["opening"].split('.'))

        dateTimeInstance = datetime.datetime(2018, int(openings[1]), int(openings[0]))
        x = dateTimeInstance.isocalendar()
        weeks.update({employee["firstname"] : x[1]})


# o = k["organization"][0]["employees"][0]["vacation"]["opening"]
#
#
#

print(openings)
print(weeks)



# k = input('dd')
# a = k.split('.')
# print(a)
# print(k)