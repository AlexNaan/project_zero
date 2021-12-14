from django.shortcuts import render,redirect
from django.http import HttpResponse
import requests
import json
import os
from django.contrib.auth import authenticate, login
from settings_1c import connect_1c


def listOrganization(request):
    
    if not request.user.is_authenticated:
        return redirect('/')

    dic_data = getListOrganizationFrom1c()
    dic_data['title'] = "Охрана труда"
    return render(request, "organization.html",context = dic_data)
    
def listSubunit(request,idOrganization):
    if not request.user.is_authenticated:
        return redirect('/')

    dic_data = getListSubunitFrom1c(idOrganization)
    dic_data['title'] = 'Организации'
    
    return render(request, "subunit.html",context = dic_data)

def listStaff(request,idOrganization,idSubunit):
    if not request.user.is_authenticated:
        return redirect('/')
    
    dic_data = getListStaffFrom1c(idOrganization,idSubunit)
    dic_data['title'] = 'Подразделение'
    dic_data['idOrganization'] = idOrganization

    return render(request, "staff.html",context = dic_data)

def employee(request,idOrganization,idSubunit,idEmployee):
    if not request.user.is_authenticated:
        return redirect('/')
        
    dic_data = getInfoEmployeeFrom1c(idOrganization,idEmployee)
    dic_data['title'] = 'Сотрудник'
    dic_data['async_load_file'] = True
    return render(request, "employee.html",context = dic_data)

def listDoc(request):
    if not request.user.is_authenticated:
        return redirect('/')

    dic_data =getListDocumentsFrom1c()
    dic_data['title'] = 'Список обучения'

    return render(request, "listDoc.html",context = dic_data)

def listEmployee(request,Symbol = 'А',Page = '1'):

    if not request.user.is_authenticated:
        return redirect('/')
    
    dic_data = getListAllEmployeeFrom1c(Symbol,Page)
    dic_data['title'] = 'Список сотрудников'
    dic_data['search_employee'] = True
    dic_data['Symbol'] = Symbol
    dic_data['Page']   = Page
    
    
    return render(request, "listEmployee.html",context = dic_data)

def getListOrganizationFrom1c():

    url = ''.join([connect_1c.PROTO,connect_1c.IP,connect_1c.URL,'GetOrg'])
    
    response = requests.post(url,auth=(connect_1c.USER_1C,connect_1c.PASSWORD_1C))

    jsonResponse = json.loads(response.content.decode('utf-8'))
    dic_data = {"jsonResponse":jsonResponse}
    
    return dic_data

def getListSubunitFrom1c(idOrganization):
    url = ''.join([connect_1c.PROTO,connect_1c.IP,connect_1c.URL,'GetSubunit'])
    
    jsonData = json.dumps({'Code_organization':idOrganization})

    response = requests.post(url,auth=(connect_1c.USER_1C,connect_1c.PASSWORD_1C),data=jsonData)
    jsonResponse = json.loads(response.content.decode('utf-8'))
    
    dic_data = {"jsonResponse":jsonResponse}

    return dic_data

def getListStaffFrom1c(idOrganization,idSubunit):
    url = ''.join([connect_1c.PROTO,connect_1c.IP,connect_1c.URL,'GetEmployee'])
    
    jsonData = json.dumps({'Code_organization':idOrganization,'Code_subunit':idSubunit})

    response = requests.post(url,auth=(connect_1c.USER_1C,connect_1c.PASSWORD_1C),data=jsonData)
    jsonResponse = json.loads(response.content.decode('utf-8'))
    
    dic_data = {"jsonResponse":jsonResponse}

    return dic_data

def getInfoEmployeeFrom1c(idOrganization,idEmployee):

    url = ''.join([connect_1c.PROTO,connect_1c.IP,connect_1c.URL,'GetInfoEmployee'])
    
    jsonData = json.dumps({'Code_organization':idOrganization,'Сode_employee':idEmployee})

    response = requests.post(url,auth=(connect_1c.USER_1C,connect_1c.PASSWORD_1C),data=jsonData)
    jsonResponse = json.loads(response.content.decode('utf-8'))
    
    dic_data = {"jsonResponse":jsonResponse}

    return dic_data

def getListDocumentsFrom1c():

    url = ''.join([connect_1c.PROTO,connect_1c.IP,connect_1c.URL,'GetListDoc'])
    
    response = requests.post(url,auth=(connect_1c.USER_1C,connect_1c.PASSWORD_1C))
    
    jsonResponse = json.loads(response.content.decode('utf-8'))
    dic_data = {"jsonResponse":jsonResponse}
    
    return dic_data

def getListAllEmployeeFrom1c(Symbol,Page):

    url = ''.join([connect_1c.PROTO,connect_1c.IP,connect_1c.URL,'GetAllEmployees'])
    jsonData = json.dumps({'Symbol':Symbol,'Page':Page})

    response = requests.post(url,auth=(connect_1c.USER_1C,connect_1c.PASSWORD_1C),data=jsonData)
    

    jsonResponse = json.loads(response.content.decode('utf-8'))
    dic_data = {"jsonResponse":jsonResponse}
    
    return dic_data