from ao3 import AO3
api = AO3()
test_work = api.work(id = "28885413")
print(test_work.fandoms)