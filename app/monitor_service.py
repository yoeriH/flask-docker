import datetime

class MonitorService():

    def __init__(self):
        self.__apps = []

    def create(self, name):
        app = {'name': name, 'id': self.__next_id() , 'status':[]}
        self.__apps.append(app)
        return app

    def find(self, id):
        return self.__find(id)

    def all(self):
        return self.__apps

    def update(self, id, status):
        id = int(id)
        status_object = {'status': status, 'created_at':self.__current_time()}
        self.__apps[id]['status'].append(status_object)
        return self.__find(id)

    def remove(self, id):
        self.__apps.pop(id)


    def __find(self, id):
        return self.__apps[id]

    def __current_time(self):
        return  str(datetime.datetime.now())

    def __next_id(self):
        return  len(self.__apps)
