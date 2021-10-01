import control.matlab as matlab
import math
import matplotlib.pyplot as pyplot


def viborZvena(): #подбор звена
    bezinterName = 'Безинерционное звено'
    aperiodName = 'Апериодическое звено'
    integrName = 'Интегрирующее звено'
    igealdifzveno = 'Идеальное дифференцирующее звено'
    realdifzveno = 'Реальное дифференцирующее звено'
    needNewChoice = True

    while needNewChoice:
        userInput = input('Введите номер команды: \n'
                          '1 - ' + bezinterName + ': \n'
                          '2 - ' + aperiodName + ': \n'
                          '3 - ' + integrName + ': \n'
                          '4 - ' + igealdifzveno + ': \n'
                          '5 - ' + realdifzveno + ': \n')

        if userInput.isdigit():
            needNewChoice=False
            userInput=int(userInput)
            if userInput == 1:
                name='Безинерционное звено'
            elif userInput == 2:
                name='Апериодическое звено'
            elif userInput == 3:
                name='Интегрирующее звено'
            elif userInput == 4:
                name='Идеальное дифференцирующее звено'
            elif userInput == 5:
                name='Реальное дифференцирующее звено'
            else: print('Данное звено находится в разработке')
        else:
            print('Введите значение из представленных выше')
            needNewChoice = True
    return name

def getUnit(name):
    needNewChoice = True

    while needNewChoice:
        needNewChoice = False
        k = input('Введите коэффициент "k": ')
        t = input('Введите коэффициент "t": ')

        if k.isdigit() and t.isdigit():
            k=int(k)
            t=int(t)
            if name == 'Безинерционное звено':
                unit = matlab.tf([k],[1])
            elif name == 'Апериодическое звено':
                unit = matlab.tf([k], [t, 1])
            elif name == 'Интегрирующее звено':
                unit = matlab.tf([1], [t, 0.00000000000000000000000000001])
            elif name == 'Идеальное дифференцирующее звено':
                unit = matlab.tf([t, 0], [0.00000000000000000000000000001,1])
            elif name == 'Реальное дифференцирующее звено':
                unit = matlab.tf([k, 0.00000000000000000000000000001], [t, 1])
    return unit

def graph(num, title, y, x):
    pyplot.subplot(2,2,num)
    pyplot.grid(True)
    pyplot.ylabel('Амплитуда')
    pyplot.xlabel('                   Время')
    if title == 'Переходная характеристика':
        pyplot.plot(x,y,'purple')
    elif title == 'Импульсная характеристика':
        pyplot.plot(x,y, 'green')
    elif title == 'АЧХ':
        pyplot.plot(x, y, 'black')
        pyplot.xlabel('                   Частота')
    elif title == 'ФЧХ':
        pyplot.plot(x, y*180/math.pi, 'red')
        pyplot.ylabel('Фаза')
        pyplot.xlabel('                   Частота')
    pyplot.title(title)

m = viborZvena()
print(m)
unit = getUnit(m)
print('УНТИЛ - ',unit)

timeLine = []
for i in range(2, 3500):
    timeLine.append(i/100)
timeLine2 = []
for i in range(2, 3500):
    f=i/(2*3.14)
    timeLine2.append(f)

mag,phase,omega = matlab.freqresp(unit,timeLine)


[y,x] = matlab.step(unit,timeLine)
graph(1, 'Переходная характеристика', y,x)
#pyplot.show()
[y,x] = matlab.impulse(unit,timeLine)
graph(2, 'Импульсная характеристика', y,x)
#pyplot.show()
[y,x] = [mag,timeLine2]
graph(3, 'АЧХ', y,x)
#pyplot.show()
[y,x] = [phase,timeLine2]
graph(4, 'ФЧХ', y,x)
pyplot.show()