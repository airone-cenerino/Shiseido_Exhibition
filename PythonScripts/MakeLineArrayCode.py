num = int(input())


file = open("LineArrayCode.txt", "w")

for i in range(num):
    file.write("int* line0_"+str(i)+"[] = {X0_"+str(i)+", Y0_"+str(i)+"};\n")

file.write("int** picture0[] = {")
for i in range(num-1):
    file.write("line0_"+str(i)+", ")
file.write("line0_" + str(num - 1) + "};")
file.close()