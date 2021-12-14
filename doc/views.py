from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from users_1c.models import ListUsers
from django.core.exceptions import ObjectDoesNotExist
import json
import requests
from settings_1c import connect_1c

def doc_all(request):

    #Если не авторризавался то на авторизацию отправляем
    if not request.user.is_authenticated:
        return redirect('/')


    username = request.user
    try:
        user_1c = ListUsers.objects.get(user_web=username)
        dic_data = get_all_doc(user_1c)
        return render(request, "doc/doc_all.html",context = dic_data)

    except ObjectDoesNotExist:
        return render(request, 'doc/doc_all.html', context={"UserError":"Пользователь не найден!!!"})

def doc_1(request):

    #Если не авторризавался то на авторизацию отправляем
    if not request.user.is_authenticated:
        return redirect('/')


    username = request.user
    try:
        user_1c = ListUsers.objects.get(user_web=username)
        dic_data = get_list_doc(user_1c,1)
        return render(request, "doc/doc_Universal_List.html",context = dic_data)

    except ObjectDoesNotExist:
        return render(request, 'doc/doc_Universal_List.html', context={"UserError":"Пользователь не найден!!!"})

def doc_2(request):

    #Если не авторризавался то на авторизацию отправляем
    if not request.user.is_authenticated:
        return redirect('/')


    return HttpResponse("doc_2")

def doc_3(request):

    #Если не авторризавался то на авторизацию отправляем
    if not request.user.is_authenticated:
        return redirect('/')


    return HttpResponse("doc_3")

def doc_4(request):

    #Если не авторризавался то на авторизацию отправляем
    if not request.user.is_authenticated:
        return redirect('/')


    return HttpResponse("doc_4")

def doc_5(request):

    #Если не авторризавался то на авторизацию отправляем
    if not request.user.is_authenticated:
        return redirect('/')

    return HttpResponse("doc_5")

def selected_docinfo(request,number=000000000,str_data='01.01.0001',type_doc=0):

    #Если не авторризавался то на авторизацию отправляем
    if not request.user.is_authenticated:
        return redirect('/')


    username = request.user
    try:
        user_1c = ListUsers.objects.get(user_web=username)
        data_doc = get_doc_info(request,number,str_data,type_doc,user_1c)

        if type_doc == 1:
            return render(request, "doc/doc_info_1.html",context=data_doc)
        elif type_doc == 2:
            return render(request, "doc/doc_info_2.html",context=data_doc)
        elif type_doc == 3:
            return render(request, "doc/doc_info_3.html",context=data_doc)
        elif type_doc == 4:
            return render(request, "doc/doc_info_4.html",context=data_doc)
        elif type_doc == 5:
            return render(request, "doc/doc_info_5.html",context=data_doc)
        else:
            return HttpResponse("Форма для документ не найден!")

    except ObjectDoesNotExist:
        return HttpResponse("Документ не найден!")
        #return render(request, 'doc/doc_info.html', context={"UserError":"Документ не найден!!!"})

def get_doc_info(request,number_doc,date_doc,type_doc,user_1c):

    #Если не авторризавался то на авторизацию отправляем
    if not request.user.is_authenticated:
        return redirect('/')

    
    jsonData = json.dumps({'КодПолучателя':user_1c.kod_users_1c,'НомерДокумента':number_doc,"ДатаДокумента":date_doc,"ТипДокумента":type_doc})
    url = ''.join([connect_1c.PROTO,connect_1c.IP,connect_1c.URL,'ПолучитьДокумент'])

    response = requests.post(url,auth=(connect_1c.USER_1C,connect_1c.PASSWORD_1C),data=jsonData)
    jsonResponse = json.loads(response.content.decode('utf-8'))
 
    dic_data = {"jsonResponse":jsonResponse}
    return dic_data

def get_all_doc(user_1c):

    #Если не авторризавался то на авторизацию отправляем
    if not request.user.is_authenticated:
        return redirect('/')


    jsonData = json.dumps({'КодПолучателя':user_1c.kod_users_1c})
    url = ''.join([connect_1c.PROTO,connect_1c.IP,connect_1c.URL,'ПолучитьВсеДокументы'])

    response = requests.post(url,auth=(connect_1c.USER_1C,connect_1c.PASSWORD_1C),data=jsonData)
    jsonResponse = json.loads(json.loads(response.content.decode('utf-8')))

    dic_data = {"jsonResponse":jsonResponse}
    return dic_data

def get_list_doc(user_1c,numberType):

    #Если не авторризавался то на авторизацию отправляем
    if not request.user.is_authenticated:
        return redirect('/')


    jsonData = json.dumps({'КодПолучателя':user_1c.kod_users_1c,"ТипДокумента":numberType})
    url = ''.join([connect_1c.PROTO,connect_1c.IP,connect_1c.URL,'ПолучитьСписокДокументовПоТипу'])

    response = requests.post(url,auth=(connect_1c.USER_1C,connect_1c.PASSWORD_1C),data=jsonData)
    jsonResponse = json.loads(json.loads(response.content.decode('utf-8')))

    dic_data = {"jsonResponse":jsonResponse}
    return dic_data
