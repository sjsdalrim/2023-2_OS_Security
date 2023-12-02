class Node :
    def __init__(node_c, val) :
        node_c.val = val
        node_c.next = None

class LinkedList :
    def __init__(list) :
        null = Node("null")
        list.head = null
        list.tail = null

        list.current = None
        list.before = None

        list.num_of_data = 0;
