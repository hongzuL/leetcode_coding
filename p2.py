# 2. Add Two Numbers
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def p2(l1,l2):
    addone = 0
    output = list()
    while l1 is not None or l2 is not None or addone == 1:
        if l1 == None and l2 != None:
            if l2.val + addone >= 10:
                curr_digit = l2.val + addone  - 10
                addone = 1
            else:
                curr_digit = l2.val + addone
                addone = 0
            l2 = l2.next
        elif l2 == None and l1 != None:
            if l1.val+ addone >= 10:
                curr_digit = l1.val + addone  - 10
                addone = 1
            else:
                curr_digit = l1.val + addone
                addone = 0
            l1 = l1.next
        elif l1 == None and l2 == None:
                curr_digit = addone
                addone = 0
        else:
            if l1.val+l2.val+ addone >= 10:
                curr_digit = l1.val + l2.val + addone  - 10
                addone = 1
            else:
                curr_digit = l1.val + l2.val + addone
                addone = 0
            l1 = l1.next
            l2 = l2.next
        output.append(curr_digit)
        
    
    next_node = None

    for i in range(1,len(output)+1):
        output_node = ListNode(output[-i],next_node)
        next_node = output_node
    return output_node

def p2_list(l1, l2):
    # decide main list and side list (longer one or shorter one)
    if len(l1)>= len(l2):
        lm = l1
        ls = l2
    else:
        lm = l2
        ls = l1
    output = list()
    addone = 0
    for i in range(len(lm)):
        if i >= len(ls):
            output.append(lm[i]+addone)
            if lm[i] + addone >= 10:
                addone = 1
            else:
                addone = 0
        else:
            if lm[i] + ls[i] + addone >= 10:
                output.append(lm[i] + ls[i] - 10 + addone)
                addone = 1
            else:
                output.append(lm[i] + ls[i] + addone)
                addone = 0
    return output

def main():
    l1 = [9,9,9,9,9,9,9]
    l2 = [9,9,9,9]
    next_node = None

    for i in range(1,len(l1)+1):
        l1node = ListNode(l1[-i],next_node)
        next_node = l1node
    next_node = None
    for j in range(1,len(l2)+1):
        l2node = ListNode(l2[-j],next_node)
        next_node = l2node
    # print(l1node)
    ans = p2(l1node, l2node)
    while ans is not None:
        print(ans.val)
        ans = ans.next

main()