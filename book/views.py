# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import requests, json

def get_contacts():
    url = 'http://www.mocky.io/v2/581335f71000004204abaf83'
    r = requests.get(url)
    contacts = r.json()
    return contacts.get('contacts')

def index(request):
    contacts = get_contacts()

    if 'search' in request.GET and request.GET['search'] is not None:
        print 'going'
        contacts = search_contacts(contacts, request.GET['search'])

    if 'sort' in request.GET and request.GET['search'] is not None:
        contacts = sort_contacts(contacts, request.GET['sort'])

    context = {'contacts': contacts}
    return render(request, 'book/index.html', context)

def search_contacts(contacts, search_param):
    searched_contacts = []
    for c in contacts:
        for att in c:
            if search_param.lower() in c.get(att).lower():
                searched_contacts.append(c)
                break
    return searched_contacts

def sort_contacts(contacts, search_param):
    if search_param == 'alpha':
        sorted_contacts = sorted(contacts, key=lambda k: k['name'])
    elif search_param == 'alpharev':
        sorted_contacts = sorted(contacts, key=lambda k: k['name'], reverse=True)
    else:
        sorted_contacts = contacts

    return sorted_contacts
