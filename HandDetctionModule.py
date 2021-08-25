'''
*********APPROACH*********
#Step1
Detect hand--->yes--->step2
-------------->no---->continue

#Step2
Case I: Single tip
    Implement Mouse Pointer Movement--->movement()

Case II: Joint
    SubCase 1: Twice tap in Short Duration
        Implement Left Click----------->leftClick()
    SubCase 2: Hold for more than 2 Sec
        Implement Right Click---------->rightClick()
    SubCase 3: Hold and move
        Implement Drag if applicable--->drag()

Case III: Anything else
    Continue to next Frame
'''
