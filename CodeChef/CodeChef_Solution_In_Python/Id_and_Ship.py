#Id_and_Ship
t=int(input())
for i in range(t):
    s=input()
    if(s=='B' or s=='b'):
        print("BattleShip")
    elif(s=='C' or s=='c'):
        print("Cruiser")
    elif(s=='D' or s=='d'):
        print("Destroyer")
    else:
        print("Frigate")    