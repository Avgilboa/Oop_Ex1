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
        self._speed = float(di["_speed"])
        self._minFloor = int(di["_minFloor"])
        self._maxFloor = int(di["_maxFloor"])
        self._closeTime = float(di["_closeTime"])
        self._openTime = float(di["_openTime"])
        self._startTime = float(di["_startTime"])
        self._stopTime = float(di["_stopTime"])
        self.direcion = 0
        self._currentFloor = 0
        self.time = 0
        self.calls = []

    def __str__(self):
        return f"{self._id} calls = {self.calls};;"

    def __repr__(self):
        return f"{self._id} calls = {self.calls} Dir: {self.direcion};;"

    def _lt_(self, other):
        if not isinstance(other, Elevator): return
        return self._currentFloor < other._currentFloor

    def _gt_(self, other):
        if not isinstance(other, Elevator): return
        return self._currentFloor > other._currentFloor

class CallForElevator:
    def __init__(self, data):
        self.name = data[0]
        self.time = float(data[1])
        self.src = int(data[2])
        self.dest = int(data[3])
        self.state = int(data[4])
        self.elevator = int(data[5])


def cmd(calls: list[CallForElevator], el: list[Elevator]):
    for k in calls:
        k.elevator =random.randint(0,9)



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


if __name__ == '__main__':
    main()

