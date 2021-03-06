# -*- coding: utf-8 -*-
# Created on Thu Nov 09 2017 10:31:55
# Author: WuLC
# EMail: liangchaowu5@gmail.com


# union find, two methods 
# method 1, perform path compression eventually and union with the hashmap parents 
# method 2, do not perform perform path compression eventually but union with find

## method 1
class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        owners, parents = {}, {}
        for account in accounts:
            owners[account[1]] = account[0]
            for i in xrange(1, len(account)):
                parents[account[i]] = account[i]
        
        for account in accounts:
            p = self.find(account[1], parents)
            for i in xrange(1, len(account)):
                parents[self.find(account[i], parents)] = p
        
        # not all paths are compressed currently
        for k, v in parents.items():
            if k!=v:
                parents[k] = self.find(parents[v], parents)
            
        unions = {}
        for k, v in parents.items():
            if v  not in unions:
                unions[v] = set()
            unions[v].add(k)
        
        result = []
        for k, v in unions.items():
            result.append([owners[k]] + sorted(v))
        return result
        
    def find(self, email, parents):
        if parents[email] !=  email:
            parents[email] = self.find(parents[email], parents)
        return parents[email]


## method 2
class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        owners, parents = {}, {}
        for account in accounts:
            owners[account[1]] = account[0]
            for i in xrange(1, len(account)):
                parents[account[i]] = account[i]
        
        for account in accounts:
            p = self.find(account[1], parents)
            for i in xrange(1, len(account)):
                parents[self.find(account[i], parents)] = p
        
        unions = {}
        for account in accounts:
            for i in xrange(1, len(account)):
                p = self.find(account[i], parents)
                unions.setdefault(p, set())
                unions[p].add(account[i])
        
        result = []
        for k, v in unions.items():
            result.append([owners[k]] + sorted(v))
        return result
        
    def find(self, email, parents):
        if parents[email] !=  email:
            parents[email] = self.find(parents[email], parents)
        return parents[email]