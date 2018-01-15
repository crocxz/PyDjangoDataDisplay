from .models import Entry
from django.shortcuts import render
from django.core import management
from settings import STATIC_ROOT
import os
import json

#from django.core import management
#management.call_command('your_command', your_options)

# open jsonfile, parse from dump into Entry objs
def load():
    file = open(os.path.join(STATIC_ROOT, 'dump.json'), 'r')
    print(file)
    arr = json.load(file)
    # loop array of jsons, save into model
    for entry in arr:
        print(entry)
        ent = Entry()
        ent.date = entry['date']
        ent.filename = entry['filename']
        ent.action = entry['action']
        ent.rating = entry['rating']
        ent.save()

# delete objects from db
def clear():
    if (Entry.objects.all().exists()): 
        Entry.objects.all().delete()
        print("wiped for repopulation")

#render and 
def index(request):
    clear()
    load()
    latest_entry_list = Entry.objects.order_by('date')[:]
    context = {'latest_entry_list': latest_entry_list}
    return render(request, 'table/index.html', context)

# clear all 
def addNewEntries()
    file = open(os.path.join(STATIC_ROOT, 'dump.json'), 'r')
    print(file)
    arr = json.load(file)
    # loop array of jsons, save into model
    for entry in arr:
        jobj = json.loads(entry)
        try:
            #check for object, then skip if found
            query = Entry.objects.get(date=entry['date'], filename=entry['filename'],
            action=entry['action'], rating=entry['rating'])
            continue
        except ObjectDoesNotExist as identifier:
            #else add object
            pass
            print("Adding Entry" + entry)
            ent = Entry()
            ent.date = entry['date']
            ent.filename = entry['filename']
            ent.action = entry['action']
            ent.rating = entry['rating']
            ent.save()

 #to check for deletions, check all database entries, find all  
def updateDeletions()
    file = open(os.path.join(STATIC_ROOT, 'dump.json'), 'r')
    print(file)
    arr = json.load(file)
    dset = Entry.objects
    for entry in arr:
        dset.filter(date=entry['date'], filename=entry['filename'],
                    action=entry['action'], rating=entry['rating'])
    dset.delete()
    
       
            