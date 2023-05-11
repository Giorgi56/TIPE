import csv
import matplotlib.pyplot as plt
filename = r"C:\Users\giorgi.kupradze\Desktop\Effacez_moi\sin10k.csv"
with open(filename, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    x, y = [], []
    counter = 0
    for line in reader:
        if counter >= 2:
            print(line)

            x_val, y_val = line[0], line[1]
            x_val = x_val[1:].replace("E", "e", 1)
            xv = float(x_val)

            y_val, y_val = line[0], line[1]
            y_val = y_val[1:].replace("E", "e", 1)
            yv = float(y_val)

            x.append(xv)
            y.append(yv)
            counter += 1
        else:
            counter += 1
            continue

plt.clf()
# plt.scatter(x[::5], y[::5])
plt.scatter(x[::5], y[::5])
plt.show()

# text = '+194.5000E-06'
# text = text[1:]
# text = text.replace("E", "e", 1)
# num = float(text)
# print(num)
