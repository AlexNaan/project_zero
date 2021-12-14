from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from users_1c.models import ListUsers
from django.core.exceptions import ObjectDoesNotExist
import json
import requests
from django.contrib.auth import authenticate, login, logout
from settings_1c import connect_1c

def task_close(request):
    
    #Если не авторризавался то на авторизацию отправляем
    if not request.user.is_authenticated:
        return redirect('/')

    username = request.user
    try:
        user_1c = ListUsers.objects.get(user_web=username)
        dic_data = get_task(user_1c,True)

        if type(dic_data) == list:
            if len(dic_data) == 0:
                    return render(request, "task/task.html",context = {"empty_task":True,"title":"Закрытые"})
            else:
                return render(request, "task/task.html",context = {"jsonResponse":dic_data,"title":"Закрытые"})
        else:
            if dic_data.get("Error"):
                return HttpResponse("В получение данных произошла ошибка.Обратитесть к разработчику <br>"  + str(dic_data.get("Error"))) # Пока для отладки оставлю
    except ObjectDoesNotExist:
        return HttpResponse("Пользователь не найден. <br> Операция не возможна.") # Пока для отладки оставлю

def task_active(request):

    #Если не авторризавался то на авторизацию отправляем
    if not request.user.is_authenticated:
        return redirect('/')

    username = request.user

    try:
        user_1c = ListUsers.objects.get(user_web=username)
        dic_data = get_task(user_1c,False)

        if type(dic_data) == dict and dic_data.get('Error') != None:
            return render(request, "task/task.html",context = {"empty_task":True,"title":"Активные"})
        else:
            return render(request, "task/task.html",context = {"jsonResponse":dic_data,"title":"Активные"})
    except ObjectDoesNotExist:
        
        return render(request, 'task/task.html', context={"UserError":"Пользователь не найден!!!"})

def get_task(user_1c,flAction):

    jsonData = json.dumps({'КодПолучателя':user_1c.kod_users_1c,'Выполнена':flAction})
    url = ''.join([connect_1c.PROTO,connect_1c.IP,connect_1c.URL,'ЗадачиПользователя'])

    response = requests.post(url,auth=(connect_1c.USER_1C,connect_1c.PASSWORD_1C),data=jsonData)
    DataPost = response.content.decode('utf-8')

    if not DataPost:
        return {"Error":"Ответ пустой"}
    else:
        #Если ответ пришел не пустой из 1с получитм из  него json
        jsonResponse = json.loads(DataPost)

        if type(jsonResponse) == list:
            return jsonResponse
        elif jr.get("Error"):
            #если в json есть Error тогда отправим его
            return (jr)

def selected_task(request,number="000000000",str_data=""):

    #Если не авторризавался то на авторизацию отправляем
    if not request.user.is_authenticated:
        return redirect('/')


    username = request.user

    try:
        url = ''.join([connect_1c.PROTO,connect_1c.IP,connect_1c.URL,'ПолучитьЗадачу'])
        user_1c = ListUsers.objects.get(user_web=username)

        jsonData = json.dumps({'КодПолучателя':user_1c.kod_users_1c,"ДатаЗадачи":str_data,"НомерЗадачи":number})
        
        response = requests.post(url,auth=(connect_1c.USER_1C,connect_1c.PASSWORD_1C),data=jsonData)
        DataPost = response.content.decode('utf-8')

        if not DataPost:
            return {"Error":"Ответ пустой"}
        else:
            #Если ответ пришел не пустой из 1с получитм из  него json
            jsonResponse = json.loads(DataPost)

            if type(jsonResponse) == list:

                if jsonResponse[0].get("ПризнакСогласования"):
                    check_box = "disabled"
                else:
                    check_box = ""

                if jsonResponse[0].get("СтатусСогласования") == "Согласована":
                    cb_sogl = "checked"
                    cb_not_sogl = ""
                elif jsonResponse[0].get("СтатусСогласования") == "НеСогласована":
                    cb_sogl = ""
                    cb_not_sogl = "checked"
                else:
                    cb_sogl = ""
                    cb_not_sogl = ""

                return render(request, "task/selected_task_index.html",context = {"jsonResponse":jsonResponse,"number":number,"str_data":str_data,"FL_dostupnost":check_box,"fl_sog":cb_sogl,"fl_not_sog":cb_not_sogl})
            elif jsonResponse.get("Error"):
                #если в json есть Error тогда отправим его
                return HttpResponse("В получение данных произошла ошибка.Обратитесть к разработчику <br>"  + str(jsonResponse.get("Error")))

    except ObjectDoesNotExist:
        return render(request, 'task/task.html', context={"UserError":"Пользователь не найден!!!"})

def selected_exec(request,number="000000000",str_data=""):

    #Если не авторризавался то на авторизацию отправляем
    if not request.user.is_authenticated:
        return redirect('/')


    url = ''.join([connect_1c.PROTO,connect_1c.IP,connect_1c.URL,'ВыполнитьЗадачу'])
    
    if request.method == 'POST':
        comment = request.POST['comment']
        otvet = request.POST['agreed']

        username = request.user
        user_1c = ListUsers.objects.get(name_users_1c=username)
        

        jsonData = json.dumps({'КодПолучателя':user_1c.kod_users_1c,"ДатаЗадачи":str_data,"НомерЗадачи":number,"Комментарий":comment,"Флаг":otvet})
        response = requests.post(url,auth=(connect_1c.USER_1C,connect_1c.PASSWORD_1C),data=jsonData)
        DataPost = response.content.decode('utf-8')


        return render(request, "task/task_execute.html")
    else:
        return HttpResponse()
