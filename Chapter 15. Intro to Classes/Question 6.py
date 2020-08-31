from datetime import datetime


class SMS_store:

    def __init__(self):
        self.store = []

    def __str__(self):
        return ("{0}".format(self))

    def add_new_arrival(self, number, time, text):
        self.store.append(("Read: False", "From: " + number, "Recieved: " + time, "Msg: " + text))

    def message_count(self):
        return (len(self.store))

    def get_unread_indexes(self):
        result = []
        for (i, v) in enumerate(self.store):
            if v[0] == "Read: False":
                result.append(i)
        return (result)

    def get_message(self, i):
        msg = self.store[i - 1]
        msg = ("Read: True",) + msg[1:]
        self.store[i] = (msg)
        return (self.store[i][1:])

    def delete(self, i):
        del self.store[i]

    def clear(self):
        self.store = []


time = datetime.now().strftime('%H:%M:%S')
my_inbox = SMS_store()
my_inbox.add_new_arrival("0182349123",time,"Hello how are you?")
my_inbox.add_new_arrival("0123455521",time,"Why didn't you come to school?")

print(my_inbox.message_count())
print(my_inbox.get_unread_indexes())
print(my_inbox.get_message(1))