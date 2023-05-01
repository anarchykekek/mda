class ClientRepository:
    def __init__(self):
        self.__options=Options()

    def statusOfClients(self):
        cursor = get_connection().cursor()
        query = self.__options.status_of_clients
        cursor.execute(query)
        return cursor.fetchall()

    def workersOfServices(self):
        cursor = get_connection().cursor()
        query = self.__options.workers_of_services
        cursor.execute(query)
        return cursor.fetchall()

    def clientsSale(self):
        cursor = get_connection().cursor()
        query = self.__options.clients_sale
        cursor.execute(query)
        return cursor.fetchall()

    def comeOfAge(self):
        cursor = get_connection().cursor()
        query = self.__options.come_of_age
        cursor.execute(query)
        return cursor.fetchall()

    def clientsRedemption(self):
        cursor = get_connection().cursor()
        query = self.__options.clients_redemption
        cursor.execute(query)
        return cursor.fetchall()

    def addClient(self, client):
        cnc = get_connection()
        cursor = cnc.cursor()
        query = self.__options.add_client + f" '{client.NameClient}', {client.Area}, {client.Address}, {client.Age}, {client.Id_Status}"
        cursor.execute(query)
        cnc.commit()
        cnc.close()


