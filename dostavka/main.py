b = WorkerRepository()
tr = b.revenueFromOrders()
for i in tr:
    print(i)


p = WorkerInputModel()
p.NameWorker = "Evgeni"
p.Post = "korobki"
p.Timetable = "every day"
p.PricePerJob = 30
p.IsDelited = False

b.addWorker(p)


