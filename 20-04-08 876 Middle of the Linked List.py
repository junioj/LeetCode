# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        x=head
        k=0
        while(x!=None):
            x = x.next
            k = k+1
        # print(k)
        
        q=0
        if(k%2==0):
            q=k/2+1
        else:
            q=(k+1)/2
        
        # print(q)
        
        x=head
        g=1
        # u=0
        n=ListNode(0)
        while(x!=None):
            # u=x
            # print(u)
            if(g==q):
                n=x
                break
            x=x.next
            g=g+1
            
        # for g in range(0,k):
        #     u=x.next
        #     if(g>k/2):
        #         n.append(u)
                
        return n