

def gather_data():
    """
    Simulates data gathering and returns a dictionary with realistic sample data.
    """
    return {'name': 'Jane Doe', 'age': 28, 'city': 'New York', 'country': 'USA', 'enrolled': True}

def process_data(data, foo):
    """
    Process the data dictionary by adding a new key-value pair where the key 
    is 'processed' and the value is True.
    """
    breakpoint()
    data['processed'] = True
    return data
