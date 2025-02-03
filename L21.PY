#給你兩個 已排序的鏈表（Linked List） list1 和 list2，請你將它們合併成一個新的排序鏈表，並返回新的鏈表頭節點。


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1, list2):
    if not list1: 
        return list2
    if not list2: 
        return list1
    
    if list1.val < list2.val:
        list1.next = mergeTwoLists(list1.next, list2)
        return list1
    else:
        list2.next = mergeTwoLists(list1, list2.next)
        return list2

def list_to_linked_list(lst):
    """將 Python list 轉換為 ListNode"""
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for val in lst[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def linked_list_to_list(node):
    """將 ListNode 轉回 Python list"""
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

# 轉換輸入
l1 = list_to_linked_list([1, 2, 4])
l2 = list_to_linked_list([1, 3, 4])

# 合併鏈結串列
merged = mergeTwoLists(l1, l2)

# 轉回 Python list 輸出
print(linked_list_to_list(merged))  # 輸出: [1, 1, 2, 3, 4, 4]
