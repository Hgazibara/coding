X = int(input())
Y = int(input())
Z = int(input())
N = int(input())

print([[x,y,z] for x in range(0, X+1) for y in range(0, Y+1) for z in range(0, Z+1) if x+y+z != N])