# Gesture Controlled Mouse

The Objective of project is to Control Mouse remotely using Hand Gestures.

## Pre-requisites

For hand detection, we are going to use Mediapipe Solutions . 

Install it in your base environment using cmd as particular package wont appear Project interpreter package search.

### Step 1.

In cmd, Install Mediapipe and start python interpreter

>pip install mediapipe

>python

### Step 2.

In Python interpreter, import the package and make sure you are not getting any error

>import mediapipe as mp

### Optional

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
