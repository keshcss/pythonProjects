print("Interest Calculator")

a = float(input("Enter Investment Amount: "))
b = float(input("Enter Interest Rate in (%): "))
c = int(input("Enter Years to Invest :"))
cint = float(b/100)
multcint = float(1 + cint)

for i in range(c):
    endamt = float(a*multcint)
    print(endamt)
    a = endamt

