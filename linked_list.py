class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    
    def __init__(self):
        self.head = None
        self.length = 0
        self.last = None
    
    def append(self, value):
        temp_node = Node(value)
        if self.head == None and self.last == None:
            self.head = temp_node
            self.last = temp_node
            self.length += 1
        else:
            # print(value, temp_node.__dict__, self.last.__dict__)
            self.last.next = temp_node
            self.last = temp_node
            self.length += 1
    
    def insert(self, position, value):
        if position >= self.length:
            print("postion greater than length appending to end")
            self.append(value)
        else:
            temp_node = Node(value)
            if position == 0:
                temp_node.next = self.head
                self.head = temp_node
                self.length += 1
            else:
                temp_head = self.head
                for index in range(self.length):
                    if index == position - 1:
                        temp_head.next, temp_node.next = temp_node, temp_head.next
                        self.length += 1
                        break
                    temp_head = temp_head.next
    
    def pop(self, *args):
        position_flag = False
        position = None
        if self.length == 0:
            print("no element to pop")
        else:
            if args and args[0] < self.length - 1:
                position = args[0]
                if position > self.length:
                    print("index greater than length popping last element")
                    position = self.length - 1
            else:
                position = self.length - 1
                position_flag = True
                
            temp_head = self.head
            
            if self.length == 1:
                print("poppped %s" %(self.head.data))
                self.head = None
                self.length = 0
                self.last = None
            else:
                if position == 0:
                    print("poppped %s" %(temp_head.data))
                    self.head = self.head.next
                    self.length -= 1
                else:
                    for index in range(self.length):
                        if index == position - 1:
                            print("poppped %s" %(temp_head.next.data))
                            temp_head.next = temp_head.next.next
                            self.length -= 1
                            if position_flag:
                                self.last = temp_head
                                print(self.last.__dict__)
                            break
                        temp_head = temp_head.next
    
    def delete(self, value):
        del_flag = True
        if self.length == 0:
            print("No item to delete")
        elif self.length == 1:
            if self.head.data == value:
                print("popped %s" %(self.head.data))
                self.head = None
                self.length -= 1
                self.last = None
                del_flag = False
            else:
                print("No item to delete")
        else:
            temp_head = self.head
            for index in range(self.length):
                if temp_head.data == value:
                    self.pop(index)
                    del_flag = False
                    break
                temp_head = temp_head.next
        if del_flag:
            print("element not found")
    
    def index(self, value):
        in_flag = True
        if self.length == 0:
            print("empty list no element found")
        else:
            temp_head = self.head
            for index in range(self.length):
                if temp_head.data == value:
                    print("index is %s" %(index))
                    in_flag = False
                    break
                temp_head = temp_head.next
        if in_flag:
            print("element not found")
    
    def print_linked_list(self):
        temp_head = self.head
        while temp_head:
            print(temp_head.data, end="-->")
            temp_head = temp_head.next
        print("\n")

ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.print_linked_list()
ll.delete(10)
ll.print_linked_list()
ll.delete(20)
ll.print_linked_list()
ll.delete(30)
ll.print_linked_list()
ll.append(10)
ll.append(20)
ll.append(30)
ll.print_linked_list()
ll.pop()
ll.print_linked_list()
ll.pop()
ll.print_linked_list()
ll.pop()
ll.print_linked_list()
ll.insert(0, 10)
ll.insert(0, 20)
ll.insert(0, 30)
ll.index(20)
ll.delete(3333)
ll.print_linked_list()
print(ll.__dict__)
