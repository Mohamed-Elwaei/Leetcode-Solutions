class Solution(object):
    def sortTheStudents(self, score, k):
        """
        :type score: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        rows=[]
        for i,row in enumerate(score):
            tmp=[]
            tmp.append(row[k])
            tmp.append(row)   
            rows.append(tmp)
        rows=sorted(rows,key=lambda row: row[0],reverse=True)
        for i,row in enumerate(score):
            score[i]=rows[i][1]
        return score
            