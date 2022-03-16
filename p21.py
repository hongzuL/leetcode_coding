# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2):
        if list1 == None and list2 == None:
            return None
        elif list1 == None:
            return list2
        elif list2 == None:
            return list1
        temp = ListNode(0,None)
        head = temp
        while list2 or list1:
            print(temp.val, list1.val, list2.val)
            
            if list1.val > list2.val:
                temp.val = list2.val
                list2 = list2.next
                if list2 is None:
                    temp.next = list1
                    break
                else:
                    temp.next = ListNode(0,None)
            else:
                temp.val = list1.val
                list1 = list1.next
                if list1 is None:
                    temp.next = list2
                    break
                else:
                    temp.next = ListNode(0,None)

            temp = temp.next
        return head

    def createLinkedList(self, list_vals):
        tmp = ListNode()
        head = tmp
        for i in range(len(list_vals)):
            tmp.val = list_vals[i]
            if i >= len(list_vals) - 1:
                tmp.next = None
            else:
                tmp.next = ListNode()
                tmp = tmp.next
        return head

    def printLinkedList(self, head):
        tmp = head
        while tmp:
            print(tmp.val)
            tmp = tmp.next

solut = Solution()
list1 = [1,2,4,5]
list2 = [1,3,4]
list1 = solut.createLinkedList(list1)
list2 = solut.createLinkedList(list2)
head = solut.mergeTwoLists(list1, list2)
solut.printLinkedList(head)