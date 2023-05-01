class Options:
    def __init__(self):
        self.connection_string = 'DRIVER={SQL Server};SERVER=HOME-PC\SQLEXPRESS;DATABASE=tablet;'
        self.status_of_clients = 'exec statusOfClients'
        self.workers_of_services='exec workersOfServices'
        self.clients_sale = 'exec ClientsSale'
        self.come_of_age = 'exec ComeOfAge'
        self.clients_redemption = 'exec ClientsRedemption'
        self.add_client = 'exex AddClient'

        self.money_for_order = 'exec moneyForOrder'
        self.revenue_from_orders = 'exec RevenueFromOrders'
        self.workers_salary = 'exec WorkersSalary'
        self.add_worker = 'exec AddWorker'

