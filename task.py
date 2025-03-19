import datetime

class Task:

    def __init__(self, name_init, priority_init):
        self.name = name_init
        self.priority = priority_init
        self.complete_status = False
        self.current_time = datetime.datetime.today()
        self.date_created = self.current_time.strftime("%m/%d/%Y")

    def task_completed(self):
        self.complete_status = True

    def set_priority(self, input_prior):
        self.priority = input_prior

    def toString(self):
        return ("\nName: " + self.name + "\n" +
                "Date Created: " + self.date_created + "\n" +
                "Priority: " + str(self.priority) + "\n" +
                "Complete Status: " + str(self.complete_status))


# test object
test = Task("Test", "Main Task")
test.task_completed()
print(test.toString())