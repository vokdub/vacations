from django.http import HttpResponse
from django.shortcuts import render
import datetime
import codecs
import json
def index(request):
    filename = 'static/dataBase.json'
    file = codecs.open(filename, mode='r', encoding="utf_8_sig")
    k = json.load(file)
    file.close()
    return render(request, 'index.html', context=k)
def byWeeks(request):
    filename = 'C:/Users/django/kursach/static/dataBase.json'
    file = codecs.open(filename, mode='r', encoding="utf_8_sig")
    k = json.load(file)
    file.close()
    openings = []
    weeks = []
    o = {}
    for organ in k["organization"]:
        for employee in organ["employees"]:
            openings = (employee["vacation"]["opening"].split('.'))
            dateTimeInstance = datetime.datetime(2018, int(openings[1]), int(openings[0]))
            x = dateTimeInstance.isocalendar()
            weeks.append({"firstname":employee["firstname"],"lastname":employee["lastname"],"ID":employee["ID"],"value" : x[1]})

    o.update({"cont":weeks})
    return render(request, 'byWeeks.html', context=o)
def person(request):
    filename = 'C:/Users/django/kursach/static/dataBase.json'
    file = codecs.open(filename, mode='r', encoding="utf_8_sig")
    k = json.load(file)
    file.close()
    id = (str(request))[-8:-2]
    for organ in k["organization"]:
        for employee in organ["employees"]:
            if id == employee["ID"]:
                cont = {"pers" : employee}
    return render(request, 'person.html', context=cont)


