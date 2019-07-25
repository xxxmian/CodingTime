class node:
    def __init__(self, val):
        self.val = val
        self.staff = 1
        self.level = 1
        self.boss = self

class QuickUnion:
    def findwWthCompress(self, a):
        while a.boss != a:
            a = a.boss
        bigboss = a
        while a.boss != a:
            next = a.boss
            a.boss = bigboss
            a = next


    def unionWithWeight(self, a, b):
        boss_a = self.find(a)
        boss_b = self.find(b)
        if boss_a != boss_b:
            if boss_a.staff < boss_b.staff:
                boss_a.boss = boss_b
                boss_b.staff += boss_a.staff
            else:
                boss_b.boss = boss_a
                boss_a.staff += boss_b
    def unionByLevel(self, a, b):
        boss_a = self.find(a)
        boss_b = self.find(b)
        if boss_a != boss_b:
            if boss_a.level <= boss_b.level:
                boss_a.boss = boss_b
                if boss_a.level == boss_b.level:
                    boss_b.level += 1
            else:
                boss_b.boss = boss_a

    def find(self, a):
        while a.boss != a:
            a = a.boss
        return a

    def union(self, a, b):
        boss_a = self.find(a)
        boss_b = self.find(b)
        if boss_a != boss_b:
            boss_b.boss = boss_a
            boss_a.staff += boss_b.staff




