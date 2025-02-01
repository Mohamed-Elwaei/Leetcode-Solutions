

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        if not lists:
            return 
        minHeap=[]



        for k in lists:
            if k:
                heapq.heappush(minHeap, (k.val, k))
        
        head=None
        curr=head

        while minHeap:
            tmp=heapq.heappop(minHeap)
            if not head:
                head=ListNode(tmp[0])
                curr=head
            else:
                curr.next=ListNode(tmp[0])
                curr=curr.next
            if tmp[1]:
                heapq.heappush(minHeap, (tmp[1].val,tmp[1]))
        return head
