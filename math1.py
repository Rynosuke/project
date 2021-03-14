import math as m
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as mlines

a = -2
b = -4
c = 3
d = 6
al = 75


def func(l = []):
    return ((((l[0] - a) * m.cos(al) + (l[1] - b) * m.sin(al)) ** 2) / c ** 2) + (
                 (((l[1] - b) * m.cos(al) - (l[0] - a) * m.sin(al)) ** 2) / d ** 2)

x1, x2 = np.mgrid[-3*np.pi:3*np.pi:100j,
                -3*np.pi:3*np.pi:100j]
z = ((((x1 - a) * m.cos(al) + (x2 - b) * m.sin(al)) ** 2) / c ** 2) + ( (((x2 - b) * m.cos(al) - (x1 - a) * m.sin(al)) ** 2) / d ** 2)


#fig, ax = plt.subplots(1,2)

fig, ax = plt.subplots()

#  Задаем значение каждого уровня:
lev = [0, 1, 2, 3, 4, 6, 10, 20, 40, 100, 900, 10000]

#  Создаем массив RGB цветов каждой области:
color_region = np.zeros((12, 3))
color_region[:, 1:] = 0.2
color_region[:, 0] = np.linspace(0, 1, 12)

ax.contourf(x1, x2, z,
            levels = lev,
            colors = color_region)

fig.set_figwidth(8)    #  ширина и
fig.set_figheight(8)    #  высота "Figure"

def set_point(l=[]):
    x1 = l[0]
    x2 = l[1]
    X = []
    X.append(x1)
    Y = []
    Y.append(x2)
    plt.scatter(X, Y, color='w', marker='o', s=1)  # зеленая звездочка


h = 1.02
x1 = np.array([1,1])
x2 = x1 + h*np.array([1,0])
x3 = x2 + h*np.array([0,1])
print('x1 =',x1,'x2 =', x2,'x3 =', x3)
x_hor = 0
x_ver = 0
eps = 0.001
run = True
count = 0
a_s = 1
g_s = 2
y_s = 0.5
b_s = 1.2
f1 = func(x1)
f2 = func(x2)
f3 = func(x3)
print(func(x1))

while run:

     l = [f1,f2,f3]
     # print('list=', l)

     fh = max(l)
     if fh == f1:
         xh = x1
     elif fh == f2:
         xh = x2
     elif fh == f3:
         xh = x3
     l.remove(fh)
     # print('list=', l)

     fl = min(l)
     if fl == f1:
         xl = x1
     elif fl == f2:
         xl = x2
     elif fl == f3:
         xl = x3
     l.remove(fl)
     # print('list=', l)
     fg = l.pop(0)
     if fg == f1:
         xg = x1
     elif fg == f2:
         xg = x2
     elif fg == f3:
         xg = x3

     # print('xmax=', xh, 'xmid=', xg, 'xmin=', xl)
     # print('f1=',f1,'f2=',f2,'f3=',f3)
     # print('list=', l)
     # print('fh=', fh, 'fl=', f2, 'fg=', f3)
     xc = (1/2)*(xg+xl)
     fc = func(xc)
     # print('xc=',xc)

     x0 = ((1+a_s)*xc) - (a_s*xh)

     f0 = func(x0)
     print('f0=', f0)
     print('fg=', fg)

     if f0 < fl:
         xr = (1-b_s)*xc - b_s*x0
         fr = func(xr)
         if fr < fl:
             xh = xr
             x1 = xh
             # print("x1=", x1)
             # print("x2=", x2)
             # print("x3=", x3)

         if fr >= fl:
             xh = x0
             x1 = xh
             # print("x1=", x1)
             # print("x2=", x2)
             # print("x3=", x3)

     if fl < f0 < fg:
         xh = x0
         x1 = xh


     if f0 > fl:
         h = h/2
         if f0 < fh:
             xs = y_s * x0 + (1 - y_s) * xc
             x1 = xs
         if f0 >= fh:
             xs = y_s * xh + (1 - y_s) * xc
             x1 = xs
         fs = func(xs)
         print("xs=", xs)
         if fs < fh:
             xh = xs
             x1 = xh
         if fs >= fh:
             x1 = x1 + 0.5 * (x1 - x1)
             x2 = x2 + 0.5 * (x2 - x1)
             x3 = x3 + 0.5 * (x3 - x1)

     x2 = x1 - h * np.array([1, 0])
     x3 = x2 - h * np.array([0, 1])
     print("x1=", x1)
     print("x2=", x2)
     print("x3=", x3)
     f1 = func(x1)
     f2 = func(x2)
     f3 = func(x3)
     # set_point(x1)
     # set_point(x2)
     # set_point(x3)
     l = mlines.Line2D([x1[0], x2[0]], [x1[1], x2[1]])
     ax.add_line(l)
     l = mlines.Line2D([x2[0], x3[0]], [x2[1], x3[1]])
     ax.add_line(l)
     l = mlines.Line2D([x3[0], x1[0]], [x3[1], x1[1]])
     ax.add_line(l)
     f = (f1+f2+f3)/(2+1)
     g2 = ((f1-f)**2/(2+1)+(f2-f)**2/(2+1)+(f3-f)**2/(2+1))
     count+=1
     print("-------count: ", count)
     if (m.sqrt(g2) <= eps):
         xc = (1 / 2) * (x1 + x2)
         print("x1_min:", xc[0],"\nx2_min:",xc[1])
         break

plt.show()