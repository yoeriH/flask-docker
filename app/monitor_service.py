import datetime

class MonitorService():
    def __init__(self):
        self.__monitors = []

    def create(self, name):
        monitor = Monitor(name, self.__next_id(), 1)
        self.__monitors.append(monitor)
        return monitor.to_object()

    def find(self, id):
        return self.__find(id).to_object()

    def all(self):
        results = []
        for monitor in self.__monitors:
            results.append(monitor.to_object())
        return results

    def update(self, id, status):
        id = int(id)
        status_object = {'status': status, 'created_at': datetime.datetime.now()}
        self.__monitors[id].add_status(status_object)
        return self.__find(id).to_object()

    def remove(self, id):
        id = int(id)
        self.__monitors.pop(id)

    def __find(self, id):
        id = int(id)
        return self.__monitors[id]

    def __next_id(self):
        return  len(self.__monitors)

class Monitor():
    def __init__(self, name, id, priority):
        self.name = name
        self.id = id
        self.priority = priority
        self.__stati = []

    def id(self):
        return self.id

    def report(self):
        if len(self.__stati) > 1:
            time_passed = datetime.datetime.now() - self.__stati[-2]['created_at']
            health = 100 - time_passed.seconds * self.priority
            print(time_passed.seconds)
            return {'health': health}
        else:
            return {'health': False, 'message': 'no status recieved'}


    def add_status(self, status):
        self.__stati.append(status)

    def to_object(self):
        return {'id': self.id, 'name': self.name, 'priority': self.priority, 'status': self.report()}
