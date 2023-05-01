import pyodbc


def get_connection():
    options = Options()
    connection = pyodbc.connect(options.connection_string)
    return connection


