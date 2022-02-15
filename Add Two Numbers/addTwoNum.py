
class addTwoNum:
    def __init__(self, l1, l2):
        self.l1 = l1
        self.l2 = l2
        self.l3 = []
        self.carry = 0
        self.sum = 0
        self.sum_list = []

    def addTwoNum(self):
        while self.l1 or self.l2:
            if self.l1:
                self.sum = self.l1.val + self.carry
                self.l1 = self.l1.next
            else:
                self.sum = self.l2.val + self.carry
                self.l2 = self.l2.next
            self.carry = self.sum // 10
            self.sum_list.append(self.sum % 10)
        if self.carry:
            self.sum_list.append(self.carry)
        return self.sum_list