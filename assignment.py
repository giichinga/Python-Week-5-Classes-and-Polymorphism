#Assignment 1
class Job:
    def __init__(self, title, salary, location):
        self.title = title
        self._salary = salary      
        self.location = location

    def get_salary(self):   
        return f"Salary for {self.title} is ${self._salary}"

    def set_salary(self, new_salary): 
        if new_salary > 0:
            self._salary = new_salary
        else:
            print("Invalid salary amount.")

    def describe(self):
        return f"Job: {self.title}, Location: {self.location}"

class RemoteJob(Job):
    def __init__(self, title, salary, location, tools):
        super().__init__(title, salary, location)
        self.tools = tools

    def describe(self):
        return f"Remote Job: {self.title}, Tools: {', '.join(self.tools)}"

job1 = Job("Software Engineer", 80000, "New York")
print(job1.describe())
print(job1.get_salary())

remote_job = RemoteJob("Data Scientist", 90000, "Remote", ["Zoom", "Slack", "Jupyter"])
print(remote_job.describe())

 #Assignment 2

class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method!")

class Car(Vehicle):
    def move(self):
        print("🚗 Driving on the road!")

class Plane(Vehicle):
    def move(self):
        print("✈️ Flying in the sky!")

class Bicycle(Vehicle):
    def move(self):
        print("🚴 Pedaling on the path!")

vehicles = [Car(), Plane(), Bicycle()]

for v in vehicles:
    v.move()
