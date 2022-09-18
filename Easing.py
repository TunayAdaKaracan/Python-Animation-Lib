from Easings import *

class EaseClass:
    def __init__(self, func):
        self.ease_function = func
    
    def getEaseValue(self, x):
        if x <= 0: return 0
        if x >= 1: return 1
        return self.ease_function(x)

class Ease:
    LINEAR = EaseClass(linear)
    EASE_IN_SINE = EaseClass(easeInSine)
    EASE_OUT_SINE = EaseClass(easeOutSine)
    EASE_IN_OUT_SINE = EaseClass(easeInOutSine)
    EASE_IN_CUBIC = EaseClass(easeInCubic)
    EASE_OUT_CUBIC = EaseClass(easeOutCubic)
    EASE_IN_OUT_CUBIC = EaseClass(easeInOutCubic)
    EASE_IN_QUINT = EaseClass(easeInQuint)
    EASE_OUT_QUINT = EaseClass(easeOutQuint)
    EASE_IN_OUT_QUINT = EaseClass(easeInOutQuint)
    EASE_IN_CIRC = EaseClass(easeInCirc)
    EASE_OUT_CIRC = EaseClass(easeOutCirc)
    EASE_IN_OUT_CIRC = EaseClass(easeInOutCirc)
    EASE_IN_ELASTIC = EaseClass(easeInElastic)
    EASE_OUT_ELASTIC = EaseClass(easeOutElastic)
    EASE_IN_OUT_ELASTIC = EaseClass(easeInOutElastic)
    EASE_IN_QUAD = EaseClass(easeInQuad)
    EASE_OUT_QUAD = EaseClass(easeOutQuad)
    EASE_IN_OUT_QUAD = EaseClass(easeInOutQuad)
    EASE_IN_QUART = EaseClass(easeInQuart)
    EASE_OUT_QUART = EaseClass(easeOutQuart)
    EASE_IN_OUT_QUART = EaseClass(easeInOutQuart)
    EASE_IN_EXPONENTIAL = EaseClass(easeInExponential)
    EASE_OUT_EXPONENTIAL = EaseClass(easeOutExponential)
    EASE_IN_OUT_EXPONENTIAL = EaseClass(easeInOutExponential)
    EASE_IN_BACK = EaseClass(easeInBack)
    EASE_OUT_BACK = EaseClass(easeOutBack)
    EASE_IN_OUT_BACK = EaseClass(easeInOutBack)
    EASE_IN_BOUNCE = EaseClass(easeInBounce)
    EASE_OUT_BOUNCE = EaseClass(easeOutBounce)
    EASE_IN_OUT_BOUNCE = EaseClass(easeInOutBounce)