from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from app.models import *
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json
import datetime
import requests


#передеача данных справочника
def get_all_directories(request):
    directories = Directory.objects.all()
    list = []
    for dir in directories:
        list.append({
            "id": dir.id,
            "version": dir.version,
            "name": dir.name,
            "short_description": dir.short_description,
            "full_description": dir.full_description,
            "start_date": dir.start_date
        })
    return JsonResponse(list, safe=False)

#передеача данных справочника и его элементов
def get_all_dirs_with_elements(request):
    directories = Directory.objects.all()
    list = []
    for dir in directories:
        elements = []
        get_elements = Element_directory.objects.filter(parent_id=dir)
        if get_elements.exists():
            for el in get_elements:
                elements.append({
                    "code": el.kod_el,
                    "value": el.value
                })
        list.append({
            "id": dir.id,
            "version": dir.version,
            "name": dir.name,
            "short_description": dir.short_description,
            "full_description": dir.full_description,
            "start_date": dir.start_date,
            "related_elements": elements
        })
    return JsonResponse(list, safe=False)

#передеача данных по дате создания справочника
def get_by_date(request, date):
    directories = Directory.objects.filter(start_date=date)
    list = []
    if directories.exists():
        for dir in directories:
            elements = []
            get_elements = Element_directory.objects.filter(parent_id=dir)
            if get_elements.exists():
                for el in get_elements:
                    elements.append({
                        "code": el.kod_el,
                        "value": el.value
                    })
            list.append({
                "id": dir.id,
                "version": dir.version,
                "name": dir.name,
                "short_description": dir.short_description,
                "full_description": dir.full_description,
                "start_date": dir.start_date,
                "related_elements": elements
            })
    return JsonResponse(list, safe=False)


#передеача данных по id справочника
def get_by_id(request, id):
    try:
        id = int(id)
        dirs = Directory.objects.filter(id = id)
        list = []
        if dirs.exists():
            for dir in dirs:
                elements = []
                get_elements = Element_directory.objects.filter(parent_id=dir)
                if get_elements.exists():
                    for el in get_elements:
                        elements.append({
                            "code": el.kod_el,
                            "value": el.value
                        })
                list.append({
                    "id": dir.id,
                    "version": dir.version,
                    "name": dir.name,
                    "short_description": dir.short_description,
                    "full_description": dir.full_description,
                    "start_date": dir.start_date,
                    "related_elements": elements
                })

        return JsonResponse(list, safe=False)
    except:
        return JsonResponse({'error': 'ID указан неверно!'}, safe=False)

#передеача данных по версии справочника
def get_version(request,ver):
    direct = Directory.objects.filter(version=ver)
    list = []
    if direct.exists():
         for dir in direct:
             elements = []
             get_elements = Element_directory.objects.filter(parent_id=dir)
             if get_elements.exists():
                 for el in get_elements:
                     elements.append({
                         "code": el.kod_el,
                         "value": el.value
                     })
             list.append({
                 "id": dir.id,
                 "version": dir.version,
                 "name": dir.name,
                 "short_description": dir.short_description,
                 "full_description": dir.full_description,
                 "start_date": dir.start_date,
                 "related_elements": elements
             })

         return JsonResponse(list, safe=False)



#добавить новых записей с помощью json
@csrf_exempt
@require_http_methods(["POST"])
def post_new_dir(request):
    json_object = json.loads(request.body)

    name = json_object['name'] if 'name' in json_object else 'None'
    version = json_object['version'] if 'version' in json_object else 'None'
    full_description = json_object['full_description'] if 'full_description' in json_object else 'None'
    short_description = json_object['short_description'] if 'short_description' in json_object else 'None'
    start_date = datetime.datetime.now()

    Directory(name=name, version=version, full_description=full_description, short_description=short_description,
              start_date=start_date).save()

    return JsonResponse({'message': 'Добавлено'}, safe=False)


#забрать json
def test_func(request):
    data = requests.get('http://127.0.0.1:8000/rest/get-all-directories')
    json_data = json.loads(data.text)

    # return JsonResponse(json_data[0]['name'], safe=False)
    return JsonResponse(json_data, safe=False)
