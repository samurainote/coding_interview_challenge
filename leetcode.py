

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        answers = []
        switch = False
        l = zip(l1, l2)
        for n1, n2 in l:
            if switch == True:
                answer = n1 + n2 + 1
            if switch == False:
                answer = n1 + n2
            if 10 <= answer:
                answers.append(answer - 10)
                switch = True
            else:
                answers.append(answer)
                switch = False

        return answers

l1 = [2,4,3]
l2 = [5,6,4]
s = Solution()
answers = s.addTwoNumbers(l1, l2)
print(answers)
