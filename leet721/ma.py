class Solution:
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        merged_accounts = []
        for account in accounts:
            s = set(account[1:])
            to_merge = []
            for i, m in enumerate(merged_accounts):
                _, subset = m
                if s.intersection(subset):
                    to_merge.append(i)
            for i in to_merge:
                name, subset = merged_accounts[i]
                s = s.union(subset)
            merged_accounts = [a for i, a in enumerate(merged_accounts) if i not in to_merge]
            merged_accounts.append((account[0], s))
        return [[name] + list(sorted(emails)) for name, emails in merged_accounts]


def test():
    solution = Solution()
    accounts = [
        ["John", "johnsmith@mail.com", "john00@mail.com"], 
        ["John", "johnnybravo@mail.com"], 
        ["John", "johnsmith@mail.com", "john_newyork@mail.com"], 
        ["Mary", "mary@mail.com"]
    ]
    print(solution.accountsMerge(accounts))

if __name__ == "__main__":
    test()