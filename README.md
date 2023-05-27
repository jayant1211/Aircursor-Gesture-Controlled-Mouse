# Aircursor : Gesture Controlled Mouse

The Objective of project is to Control Mouse remotely using Hand Gestures.

## Getting Started

For hand detection, i used [Mediapipe Solutions](https://google.github.io/mediapipe/). 
And for controlling Mouse, [Autopy](https://pypi.org/project/autopy/)

Install both in your base environment using cmd as particular packages wont appear in Pycharm's project interpreter->package search results.

### Mediapipe

In cmd, Install Mediapipe and verify the installation

```bash
pip install mediapipe
```

verify installation by importing package
```bash
python
import mediapipe as mp
```

### Autopy

Install autopy and verify the installation
```bash
pip install wheel
pip install setuptools-rust
pip install autopy
```

verify:
```bash
python
import autopy
autopy.mouse.move(1, 1)
```

## Different Gesture Modes

### 1.Mouse Movement

Cursor movement mode can be triggered using one finger or more than one fingers, given they maintain a distance between them.

![Alt text](https://github.com/jayant1211/GestureControlledMouse/blob/master/results/movement.gif)

### 2.Left Click

Left click can be implemented by touching middle and index finger.

![Alt text](https://github.com/jayant1211/GestureControlledMouse/blob/master/results/left.gif)

### 3.Right Click

Right click can be implemented by touching thumb and middle finger.

![Alt text](https://github.com/jayant1211/GestureControlledMouse/blob/master/results/right.gif)

### 4.Hold and Drag

Can be triggered using Three fingers, Index, Middle and Ring.  

![Alt text](https://github.com/jayant1211/GestureControlledMouse/blob/master/results/drag.gif)
