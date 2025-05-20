from typing import List

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        found = set()

        for email in emails:
            local, domain = email.split('@', 1)
            cleaned_local = local.partition('+')[0].replace('.', '') 
            found.add(f"{cleaned_local}@{domain}")

        return len(found)
