import math

def linear(x):
    return x

def easeInSine(x):
    return float(1 - math.cos(( x* math.pi) / 2))

def easeOutSine(x):
    return float(math.sin((x * math.pi) / 2))

def easeInOutSine(x):
    return float(-(math.cos(math.pi * x)-1) / 2)

def easeInCubic(x):
    return float(x * x * x)

def easeOutCubic(x):
    return float(1 - math.pow(1- x, 3))

def easeInOutCubic(x):
    return float((4 * x * x * x * x if x < 0.5 else 1) - math.pow(-2 * x + 2, 3) / 2)

def easeInQuint(x):
    return float(x * x * x * x * x)

def easeOutQuint(x):
    return float(1 -  math.pow(1 - x, 5))

def easeInOutQuint(x):
    return float((16 * x * x * x * x if x < 0.5 else 1) - math.pow(-2 * x +2, 5) / 2)

def easeInCirc(x):
    return float(1 - math.sqrt(1 - math.pow(x, 2)))

def easeOutCirc(x):
    return float(math.sqrt(1 - math.pow(x - 1, 2)))

def easeInOutCirc(x):
    return float (((1 - math.sqrt(1 - math.pow(2 * x, 2))) / 2) if x < 0.5 else (math.sqrt(1 - math.pow(-2 * x + 2, 2)) + 1) / 2)

def easeInElastic(x):
    if x <= 0: return 0
    if x >= 1: return 1
    return float(-math.pow(2, 10 * x - 10) * math.sin((x * 10 - 10.75) * ((2 * math.pi) / 3)))

def easeOutElastic(x):
    if x <= 0: return 0
    if x >= 1: return 1
    return float(math.pow(2, -10 * x) * math.sin((x * 10 - 0.75) * ((2 * math.pi) / 3)) + 1)

def easeInOutElastic(x):
    if x <= 0: return 0
    if x >= 1: return 1
    return float( -(math.pow(2, 20 * x - 10) * math.sin((20 * x - 11.125) * ((2 * math.pi) / 4.5))) / 2 if x < 0.5 else (math.pow(2, -20 * x + 10) * math.sin((20 * x - 11.125) * ((2 * math.pi) / 4.5))) / 2 + 1)

def easeInQuad(x):
    return float(x * x)

def easeOutQuad(x):
    return float(1 - (1 - x) * (1 - x))

def easeInOutQuad(x):
    return float(2 * x* x if x < 0.5 else 1 - math.pow(-2 * x + 2, 2) / 2)

def easeInQuart(x):
    return float(x * x * x * x)

def easeOutQuart(x):
    return float(1 - math.pow(1-x, 4))

def easeInOutQuart(x):
    return float(8 * x * x * x * x if x < 0.5 else 1 - math.pow(-2 * x + 2, 4) / 2)

def easeInExponential(x):
    return float(0 if x == 0 else math.pow(2, 10 * x - 10))

def easeOutExponential(x):
    return float(1 if x == 1 else 1 - math.pow(2, -10 * x))

def easeInOutExponential(x):
    return float(0 if x == 0 else 1 if x == 1 else math.pow(2, 20 * x - 10) / 2 if x < 0.5 else (2 -  math.pow(2, -20 * x + 10)) / 2)

def easeInBack(x):
    c1 = 1.70158
    return float((c1 + 1) * x * x * x - c1 * x * x)

def easeOutBack(x):
    c1 = 1.70158
    return float(1 + (c1 + 1) * pow(x - 1, 3) + c1 * pow(x - 1 , 2))

def easeInOutBack(x):
    c1 = 1.70158
    c2 = c1 * 1.525

    return float((math.pow(2 * x, 2) * ((c2 + 1) * 2 * x - c2)) / 2 if x < 0.5 else (math.pow(2 * x - 2, 2) * ((c2 + 1) * (x * 2 - 2) + c2) + 2) / 2)

def easeInBounce(x):
    return 1 - easeOutBounce(1 - x)

def easeOutBounce(x):
    n1 = 7.5625
    d1 = 2.75
    if x < 1 / d1:
        return n1 * x * x
    elif x < 2 / d1:
        x -= 1.5
        return float(n1 * (x / d1) * x + 0.75)
    elif x < 2.5 / d1:
        x -= 2.25
        return float(n1 * (x / d1) * x + 0.9375)
    else:
        x -= 2.625
        return float(n1 * (x / d1) * x + 0.984375)

def easeInOutBounce(x):
    return (1 - easeOutBounce(1 - 2 * x)) / 2 if x < 0.5 else (1 + easeOutBounce(2 * x - 1)) / 2
