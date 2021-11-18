import json, csv, random
class Building:
    def __init__(self, file_name):
        with open(file_name, "r") as fp:
            di = json.load(fp)
            self._minFloor = int(di["_minFloor"])
            self._maxFloor = int(di["_maxFloor"])
            self._elevators = []
            elev = di["_elevators"]
            for k in elev:
                self._elevators.append(Elevator(k))
class Elevator:
    def __init__(self, di):
        self._id = int((di["_id"]))
        self.speed = float(di["_speed"])
        self._minFloor = int(di["_minFloor"])
        self._maxFloor = int(di["_maxFloor"])
        self._closeTime = float(di["_closeTime"])
        self._openTime = float(di["_openTime"])
        self._startTime = float(di["_startTime"])
        self._stopTime = float(di["_stopTime"])
        self.countP = {}
        for i in range(self._minFloor, self._maxFloor+1):
            self.countP[i] = 0
        self.timeS = 0
        self.work = 0
        self.Sfloor = 0
        self.Efloor = 0
        self.other =None
        self.door = self._openTime + self._closeTime + self._stopTime + self._startTime


    def type(self):
        if self.Sfloor - self.Efloor == 0: return 0
        if self.Sfloor - self.Efloor > 0: return -1
        if self.Sfloor - self.Efloor < 0: return 1


class CallForElevator:
    def __init__(self, data):
        self.name = data[0]
        self.time = float(data[1])
        self.src = int(data[2])
        self.dest = int(data[3])
        self.state = int(data[4])
        self.elevator = int(data[5])

    def type(self):
        if self.src -self.dest > 0: return -1
        if self.src - self.dest < 0: return 1


def cmd(calls: CallForElevator, el: list[Elevator]):
    for c in calls:
        # min = abs(el[0].work - el[0].goto(c.src))
        for e in el:
            if e.work <= c.time:
                print("Re")
                restart(e)
            if e.type() == 0:
                update(c,e)
                c.elevator = e._id
                break
            # if goto(c.src,e) > c.time:


        if(c.elevator==-1):
            print(f"{e.Efloor} , {e._id}, {e.timeS} , work ={e.work}")
            c.elevator = random.randint(0,9)


def restart(e):
    e.timeS = e.work
    e.work =0
    e.Efloor = e.Sfloor


def goto(c:int, e:Elevator):
    temp = e.timeS + abs(e.Sfloor - c) *e.speed + e.countP[c]*e.door
    return temp




    return temp
def update(c:CallForElevator, e:Elevator):
        if e.type() >-1 and c.type()==1:
            if e.Efloor<c.dest:
                e.Efloor =c.dest
        for i in range(c.src, e._maxFloor):
            if i >= c.dest:
                e.countP[i] +=1
            e.countP[i] +=1

        if e.type() < 1 and c.type()==-1:
            if e.Efloor > c.dest:
                e.Efloor =c.dest
            for i in range(c.src, e._minFloor):
                if i <= c.dest:
                    e.countP[i]+= 1
                e.countP[i] += 1
        e.work = e.timeS + abs(e.Efloor - e.Sfloor) * e.speed + e.door * (e.countP[c.src])





def readCalls(file_name):
    calls = []
    with open(file_name, "r") as fp:
        data = csv.reader(fp)
        for k in data:
            calls.append(CallForElevator(k))
    return calls


def writeCalls(calls):
    dataCalls = []
    for k in calls:
        dataCalls.append(k.__dict__.values())
    with open("output.csv", "w", newline="") as fu:
        csvwriter = csv.writer((fu))
        csvwriter.writerows(dataCalls)


def main():
    building = Building("other\B5.json")
    calls = readCalls("other\Calls_c.csv")
    cmd(calls, building._elevators)
    writeCalls(calls)
    print("end")


if __name__ == '__main__':
    main()
