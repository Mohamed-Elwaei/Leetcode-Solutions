class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        S = set()

        for email in emails:
            local,domain = email.split('@')

            formatted_local = ''
            for c in local:
                if c == '+': break
                if c != '.':
                    formatted_local += c
            new_email = formatted_local + '@' + domain
            print(new_email)
            S.add(new_email)
        return len(S)