# PROJECT: Gesture FX Panel with Streamlit
import streamlit as st
import cv2
import mediapipe as mp

# Streamlit Page Setup
st.set_page_config(layout="centered", page_title="Hand Gesture Filter")

st.title("🖐️ Gesture Controlled Streamlit FX")

run = st.checkbox('🎥 Start Webcam')
frame_window = st.image([])

# MediaPipe Hand States
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, max_num_hands=1)
mp_draw = mp.solutions.drawing_utils

# Secondary camera
cap = cv2.VideoCapture(1)

# Gesture flags
gesture_flags = {
    "thumbs_up": False,
    "peace": False,
    "fist": False,
    "palm": False
}

# Theme function
def set_theme(mode="light"):
    if mode == "dark":
        st.markdown("""
            <style>
                body { background-color: #111; color: white; }
                .stApp { background-color: #111; color: white; }
            </style>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
            <style>
                body { background-color: white; color: black; }
                .stApp { background-color: white; color: black; }
            </style>
        """, unsafe_allow_html=True)

# Default theme
set_theme("light")

while run:
    success, frame = cap.read()
    if not success:
        st.warning("Camera not found.")
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)

    gesture = None
#Setting up Gestures
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            lm = hand_landmarks.landmark

            # Tip landmarks
            thumb = lm[mp_hands.HandLandmark.THUMB_TIP]
            index = lm[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            middle = lm[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
            ring = lm[mp_hands.HandLandmark.RING_FINGER_TIP]
            pinky = lm[mp_hands.HandLandmark.PINKY_TIP]

            # MCP joints for "fist" check
            index_mcp = lm[mp_hands.HandLandmark.INDEX_FINGER_MCP]
            middle_mcp = lm[mp_hands.HandLandmark.MIDDLE_FINGER_MCP]
            ring_mcp = lm[mp_hands.HandLandmark.RING_FINGER_MCP]
            pinky_mcp = lm[mp_hands.HandLandmark.PINKY_MCP]

            # Detect 👍🏼 (thumbs up)
            if thumb.y < index.y and thumb.y < middle.y:
                gesture = "thumbs_up"

            # Detect ✌🏼 (peace)
            elif (index.y < ring.y and middle.y < ring.y and thumb.y > index.y):
                gesture = "peace"

            # Detect ✊🏼 (fist)
            elif (index.y > index_mcp.y and
                  middle.y > middle_mcp.y and
                  ring.y > ring_mcp.y and
                  pinky.y > pinky_mcp.y):
                gesture = "fist"

            # Detect 🖐🏼 (open palm)
            elif (index.y < index_mcp.y and
                  middle.y < middle_mcp.y and
                  ring.y < ring_mcp.y and
                  pinky.y < pinky_mcp.y):
                gesture = "palm"

    # Gesture Effects (One-time trigger)
    if gesture == "thumbs_up" and not gesture_flags["thumbs_up"]:
        st.balloons()
        gesture_flags = {k: False for k in gesture_flags}
        gesture_flags["thumbs_up"] = True

    elif gesture == "peace" and not gesture_flags["peace"]:
        st.snow()
        gesture_flags = {k: False for k in gesture_flags}
        gesture_flags["peace"] = True

    elif gesture == "fist" and not gesture_flags["fist"]:
        set_theme("dark")
        gesture_flags = {k: False for k in gesture_flags}
        gesture_flags["fist"] = True

    elif gesture == "palm" and not gesture_flags["palm"]:
        set_theme("light")
        gesture_flags = {k: False for k in gesture_flags}
        gesture_flags["palm"] = True

    elif gesture is None:
        gesture_flags = {k: False for k in gesture_flags}

    frame_window.image(frame, channels="BGR")
    cv2.waitKey(10)

cap.release()
