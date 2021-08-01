from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.http import JsonResponse, request
import os,time,json
# Create your views here.
from .person_sch import Person_schedule
room_arr = []
person_arr = []
person_schedule_dict = {}
room_schedule_dict={}
def create_task(date,start_time,end_time,roomID,person_arr_temp)->bool:
    count = 0
    global person_schedule_dict
    for person_temp in person_arr_temp:
        #print(person_temp)
        count += 1
        if(not person_temp.create_meeting(date,start_time,end_time,roomID)):
            print("Person not free")
            #print(person_schedule_dict)
            return False
    return True




def api_json(request):
    # print(request.POST)
    data = request.body.decode('utf-8')
    person_schedule_dict = json.loads(data)
    
    for users,task_info in person_schedule_dict["user"].items():
        #print(users,task_info)
        person_obj = Person_schedule(users)
        #print(users,"-->",task_info)
        for date,times in task_info.items():
            #print(date,times)
            for time_t in times:
                person_obj.create_meeting(date=int(date),start_time=int(time_t['start']),end_time=int(time_t['end']),roomID=time_t['roomID'])
        person_arr.append(person_obj)
    # for per in person_arr:
    #     per.show_meetings()
    
    if(len(person_arr)>0):
        return JsonResponse({'status':'success'})
    return JsonResponse({'status':'fail'})

def api_create_meetings(request):
    
    data = request.body.decode('utf-8')
    person_schedule_dict = json.loads(data)
    #person_schedule_dict = {"person":["p1","p2","p3"],"date":5082021,"start":1030,"end":1100,"roomID":"r1"}
    date = person_schedule_dict["date"]
    start_time = person_schedule_dict["start"]
    end_time = person_schedule_dict["end"]
    roomID = person_schedule_dict["roomID"]
    person_ids = person_schedule_dict["person"]
    for id in person_ids:
        person = Person_schedule(personID=id)
        person_arr.append(person)
    if create_task(date,start_time,end_time,roomID,person_arr):
        # for per in person_arr:
        #     per.show_meetings()
        return JsonResponse({'success':'pass'})
    return JsonResponse({'success':'fail'})

def index(request):
    return HttpResponse("HEllo WOrld")