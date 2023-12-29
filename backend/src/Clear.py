from src.DataStore import data_store

def clear():
    '''
    Resets the internal data of the application to its initial state

    Arguments:
        N/A

    Exceptions:
        N/A

    Return Value:
        Returns an empty dictionary
    '''
    store = data_store.get()
    store['users'] = []
    return {}   