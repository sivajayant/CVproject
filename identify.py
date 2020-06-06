import face_recognition
import cv2
import numpy as np
from accessDatabase1 import *
from registerStaffPic import *

#part1
# Get a reference to webcam #0 (the default one)
video_capture = cv2.VideoCapture(0)

#part2 (in registerStaffPic.py)

#part3C
known_face_encodings = getKnownFaceEncodings()
known_face_names = getKnownFaceNames()


#part4
# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True
username = ""

#part5
while True:
    #part5A
    # Grab a single frame of video
    ret, frame = video_capture.read()

    # Resize frame of video to 1/4 size for faster face recognition processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # Convert the image from BGR color (which OpenCV uses) to 
    #RGB color (which face_recognition uses)
    rgb_small_frame = small_frame[:, :, ::-1]
    #we shall see what it means in the explanation part
    
    #part5B
    # Only process every other frame of video to save time
    if process_this_frame:
        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
                            #meanings of parameters: in the explanation part
        face_names = []
        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            #Returns:	A list of True/False values 
            #indicating which known_face_encodings match the face encoding to check

            name = "Unknown"
            
            face_distances = face_recognition.face_distance(known_face_encodings, 
                                                            face_encoding)
                            
            best_match_index = np.argmin(face_distances)

            if matches[best_match_index]:
                name = known_face_names[best_match_index]
                username = name

            face_names.append(name)

    process_this_frame = not process_this_frame

    #part5C
    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face loc.s since the frame we detected in was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35),(right, bottom),(0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), 
                    font, 1.0, (255, 255, 255), 1) #white font on red background(BGR)
        cv2.putText(frame, name + ", added ", (left - 24, bottom + 24), 
                    font, 1.0, (255, 255, 255), 1) 
        font2 = font
        left2 = left
        bottom2 = bottom
        frame2 = frame
    #part5D
    # Display the resulting image
    cv2.imshow('Video', frame)
    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
#part6
myAddRecord(username)

#part7
# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()