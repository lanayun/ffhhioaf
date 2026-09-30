input("built a bit mask - one 1 at exactly tha pos"
      )
for k in range(4):
    mask = 1<< k
    print("bit",k,"mask:",mask,"binary:",bin(mask)[2:])

n = int(input("enter a number try42 or 13"))
guess = input("is bit 2 of"+str(n)+"ON?(yes/no)")
input("check if the Nth bit is set - and with mask.")
result = (n>>2)&1
if result:
    print(n,"binary:",bin(n)[2:],"bit 2 is ON your guess:",guess)
else:
    print(n,"binary:",bin(n)[2:],"bit 2 is OFF your guess:",guess)