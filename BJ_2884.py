H,M=list(map(int,input().split()))

if (H!=0):
    if (M<45):
        H=H-1
        M=M-45+60
    elif(M>=45):
        M=M-45

if (H==0):
    if (M < 45):
        H = 23
        M = M - 45 + 60
    elif (M >= 45):
        M = M - 45

print(H,M)