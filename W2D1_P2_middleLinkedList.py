class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)
        self.tail = self.head

    def insert(self, value):
        newNode = Node(value)
        self.tail.next = newNode
        self.tail = newNode


def printLinkedList(head):
    currentNode = head
    array = []
    while(currentNode != None):
        # print(currentNode.value)
        array.append(currentNode.value)
        currentNode = currentNode.next
    print(array)

# Approach 1: Time Complexity O(n), space O(1)


def middleNode(head):
    llistLength = 0
    currentNode = head
    # Find the Length of the List
    while currentNode:
        currentNode = currentNode.next
        llistLength += 1
    print(llistLength)
    # Transerve to the Middle Index = llistLength // 2
    # Note: // is divde, then floor the result

    currentNode = head
    index = 0
    mid = llistLength//2
    while (currentNode and index < llistLength):
        if index == mid:
            return currentNode
        else:
            currentNode = currentNode.next
            index += 1

# Approach 2: Time Complexity O(n), space O(1)
# with less memory used in compare with Approach 1


def middleNode2(head):
    slow = fast = head
    while(fast and fast.next):
        fast = fast.next.next
        slow = slow.next
    return slow


# Code execution starts here
if __name__ == '__main__':
      # Start with the empty list
    llist = LinkedList(1)
    llist.insert(2)
    llist.insert(3)
    llist.insert(4)
    llist.insert(5)
    llist.insert(6)

    printLinkedList(llist.head)

    result = middleNode2(llist.head)
    printLinkedList(result)
