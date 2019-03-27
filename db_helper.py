import sqlite3

def make_mapped(descriptor, response_list):
    headers = [d[0] for d in descriptor]
    return [{headers[i]:response[i] for i in range(len(response))} for response in response_list]