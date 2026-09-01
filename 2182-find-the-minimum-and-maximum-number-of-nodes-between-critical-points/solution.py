# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        pos=2
        crit_points=[]
        while head.next.next:
            if((head.next.val < head.val and head.next.val<head.next.next.val) or (head.next.val>head.val and head.next.val>head.next.next.val) ):
                crit_points.append(pos)
            pos+=1
            head = head.next
        if (len(crit_points)<2):
            return [-1, -1]
        else:
            minDistance=0
            for n in range(0, len(crit_points)-1 ):
                if( (crit_points[n+1] - crit_points[n] < minDistance) or (minDistance==0) ):
                    minDistance=crit_points[n+1] - crit_points[n]
            maxDistance=crit_points[-1]-crit_points[0]
            return[minDistance,maxDistance]

            
