class Solution:
    def intToRoman(self, num: int) -> str:
        output=''
        M=num//1000
        num=num%1000
        CM=num//900
        num=num%900
        D=num//500
        num=num%500
        CD=num//400
        num=num%400
        C=num//100
        num=num%100
        XC=num//90
        num=num%90
        L=num//50
        num=num%50
        XL=num//40
        num=num%40
        X=num//10
        num=num%10
        IX=num//9
        num=num%9
        V=num//5
        num=num%5
        IV=num//4
        num=num%4
        I=num//1
        num=num%1
        output='M'*M+'CM'*CM+'D'*D+'CD'*CD+'C'*C+'XC'*XC+'L'*L+'XL'*XL+'X'*X+'IX'*IX+'V'*V+'IV'*IV+'I'*I        
        return output
