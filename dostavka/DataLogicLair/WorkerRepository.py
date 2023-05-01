class WorkerRepository:
    def __init__(self):
        self.__options = Options()

    def moneyForOrder(self):
        cursor = get_connection().cursor()
        query = self.__options.money_for_order
        cursor.execute(query)
        return cursor.fetchall()

    def revenueFromOrders(self):
        cursor = get_connection().cursor()
        query = self.__options.revenue_from_orders
        cursor.execute(query)
        return cursor.fetchall()

    def WorkersSalary(self):
        cursor = get_connection().cursor()
        query = self.__options.workers_salary
        cursor.execute(query)
        return cursor.fetchall()

    def addWorker(self, worker):
        cnc = get_connection()
        cursor = cnc.cursor()
        query = self.__options.add_worker + f" '{worker.NameWorker}', {worker.Post}, {worker.Timetable}, {worker.PricePerJob}, {worker.IsDelited}"
        cursor.execute(query)
        cnc.commit()
        cnc.close()


