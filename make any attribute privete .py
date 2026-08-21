class Bank:
    def __init__(self, acc_no,acc_pass):
        self.acc_no = acc_no
        self.__acc_pass= acc_pass # This is privet attribute , it can't be access from outside the class

acc1= Bank("1234567890","FCVGBHNJM")
print(acc1.acc_no)
print(acc1.acc_pass)