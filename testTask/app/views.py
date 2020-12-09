from django.http import HttpResponse
from app.models import Directory, Element_directory
from django.shortcuts import render, redirect


#просмотр списка справочников
def directory(request):
    d = Directory.objects.all()

    res = {'sp': d}

    return render(request, 'table_directory.html', res)
#добавление нового справочника
def add_directory(request):
    if request.method == "POST":
        name = request.POST.get('name','')
        short_description = request.POST.get('short_description','')
        full_description = request.POST.get('full_description','')
        version = request.POST.get('version','')
        start_date = request.POST.get('start_date','')
        directory = Directory(name=name,short_description=short_description,full_description=full_description,version=version,start_date=start_date)
        directory.save()
        return redirect('/')
    else:
        return render(request, 'add_directory.html')

#просмотр элементов справочника
def get_sp_info(request, id):
    selected_el = Element_directory.objects.filter(parent_id=id)
    if selected_el.exists():
        list = Element_directory.objects.filter(parent_id=id)

        args = {
            'list': list

        }

        return render(request, 'table_element.html', args)
    else:
        return render(request, 'element_not_fiind.html', {'not_find': 'элемент не найден'})
#редактирование спровочников
def edit_elemet(request,id):
    if request.method=="POST":
        name = request.POST.get('name','')
        short_description = request.POST.get('short_description','')
        full_description = request.POST.get('full_description','')
        version = request.POST.get('version','')
        start_date = request.POST.get('start_date','')
        Directory.objects.filter(id=id).update(name=name,short_description=short_description, full_description=full_description,version=version,start_date=start_date)
        return redirect('/')
    else:
        direct_info = Directory.objects.filter(id=id)
        if direct_info.exists():
            direct_data = Directory.objects.get(id=id)
            args = {
                'sp': direct_data
            }
            return render(request, 'edit_direct.html', args)
        else:
            return HttpResponse('элемент не найдена')
#удаление справочников
def delete_element(request,id):

    check_element = Directory.objects.filter(id=id)

    if check_element.exists():

        Directory.objects.get(id=id).delete()
        return redirect('/')
    else:
        return HttpResponse('справочник не найдена!')


#добаление элементов справочника
def add_el_direct(request):
    select_direct = Directory.objects.all()
    if request.method == "POST":
        dir_id = int(request.POST.get('dir', None))
        code = request.POST.get('code_input', None)
        value = request.POST.get('value_input', None)

        if dir_id is not None:
            dir_entity = Directory.objects.get(id=dir_id)
            if code is not None and value is not None:
                Element_directory(kod_el=code, value=value, parent_id=dir_entity).save()
                return HttpResponse('Сохранено!')
            else:
                return HttpResponse('Значения указаны неверно!')
        else:
            return HttpResponse('ID справочника не указан или неверен')
    else:
        args = {
            'list': select_direct
        }
        return render(request, 'add_el_direct.html', args)


#удаления элемента
def delete_el_direct(request,id):

    check_element = Element_directory.objects.filter(id=id)

    if check_element.exists():

        Element_directory.objects.get(id=id).delete()
        return HttpResponse('элемент удалена!')
    else:
        return render(request, 'element_not_fiind.html', {'not_find': 'элемент не найден'})

#редактирование элементов справочника
def edit_elemet_direct(request,id):
    if request.method=="POST":

        kod_el = request.POST.get('kod_el','')
        value = request.POST.get('value','')
        Element_directory.objects.filter(id=id).update(kod_el=kod_el,value=value)
        return HttpResponse('справочник обновлен')
    else:
        elemet_info = Element_directory.objects.filter(id=id)
        if elemet_info.exists():
            elemet_data = Element_directory.objects.get(id=id)
            args = {
                'elemet_data': elemet_data
            }
            return render(request, 'edit_ell.html', args)
        else:
            return HttpResponse('справочник не найдена')