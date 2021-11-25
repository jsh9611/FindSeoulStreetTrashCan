import json
from django.shortcuts import render
from haversine import haversine

def results(request):

    lati = float(request.POST.get("lati"))
    long = float(request.POST.get("long"))
    with open('map/static/json/seoul_data.json', encoding='utf-8') as json_file:
        json_data = json.load(json_file)

    map_dic = {}
    map_dic['item0'] = "{\"id\": 0, \"borough\": \"\", \"street\": \"\", \"location\": \"내 위치\", \"latitude\": "+str(lati)+", \"longitude\": "+str(long)+"}"

    i=1
    for item in json_data:
        distance = haversine( (lati,long),(item['latitude'], item['longitude']) ) * 1000
        if distance > 500:
            continue
        map_dic['item'+str(i)] = ( json.dumps(item,ensure_ascii=False) )
        i += 1
    context ={'result' : map_dic}

    return render(request, 'page/map2.html', context)

def showmap(request):
    return render(request, 'page/map.html')


def results_eng(request):

    lati = float(request.POST.get("lati"))
    long = float(request.POST.get("long"))
    with open('map/static/json/seoul_data.json', encoding='utf-8') as json_file:
        json_data = json.load(json_file)

    map_dic = {}
    map_dic['item0'] = "{\"id\": 0, \"borough\": \"\", \"street\": \"\", \"location\": \"내 위치\", \"latitude\": "+str(lati)+", \"longitude\": "+str(long)+"}"

    i=1
    for item in json_data:
        distance = haversine( (lati,long),(item['latitude'], item['longitude']) ) * 1000
        if distance > 500:
            continue
        map_dic['item'+str(i)] = ( json.dumps(item,ensure_ascii=False) )
        i += 1
    context ={'result' : map_dic}

    return render(request, 'page/eng_map2.html', context)

def showmap_eng(request):
    return render(request, 'page/eng_map.html')