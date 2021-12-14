from django.shortcuts import render
from django.http import JsonResponse
import requests
import json
import os
from settings_1c import connect_1c


def getPhotoEmployee(request,idEmployee):

    responseData = getPhotoEmployeeFrom1c(idEmployee)

    return JsonResponse(responseData)

def getCertificateEmploy(request,idCertificate):
    responseData = getCertificateEmployFrom1c(idCertificate)
    
    return JsonResponse(responseData)

def getPhotoEmployeeFrom1c(idEmployee):
    defaultPhoto = 'static/images/employee/default'

    url = ''.join([connect_1c.PROTO,connect_1c.IP,connect_1c.URL,'GetNameImageEmployee'])
    
    jsonData = json.dumps({'Сode_employee':idEmployee,'Type_file':'Photo'})

    response = requests.post(url,auth=(connect_1c.USER_1C,connect_1c.PASSWORD_1C),data=jsonData)
    jsonResponse = json.loads(response.content.decode('utf-8'))
    
    shortPath = 'static/images/employee/'+ jsonResponse['Name']

    pathToPhoto = os.path.abspath(os.curdir) + '/main/static/images/employee/'+ jsonResponse['Name']

    if jsonResponse['Exist']:
        if os.path.exists(pathToPhoto):
            
            return { 'pathPhoto':shortPath }
        else:
            url = ''.join([connect_1c.PROTO,connect_1c.IP,connect_1c.URL,'GetImageEmployee'])
        
            jsonData = json.dumps({'Сode_employee':idEmployee})
            
            response = requests.post(url,auth=(connect_1c.USER_1C,connect_1c.PASSWORD_1C),data=jsonData)
            binaryPhoto = response.content
            
            returnName = 'static/images/employee/'+ jsonResponse['Name']
            
            
            with open(pathToPhoto, 'wb') as file:
                file.write(binaryPhoto)
    else:
        shortPath = defaultPhoto
      

    return { 'pathPhoto':shortPath }

def getCertificateEmployFrom1c(idCertificate):
    
    returnData = {
        'id':idCertificate,
        'url':'#'
    }

    pathToCertificate = os.path.abspath(os.curdir) + '/main/static/certificate/'+ idCertificate + ".pdf"
    shortPath = '/static/certificate/'+ idCertificate + ".pdf"

    if os.path.exists(pathToCertificate):
        returnData['url'] = shortPath

        return returnData
    else:
        url = ''.join([connect_1c.PROTO,connect_1c.IP,connect_1c.URL,'GetCertificate'])
        
        jsonData = json.dumps({'Certificate_code':idCertificate,'Type':'Certificate'})

        response = requests.post(url,auth=(connect_1c.USER_1C,connect_1c.PASSWORD_1C),data=jsonData)
        binaryCertificate = response.content
        
        if type(binaryCertificate) == bytes:
            with open(pathToCertificate, 'wb') as file:
                    file.write(binaryCertificate)

        if os.path.exists(pathToCertificate):
            returnData['url'] = shortPath

        return returnData