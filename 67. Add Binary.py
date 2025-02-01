class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        maxlen=len(a) if len(a)>len(b) else len(b)
        carry=0
        out=''
        for i in range(-1,-maxlen-1,-1):
            inta=int(a[i]) if i>=-len(a) else 0
            intb=int(b[i]) if i>=-len(b) else 0
            out+=str(inta^intb^carry)
            if inta+intb+carry>=2:
                carry=1
            else:
                carry=0
        if carry:
            out+='1'       
        return out[::-1]        