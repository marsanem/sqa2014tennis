# -*- coding: utf-8 -*-
class Match:

    def __init__(self, p1, p2, sets):
        self.p1 = p1
        self.p2 = p2
        self.sets = sets
        self.contp1 = 0
        self.contp2 = 0
        self.scorep1 = ['', '', '', '', '']
        self.scorep2 = ['', '', '', '', '']

    def score(self):
        if self.contp1 == 0 and self.contp2 == 0:
            return "{0} plays with {1} | 0-0".format(self.p1, self.p2)
        elif self.contp1 > self.contp2:
            return "{0} defeated {1} | {2}".format(self.p1, \
                                                   self.p2, self.getpoints(self.p1))
        else:
            return "{0} defeated {1} | {2}".format(self.p2, \
                                                   self.p1, self.getpoints(self.p2))

    def add(self, player, set_num, num1, num2):
        if player == self.p1:
            self.contp1 += 1
            self.scorep1[set_num - 1] = num1
            self.scorep2[set_num - 1] = num2
        else:
            self.contp2 += 1
            self.scorep1[set_num - 1] = num2
            self.scorep2[set_num - 1] = num1

    def getpoints(self, player):
        points = ""
        i = 0
        total = self.contp1 + self.contp2
        for i in range(total):
            if player == self.p1:
                points += str(self.scorep1[i]) + "-" + str(self.scorep2[i]) + ", "
            else:
                points += str(self.scorep2[i]) + "-" + str(self.scorep1[i]) + ", "
        return points[:-2]
