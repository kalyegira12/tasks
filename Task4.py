class employee:
    def work(self):
        print(f"Employee is working")

class manager(employee):
    def work(self):
        print(f"manager is managing the team")    

class developer(manager):
    def work(self):
        print(f"Developer is writing code")    

manager = manager()
developer = developer() 

manager.work()
developer.work()