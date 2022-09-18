from Easing import Ease, EaseClass
import math
import time

class InvalidEaseFunction(Exception):
    def __init__(self):
        super().__init__("Invalid Easing Function")


class Animation:
    def __init__(self, duration, start, end, easing=Ease.LINEAR):
        if isinstance(duration, float):
            duration = duration / 1000
        
        self.value = start

        self.start = start
        self.end = end

        if not isinstance(easing, EaseClass):
            raise InvalidEaseFunction()

        self.easing = easing

        self.increasing = end > start
        difference = abs(start - end)
        
        self.changePerMillisecond = difference / duration
        self.lastTime = time.time()

    def reset(self):
        self.value = self.start
        self.lastTime = time.time()

    def getValue(self):
        return self.getEased()
    
    def loadValue(self):
        if self.value == self.end: return self.value
        if self.increasing:
            if self.value >= self.end:
                self.value = self.end
                return self.value
            self.value += (self.changePerMillisecond) * (time.time() - self.lastTime)
            if self.value > self.end:
                self.value = self.end
            self.lastTime = time.time()
            return self.value
        else:
            if self.value <= self.end:
                self.value = self.end
                return self.value
            self.value -= (self.changePerMillisecond) * (time.time() - self.lastTime)
            if self.value < self.end:
                self.value = self.end
            self.lastTime = time.time()
            return self.value
    
    def isDone(self):
        return self.value == self.end
    
    def getEased(self):
        if self.easing == Ease.LINEAR: return self.loadValue()
        return self.map(self.easing.getEaseValue(self.map(self.loadValue(), self.start, self.end, 0, 1)), 0, 1, self.start, self.end)

    def map(self, value, minInp, maxInp, minMapped, maxMapped):
        return (value - minInp) / (maxInp - minInp) * (maxMapped - minMapped) + minMapped