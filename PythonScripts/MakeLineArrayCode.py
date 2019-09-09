num = int(input("画像の枚数"))
imageNumber = int(input("画像番号"))


file = open("LineArrayCode.txt", "w")

for i in range(num):
    file.write("int* line" + str(imageNumber) + "_" + str(i)+"[] = {X"+ str(imageNumber) +"_"+str(i)+", Y"+ str(imageNumber) +"_"+str(i)+"};\n")

file.write("int** picture"+ str(imageNumber) +"[] = {")
for i in range(num-1):
    file.write("line"+ str(imageNumber) +"_"+str(i)+", ")
file.write("line"+ str(imageNumber) +"_" + str(num - 1) + "};")
file.close()