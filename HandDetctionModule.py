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



# For static images:
def detectHand(img):
    with mp_hands.Hands(static_image_mode=True, max_num_hands=1, min_detection_confidence=0.5) as hands:
        img = cv2.flip(cv2.cvtColor(img,cv2.COLOR_BGR2RGB),1)
        result = hands.process(img)
        height, width = img.shape[:2]
        if not result.multi_hand_landmarks:
            return cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

        else:
            for hand_landmarks in result.multi_hand_landmarks:
                mp_drawing.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS,
                                      mp_drawing_styles.get_default_hand_landmarks_style(),
                                      mp_drawing_styles.get_default_hand_connections_style())

        return cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        '''for multiple images together
    with mp_hands.Hands(static_image_mode=True, max_num_hands=1, min_detection_confidence=0.5) as hands:
        for idx, file in enumerate(IMAGE_FILES):
            # Read an image, flip it around y-axis for correct handedness output (see
            # above).
            image = cv2.flip(cv2.imread(file), 1)
            # Convert the BGR image to RGB before processing.
            results = hands.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
            mp_drawing.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS,
                                      mp_drawing_styles.get_default_hand_landmarks_style(),mp_drawing_styles.get_default_hand_connections_style())
            
            # Print handedness and draw hand landmarks on the image.
            print('Handedness:', results.multi_handedness)
            if not results.multi_hand_landmarks:
                continue
            image_height, image_width, _ = image.shape
            annotated_image = image.copy()
            for hand_landmarks in results.multi_hand_landmarks:
                print('hand_landmarks:', hand_landmarks)
                print(
                    f'Index finger tip coordinates: (',
                    f'{hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x * image_width}, '
                    f'{hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y * image_height})'
                )
                mp_drawing.draw_landmarks(annotated_image,hand_landmarks,mp_hands.HAND_CONNECTIONS,mp_drawing_styles.get_default_hand_landmarks_style(),mp_drawing_styles.get_default_hand_connections_style())
            cv2.imwrite('/tmp/annotated_image' + str(idx) + '.png', cv2.flip(annotated_image, 1))'''

