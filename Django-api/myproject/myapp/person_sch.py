import json

# file_open =  open("schedule.json")

# data = json.load(file_open)
# file_open.close()

class Person_schedule:
    """
    format date = 5082021 DDMMYYY
    format time = 1000 # 10:00 AM, 2000  # 08:00 PM
    remainder = {date:{start:start_time,end:end_time}}

    """
    def __init__(self,personID=0) -> None: # Constructor
         # A Dictionary for Ease of Access
        self.remainder = {}
        self.start_day_time = 1000 # 10:00 AM
        self.end_day_time  = 2000  # 08:00 PM
        self.personID = personID
        self.remainder[personID] = {}
        
        #self.count_task = 0
    def create_meeting(self,date,start_time,end_time,roomID=0) -> bool:
        if start_time < self.start_day_time or end_time > self.end_day_time or start_time >=end_time:
            return False
        #self.count_task += 1
        if date not in self.remainder[self.personID]:
            if(self.personID):
                temp = [{"start":start_time,"end":end_time,"roomID":roomID}]
                self.remainder[self.personID][date] = temp
                #print("Successfully added")
                return True
        else:
            for i in self.remainder[self.personID][date]:
                if(start_time>=i["start"] and start_time<=i["end"]) or (end_time>=i["start"] and end_time<=i["end"]):
                    #print("Collision")
                    return False
            
            if(self.personID):
                temp = [{"start":start_time,"end":end_time,"roomID":roomID}]
                self.remainder[self.personID][date] += temp
                #print("Successfully added")
                return True

    def show_meetings(self,date=None)->None:
        if(not date):
            if (not self.remainder):
                print("Empty")
            else:
                print(self.remainder)
        else:
            print(self.remainder[date])
    def get_remainder(self)->dict:
        return self.remainder