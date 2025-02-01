def pfix( infix):
        st=[]
        postfix=''

        operators={
            '+':1, '-':1,
            '*':2, '/':2,
            '^':3, '(':3
        }
        for ch in infix:
            if ch in '0123456789':
                postfix+=ch
            elif ch=='(':
                st.append(ch)
            elif ch == ')':
                while st and st[-1]!='(':
                    postfix+=st.pop()
                st.pop()
            elif ch in operators:

                while st and st[-1]!=')' and operators[ch]>=operators[st[-1]]:
                    postfix+=st.pop()
                st.append(ch)
        while st:
            postfix+=st.pop()

        return postfix

def calculate( s):
        """
        :type s: str
        :rtype: int
        """
        postfix=pfix(s)
        print(postfix)
        st=[]
        operators={
            '+':1, '-':1,
            '*':2, '/':2,
            '^':3, '(':3
        }
        for ch in postfix:
            if ch in '0123456789':
                st.append(int(ch))
            if ch in operators:
                a,b=st.pop(),st.pop()

                if ch=='-':
                    st.append(b-a)
                else:
                    st.append(b+a)
            
            
        print(st)

        return st[-1]



# print(calculate(" 2-1 + 2 "))
print(calculate("1-(     -2)"))
print(calculate("(1+(4+5+2)-3)+(6+8)"))