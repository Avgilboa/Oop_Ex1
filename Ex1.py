import json, csv, random
import math


class Building:
    def __init__(self, file_name):
        with open(file_name, "r") as fp:
            di = json.load(fp)
            self._minFloor = di["_minFloor"]
            self._maxFloor = di["_maxFloor"]
            self._elevators = []
            elev = di["_elevators"]
            for k in elev:
                self._elevators.append(Elevator(k))

class Elevator:
    def __init__(self, di):
        self._id = di["_id"]
        self.speed = di["_speed"]
        self._minFloor = di["_minFloor"]
        self._maxFloor = di["_maxFloor"]
        self._closeTime = di["_closeTime"]
        self._openTime = di["_openTime"]
        self._startTime = di["_startTime"]
        self._stopTime = di["_stopTime"]
        self.direcion = 0
        self.currentFloor = 0
        self.max_call = 0
    def update_floor(self, time:float):
        dis = abs(time- self.time)



class CallForElevator:
    def __init__(self, data):
        self.name = data[0]
        self.time = data[1]
        self.src = data[2]
        self.dest = data[3]
        self.state = data[4]
        self.elevator = data[5]

def Time_work(call:CallForElevator, elev: Elevator):
    dis = abs(call.src - call.dest) * elev.speed
    start = abs(elev.currentFloor -elev.src) * elev.speed
    return dis + start

def readCalls(file_name):
    calls = []
    with open(file_name, "r") as fp:
        data = csv.reader(fp)
        for k in data:
            calls.append(CallForElevator(k))
    return calls

def choose(call: CallForElevator, elev:list[Elevator]):
    for i in elev:
        if()
def writeCalls(calls):
    dataCalls = []
    for k in calls:
        dataCalls.append(k.__dict__.values())
    with open("output.csv", "w", newline="") as fu:
        csvwriter = csv.writer((fu))
        csvwriter.writerows(dataCalls)
"""
functions for the choose elevators
"""
def is_empty(elevator):
    return elevator._currentFloor == maxCall(elevator)
#
#
# def get_pos():
# def direction():
# def num_of_people():
#     return
# def next_call():
def candidate_elevators(elev, call):
    list = []
    for i in elev:
        if elev.direcion == 0:
            list.append(elev)
        elif (elev.direcion == TypeCall(call)):
            list.append(elev)
    return list

def cal(elev:Elevator, num_cal: CallForElevator):
    return math.abs(elev._currentFloor)

def type_call(call):
    if((call.dest - call.src) > 0):
        return 1;
    return -1;

def list_calls(calls, num_of_elevators):
    list = []
    for i in range(num_of_elevators):
        list.append([])
    for i in calls,range(10):
        list[random.randint(0,len(list)-1)].append(i)
    print(list)

def chooseElevator(building, calls ):
    list_calls(calls,len(building._elevators) )
    for k in calls:
        k.elevator = random.randint(0, len(building._elevators)-1)




def main():
    building = Building("Ex1_input\Ex1_Buildings\B2.json")
    calls = readCalls("Ex1_input\Ex1_Calls\Calls_b.csv")
    # print((calls))
    chooseElevator( building, calls)
    writeCalls(calls)

if __name__ == '__main__':
    main()
