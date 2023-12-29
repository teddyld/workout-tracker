initial_object = {
    'users': [],
}

class DataStore:
    def __init__(self):
        self.__store = initial_object

    def get(self):
        return self.__store

    def set(self, store):
        self.__store = store
        
        
global data_store
data_store = DataStore()