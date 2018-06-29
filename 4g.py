import matplotlib.pyplot as plt

H = [] #키
W = [] #몸무게
with open("data/test.csv") as f:
   for line in f:
      [i, height, weight] = line.strip().split(",")
      height = 2.54 * float(height)
      weight = 0.343592 * float (weight)
#      print(line)
      print("%.2f" % height, "%.2f" % weight)
      H.append(height)
      W.append(weight)

#plt.plot(H,W)
plt.plot(H,W,linestyle="None",marker="o",markersize=10,color="blue")
plt.show()
