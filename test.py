from Animation import Animation, Ease
import time

myAnimation = Animation(10, 0, 5, Ease.EASE_IN_OUT_QUART)

while not myAnimation.isDone():
    time.sleep(1)
    print(myAnimation.getValue())