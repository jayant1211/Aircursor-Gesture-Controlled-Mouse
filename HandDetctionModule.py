'''
*********APPROACH*********
#Step1
Detect hand--->yes--->step2
-------------->no---->continue
    detectHand()

#Step2
Case I: Single tip
    Implement Mouse Pointer Movement--->movement()

Case II: Joint
    detectCase():
        SubCase 1: Twice tap in Short Duration
            Implement Left Click----------->leftClick()
        SubCase 2: Hold for more than 2 Sec
            Implement Right Click---------->rightClick()
        SubCase 3: Hold and move
            Implement Drag if applicable--->drag()

Case III: Anything else
    Continue to next Frame
'''
import mediapipe as mp
import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands


def detectHand(img):
    i = 0
    locs = []
    with mp_hands.Hands(static_image_mode=True, max_num_hands=1, min_detection_confidence=0.5) as hands:
        img = cv2.flip(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), 1)
        result = hands.process(img)
        height, width = img.shape[:2]
        if not result.multi_hand_landmarks:
            return cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

        else:
            locs = []
            for hand_landmarks in result.multi_hand_landmarks:
                mp_drawing.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS,mp_drawing_styles.get_default_hand_landmarks_style(),mp_drawing_styles.get_default_hand_connections_style())
                for point in mp_hands.HandLandmark:
                    normalizedLandmark = hand_landmarks.landmark[point]
                    pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x,
                                                                                              normalizedLandmark.y,
                                                                                              width, height)


                    #print(point, i)
                    #print(pixelCoordinatesLandmark)
                    locs.append((pixelCoordinatesLandmark))
                    #i=i+1
                    #print(normalizedLandmark)
                '''for i in range (0,24):
                    locs.append((hand_landmarks.landmark[i].x * width,
                                 hand_landmarks.landmark[i].y * height,
                                 hand_landmarks.landmark[i].z))'''
        print(len(locs))
        return cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
def detectCase(locs):
    print(locs)
