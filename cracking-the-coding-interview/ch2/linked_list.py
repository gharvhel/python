import random

class Linked_list:
    def __init__(self):
        self.head = None
        self.size = 0

    # Imbedded Node class
    class Node:
        def __init__(self, data, next = None):
            self.data = data
            self.next = next

    def append(self, data):
        new_node = self.Node(data)
        if self.size == 0:
            self.head = new_node
        else:
            walker = self.head
            while walker.next is not None:
                walker = walker.next
            walker.next = new_node
        self.size += 1
        return self.head

    def delete(self, data):
        if self.size == 0:
            return self.head
        elif self.head.data == data:
            self.head = self.head.next
        else:
            walker = self.head
            while walker and walker.next is not None:
                if walker.next.data == data:
                    walker.next = walker.next.next
                walker = walker.next
        self.size -= 1
        return self.head

    def __str__(self):
        ch_arr = []
        ch_arr.append('[ ')
        walker = self.head
        while walker is not None:
            ch_arr.append(str(walker.data) + ' -> ')
            walker = walker.next
        ch_arr.append(' Null ] {SIZE:' + str(self.size) + '}' )
        return ''.join(ch_arr)

    """
    2.1 Remove Dups: Write code to remove duplicates from an unsorted list.
    FOLLOW UP
    How would you solve this problem if a temporary buffer is not allowed?
    """
    # Using additional space
    def remove_dups_1(self):
        if self.size < 2:
            return self.head
        seen = set()
        walker = self.head
        previous = None
        while walker is not None:
            if walker.data in seen:
                previous.next = walker.next
                self.size -= 1
            else:
                seen.add(walker.data)
                previous = walker
            walker = walker.next
        return self.head

    def remove_dups_2(self):
        if self.size < 2:
            return self.head    # Cannot be any duplicates

        walker = self.head
        while walker is not None:
            runner = walker
            while runner.next is not None:
                if runner.next.data == walker.data:
                    runner.next = runner.next.next
                    self.size -= 1
                else:
                    runner = runner.next
            walker = walker.next

    def kth2last1(self, k):
        """
        4->6->7->None, 2 = 6
        """
        distance = self.size - k
        walker = self.head
        while distance:
            walker = walker.next
            distance -= 1
        return walker.data



if __name__=='__main__':
    l = Linked_list()

    for i in [1,5,2,3,4,5,5,6,7,8,5,5,9,10]:
        l.append(i)
    print(l)

    l.delete(4)
    l.delete(1)
    l.delete(10)
    print(l)

    l.remove_dups_1()
    print(l)

    for i in [1,5,2,3,4,5,5,6,7,8,5,5,9,10]:
        l.append(i)
    print(l)

    l.remove_dups_2()
    print(l)

    print(l.kth2last1(2))
    print(l.kth2last1(4))
