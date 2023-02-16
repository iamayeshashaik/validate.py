class Check:

    def tri(self):
        side1 = int(input("Enter value of side1 :"))
        side2 = int(input("Enter value of side2 :"))
        side3 = int(input("Enter value of side3 :"))
        if side1 + side2 > side3 and side2 + side3 > side1 and side1 + side3 > side2:
            print("\n!Valid Triangle!\n")
        else:
            print("\n!Invalid Triangle!\n")

    def rec(self):
        a = int(input("Enter value of length :"))
        b = int(input("Enter value of breadth :"))
        c = int(input("Enter value of length :"))
        d = int(input("Enter value of breadth :"))
        if (a == c and b == d):
            print("\n!Valid Rectangle!\n")
        else:
            print("\n!Invalid Rectangle!\n")

obj = Check()
obj.tri()
obj.rec()