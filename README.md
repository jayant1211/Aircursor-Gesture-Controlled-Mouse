# Gesture Controlled Mouse

The Objective of project is to Control Mouse remotely using Hand Gestures.

## Pre-requisites

For hand detection, we are going to use [Mediapipe Solutions](https://google.github.io/mediapipe/). 
And for controlling Mouse, [Autopy](https://pypi.org/project/autopy/)

Install both in base environment using cmd as particular packages wont appear in Project interpreter package search result.

### Mediapipe
#### Step 1.

In cmd, Install Mediapipe and verify the installation

>pip install mediapipe

#### Step 2.

verify installation by importing package

>python

>import mediapipe as mp

### Autopy

#### Step 1.

In cmd, install autopy and verify the installation

>pip install wheel

>pip install setuptools-rust

>pip install autopy

#### Step 2.

>python

>import autopy

>autopy.mouse.move(1, 1)

### *Optional*

*If you are using virtual environment, activate it and install the package there.*

*For instance,*

>*path_to_venv\scripts\activate.bat*

*repeat step 1 and 2*

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
