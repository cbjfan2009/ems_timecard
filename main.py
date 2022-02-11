import datetime, time, tkinter
times_list = []
class Employees:
    def __init__(self, name,user_id, user_password,start_time,end_time,hours_worked):
        self.name = name
        self.user_id = user_id
        self.user_password = user_password
        self.start_time = start_time
        self.end_time = end_time
        self.hours_worked = hours_worked

    def create_employee(self):
        print("New Employee Information")
        name = input("Employee's Name: ")
        user_id = input("User ID: ")
        user_password = input("User Password: ")
        print("Employee Added Successfully!")
        return

def clock_in():
    clock_in = datetime.datetime.now()
    x = int(clock_in.strftime("%H%M%S"))
    return x


#employees = {"Matt": {"Date": {"Clock In", "Clock Out"}}, "Ken": {"Date": {"Clock In", "Clock Out"}}, "Sherry": {"Date": {"Clock In", "Clock Out"}}}

#print(employees["Matt"]["Date"])
time_sheet_list =[
  {
     "name": "john",
     "times": [
         {
             "time_in": "4-10-2020 04:20:20", # date time format in whatever database youre using
             "time_out": "4-10-2020 10:20:20",
          },
         {
             "time_in": "4-11-2020 07:20:20",
             "time_out": "4-11-2020 11:20:20",
          }
     ]
  },
  {
     "name": "sue",
     "times": [
         {
             "time_in": "4-10-2020 02:20:20", # date time format in whatever database youre using
             "time_out": "4-10-2020 11:20:20",
          },
         {
             "time_in": "4-11-2020 1:20:20",
             "time_out": "4-11-2020 17:20:20",
          }
     ]
  },
]

#print(time_sheet_list)

#for entries in time_sheet_list:
#    print (entries)
    #for key in indexes:
        #print(key)

#print(time_sheet_list[0]["times"][0]) #prints time in / time out from indexed position of 'times'

def print_times():
    print(time_sheet_list[0]["times"])

print_times()

clock_in()