class Node(object):

    def __init__(self, value = None, next = None):

        self.value = value
        self.next = next

class LinkedList(object):



    def __init__(self, *args):

        self.first = None
        self.last = None
        self.leng = 0
        self.counter = -1

        for item in args:
            self.add(item)

    def add(self, value):

        if self.first == None:
            self.first = Node(value, None)
            self.last = self.first
            self.leng = 1
        else:
            self.last.next = self.last = Node(value, None)
            self.leng += 1

    def insert(self, index, value):
        if index == 0:
            self.leng += 1
            if self.first == None:
                self.first = Node(value, None)
                self.last = self.first
            else:
                self.first = Node(value, self.first)
                return

        if index >= self.leng:
            self.add(value)
        else:
            counter = 0
            elem = self.first
            while elem != None:
                counter += 1
                if counter == index:
                    elem.next = Node(value, elem.next)
                    self.leng += 1
                    if elem.next.next == None:
                        self.last = elem.next
                        self.leng += 1
                    break
                elem = elem.next

    def get(self, index):
        if index >= self.leng:
            raise IndexError

        counter = -1
        elem = self.first
        while elem != None:
            counter += 1
            if counter == index:
                return elem.value
            elem = elem.next

    def remove(self, value):

        elem = self.first
        while elem != None:

            if elem.value == value:
                if elem.next == None:
                    self.remove_at(self.leng - 1)
                    return

                elem.value = elem.next.value
                elem.next = elem.next.next
                self.leng -= 1
                return
            elem = elem.next

    def remove_at(self, index):

        if index >= self.leng:
            raise IndexError
        elem = self.first

        if index == 0:
            self.leng -= 1
            buf = self.first.value
            self.first = elem.next
            return buf
        counter = -1

        while elem != None:
            counter += 1
            if counter + 1 == index:
                buf = elem.next.value
                elem.next = elem.next.next
                self.leng -= 1
                return buf
            elem = elem.next

    def clear(self):
        self.__init__()

    def contains(self, value):

        elem = self.first
        while elem != None:
            if elem.value == value:
                return True
            elem = elem.next
        return False

    def len(self):
        return self.leng

    def is_empty(self):
        if self.first == None:
            return True
        else:
            return False

    def __str__(self):
        if self.first != None:
            elem = self.first
            output = 'LinkedList(' + str(elem.value) + ', '
            while elem.next != None:
                elem = elem.next
                output += str(elem.value) + ', '
            return output.rstrip(', ') + ')'
        return 'LinkedList()'

    def __iter__(self):
        return self

    def __next__(self):
        self.counter += 1
        if self.counter < self.leng:

            return self.get(self.counter)
        else:
            raise StopIteration