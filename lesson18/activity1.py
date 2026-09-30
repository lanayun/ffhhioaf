input("set a bin Or turn it ON")
print("5  ",bin(5)[2:])
print("5|2 =",5|2,"binary:",bin(5 | 2)[2:])

input("zero a bit - AND turns it OFF")
print(" 7=",bin(7)[2:])
print("7&5 =",7&5,"binary:",bin(7&5)[2:])

n = int(input("enter a number try 4 or 6"))
guess = input("is it a power of 2?(yes no)")
input("Power of2 - only one bit is on")
if n >0 and (n&(n-1)) == 0:
    print(n," binary:",bin(n)[2:],"power of2 guess:",guess)

else:
    print(n," binary:",bin(n)[2:],"not power of 2 guess:",guess)