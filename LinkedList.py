class ListNode:
    def __init__(self, val, next=None):
        self.val = val #value of node
        self.next = next #next node

class SingleLinkedList:
    #store many node
    def __init__(self, head=None):
        self.head = head # first node

    def checkLenght(self):
        count = 0
        nowNode = self.head #start node position
        while nowNode != None: # until no Node
            count += 1
            nowNode = nowNode.next

        return count

    def addNode(self, newNode):
        if self.head == None:
            self.head = newNode
        else:
            pos = self.head
            while pos.next != None: #find the last position
                pos = pos.next
            pos.next = newNode
        
    def displayAllNode(self):
        pos = self.head
        while pos != None:
            print(pos.val)
            pos = pos.next

sll = SingleLinkedList()
sll.addNode(ListNode(19))
print(sll.checkLenght())
sll.addNode(ListNode(3))
print(sll.checkLenght())
sll.displayAllNode()