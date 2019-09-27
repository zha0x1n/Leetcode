# ----------------First try--------------------------------------
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        sum1,sum2=0,0
        i,j=0,0
        while(l1!=None):
            sum1+=l1.val*10**i
            l1=l1.next
            i=i+1
        while(l2!=None):
            sum2+=l2.val*10**j
            l2=l2.next
            j=j+1
        sum=sum1+sum2
        print(sum)
        n=1
        l0=ListNode(0)
        while(sum!=0):
            l=ListNode(sum%10)
            if n==1:
                l0=l
            else:
                ll.next=l
            sum=sum//10
            n=n+1
            ll=l
        return l0
#------------------------Key----------------------------------
class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        re = ListNode(0)
        r=re
        carry=0
        while(l1 or l2):
            x= l1.val if l1 else 0
            y= l2.val if l2 else 0
            s=carry+x+y
            carry=s//10
            r.next=ListNode(s%10)
            r=r.next
            if(l1!=None):l1=l1.next
            if(l2!=None):l2=l2.next
        if(carry>0):
            r.next=ListNode(1)
        return re.next
#-------------------------Retry--------------------------------------
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res=ListNode(0)
        carry=0
        re=res
        while(l1 or l2):
            x=l1.val if l1!=None else 0
            y=l2.val if l2!=None else 0
            s=x+y+carry
            carry=s//10
            re.next=ListNode(s%10)
            re=re.next
            if l1 !=None:l1=l1.next
            if l2 !=None:l2=l2.next
        if(carry!=0):
            re.next=ListNode(1)
        return res.next
