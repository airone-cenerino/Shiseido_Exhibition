import numpy as np

data = np.loadtxt("LeftMotor.csv", delimiter=",")
print(data)
print(sum(data))
data = np.loadtxt("RightMotor.csv", delimiter=",")

print(sum(data))
