# Advance Task

from person_sch import Person_schedule
from room_sch import Room_schedule
import json

person_schedule_dict = {}
room_schedule_dict = {}
try:
    with open("pSchedule.json",'r') as file_p:
        person_schedule_dict.update(json.load(file_p))
    with open("rSchedule.json",'r') as file_p:
        room_schedule_dict.update(json.load(file_p))
except:
    person_schedule_dict["user"] = {}
    room_schedule_dict["roomID"] = {}


def create_task(date,start_time,end_time,room_arr,roomID,person_arr_temp,person_ids)->bool:
    count = 0
    global person_schedule_dict
    for person_temp in person_arr_temp:
        #print(person_temp)
        count += 1
        if(not person_temp.create_meeting(date,start_time,end_time,roomID)):
            print("Person not free")
            #print(person_schedule_dict)
            return False
    
    
    
    if(room_arr[int(roomID[1])-1].create_meeting(date,start_time,end_time,person_ids)):
        for ids in person_arr_temp:
            person_schedule_dict["user"].update(ids.get_remainder())
        for roomIds in room_arr:
            room_schedule_dict["roomID"].update(roomIds.get_remainder())
        
        with open("pSchedule.json",'w') as file_p:
        # data = json.load(file_p)
        # data["user"].update(person_schedule_dict)
        # file_p.seek(0)
            json.dump(person_schedule_dict,file_p,indent=2)
        with open("rSchedule.json",'w') as file_p:
            json.dump(room_schedule_dict,file_p,indent=2)
        return True
    print("RoomID : "+str(roomID)+" Free")
    return False


room_arr = []
person_arr = []
num=0

if len(room_schedule_dict["roomID"])>1:
    for keys,values in room_schedule_dict["roomID"].items():
        room = (Room_schedule(keys))
        for date,times in values.items():
            for time_t in times:
                room.create_meeting(int(date),int(time_t['start']),int(time_t['end']),time_t['personID'])
        room_arr.append(room)
else:
    room1 = Room_schedule("r1")
    room2 = Room_schedule("r2")
    room3 = Room_schedule("r3") 
    room4 = Room_schedule("r4")
    room5 = Room_schedule("r5")
    room_arr = [room1,room2,room3,room4,room5]

if len(person_schedule_dict["user"]) == 0:
    num = int(input("Please enter How many Person : "))
    for i in range(num):
        id = "p"+str(i)
        person = Person_schedule(personID=id)
        person_arr.append(person)

else:
    for users,task_info in person_schedule_dict["user"].items():
        #print(users,task_info)
        person_obj = Person_schedule(users)
        #print(users,"-->",task_info)
        num+=1
        for date,times in task_info.items():
            #print(date,times)
            for time_t in times:
                person_obj.create_meeting(date=int(date),start_time=int(time_t['start']),end_time=int(time_t['end']),roomID=time_t['roomID'])
        person_arr.append(person_obj)

    # for person in person_arr:
    #     person.show_meetings()



while(True):
    res = 0
    count_user = 0
    string = ""
    if(num):
        for i in range(num):
            string += " p"+str(i+1)

        print("Available User :"+string)
    else:
        print("Available User : ")
        for users,task_info in person_schedule_dict["user"].items():
            new_user = "p"+str(int(users[1])+1)
            num += 1 
        
            # print(new_user)

    
        
    
    person_id = input("Please Enter the Person ID: ex p1 == person1 : ").split(" ")
    person_arr_temp = []
    for i in person_id:
        number = int(i[1])
        if(number>num):
            res = 1
            break
        person_arr_temp.append((person_arr[number-1]))
    #print(person_arr_temp)
    if(res):
        break
    date = int(input("Please enter the date DMMYYY : "))
    start_time = int(input("Please Enter the start time 10:00 AM == 1000 : "))
    end_time = int(input("Please Enter the end time 10:00 AM == 1000 : "))
    roomID = int(input("Enter the scheduler ID 1,2,3,4,5 : "))
    roomID = "r"+str(roomID)
    if create_task(date = date,start_time= start_time,end_time = end_time,room_arr= room_arr,person_arr_temp= person_arr_temp,roomID=roomID,person_ids = person_id):
        print("Created Successfully")
        # for person in person_arr_temp:
        #     person.show_meetings()
        
    else:
        print("Collision")
        break



