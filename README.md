
## Examples

Importing

```py
  from Animation import Animation, Easing
```

How to create an animation class
```py
duration = 10 # if you want in milliseconds use float instead. I.E: 500.0 for 500 ms
start = 0
end = 100

myAnimation = Animation(duration, start, end)
```

Use with easings

```py
myAnimation = Animation(duration, start, end, Easing.EASE_IN_OUT_QUAD) 
```

https://easings.net to learn more about easings.

Getting a value from animation

```py
result = myAnimation.getValue()
```

Check And Reset Animation

```py
if myAnimation.isDone():
    myAnimation.reset()
```

# This project might contain bugs. Dont be afraid to make pull requests!
This project is implemantation of [Sim's Animation](https://github.com/SIMULATAN/MCPSnippets/tree/main/animations).
