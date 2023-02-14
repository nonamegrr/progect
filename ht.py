import matplotlib.pyplot as temper
import matplotlib.pyplot as air
import matplotlib.pyplot as ground
import time
y1g, y2g, y3g, y4g, y5g, y6g, yMg, yMa, yMt, x, y1t, y2t, y3t, y4t, y1a, y2a, y3a, y4a = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
hum_air, temp, hum_gr = [], [], []
a, b = 0, 0
create_table_query = {"brand": 2,    "model": 1,
    "price": 2,    "released": 3,    "brand1": 4,    "model1": 5,
    "price1": 6,    "released1": 1,
    "brand2": 2,    "model2": 3,    "price2": 4,    "released2": 1,
    "released3": 2,    "brand3": 3,    "model3": 4}
while a < 5:
    b += 1
    a += 1
    time.sleep(1)
    if b > 5:
        hum_gr.pop(4)
        hum_air.pop(4)
        temp.pop(4)
        y1t.pop(4)
        y1g.pop(4)
        y1a.pop(4)
        yMg.pop(4)
        yMa.pop(4)
        yMt.pop(4)
        y2g.pop(4)
        y2t.pop(4)
        y2a.pop(4)
        y3g.pop(4)
        y3a.pop(4)
        y3t.pop(4)
        y4g.pop(4)
        y4a.pop(4)
        y4t.pop(4)
        y5g.pop(4)
        y6g.pop(4)
    val = list(create_table_query.values())
    val0 = input(val[0]).split
    del val0[0]
    val[0] = val0
    hum_air.append([val[0], val[7], val[8], val[9], val[10]])
    temp.append([val[0], val[11], val[12], val[13], val[14]])
    hum_gr.append([val[0], val[1], val[2], val[3], val[4], val[5], val[6]])
    y1g.append(val[1])
    y2g.append(val[2])
    y3g.append(val[3])
    y4g.append(val[4])
    y5g.append(val[5])
    y6g.append(val[6])
    x.append(val[0])
    yMg.append((val[1] + val[2] + val[3] + val[4] + val[5] + val[6]) / 6)
    y1t.append(val[11])
    y2t.append(val[12])
    y3t.append(val[13])
    y4t.append(val[14])
    yMt.append((val[11] + val[12] + val[13] + val[14]) / 4)
    y1a.append(val[7])
    y2a.append(val[8])
    y3a.append(val[9])
    y4a.append(val[10])
    yMa.append((val[7] + val[8] + val[9] + val[14]) / 4)
# for site
ground.plot(x, y1g, label="line 1")
ground.plot(x, y2g, label="line 2")
ground.plot(x, y3g, label="line 3")
ground.plot(x, y4g, label="line 4")
ground.plot(x, y5g, label="line 5")
ground.plot(x, y6g, label="line 6")
ground.plot(x, yMg, label="middle")
ground.xlabel('x - time')
ground.ylabel('y - air')
ground.title('Ground')
ground.legend()
ground.show()
air.plot(x, y1t, label="line 1")
air.plot(x, y2t, label="line 2")
air.plot(x, y3t, label="line 3")
air.plot(x, y4t, label="line 4")
air.plot(x, yMa, label="middle")
air.xlabel('x - time')
air.ylabel('y - air')
air.title('Air')
air.legend()
air.show()
temper.plot(x, y1t, label="line 1")
temper.plot(x, y2t, label="line 2")
temper.plot(x, y3t, label="line 3")
temper.plot(x, y4t, label="line 4")
temper.plot(x, yMt, label="middle")
temper.xlabel('x - time')
temper.ylabel('y - temp')
temper.title('Temp')
temper.legend()
temper.show()
from tabulate import tabulate
header = ['Time', 'upper_left', 'upper_right', 'down_left', 'down_right']#change names
header_gr = ['Time', 'first', 'second', 'third', 'fourth', 'fifth', 'sixth']#change names
print("Ground", tabulate(hum_gr, headers=header_gr, tablefmt="fancy_grid", showindex="always"), sep='\n')
print("Air", tabulate(hum_air, headers=header, tablefmt="fancy_grid", showindex="always"), sep="\n")
print("Temperature", tabulate(temp, headers=header, tablefmt="fancy_grid", showindex="always"), sep='\n')
