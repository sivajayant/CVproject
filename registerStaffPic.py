import face_recognition
import os
#part2
# Load a sample picture and learn how to recognize it.

bvraju_image = face_recognition.load_image_file("ComputerVisionImages/bvraju1.jpg")
bvraju_face_encoding = face_recognition.face_encodings(bvraju_image)[0]

# Load a second sample picture and learn how to recognize it.
rajsekhar_image = face_recognition.load_image_file("ComputerVisionImages/rajsekhar1.jpg")
rajsekhar_face_encoding = face_recognition.face_encodings(rajsekhar_image)[0]

# lly third
manoj_image = face_recognition.load_image_file("ComputerVisionImages/manoj1.jpg")
manoj_face_encoding = face_recognition.face_encodings(manoj_image)[0]

# lly fourth
balu_image = face_recognition.load_image_file("ComputerVisionImages/balu1.jpg")
balu_face_encoding = face_recognition.face_encodings(balu_image)[0]

# lly fifth
satyasir_image = face_recognition.load_image_file("ComputerVisionImages/satyasir1.jpg")
satyasir_face_encoding = face_recognition.face_encodings(satyasir_image)[0]

# lly sixth
vasu_image = face_recognition.load_image_file("ComputerVisionImages/vasu1.jpg")
vasu_face_encoding = face_recognition.face_encodings(vasu_image)[0]

# lly seventh
santhosh_image = face_recognition.load_image_file("ComputerVisionImages/santhosh1.jpg")
santhosh_face_encoding = face_recognition.face_encodings(santhosh_image)[0]

# lly eight
satyanarayana_image = face_recognition.load_image_file("ComputerVisionImages/satyanarayana1.jpg")
satyanarayana_face_encoding = face_recognition.face_encodings(satyanarayana_image)[0]

# lly ninth
ranjitha_image = face_recognition.load_image_file("ComputerVisionImages/ranjitha1.jpg")
ranjitha_face_encoding = face_recognition.face_encodings(ranjitha_image)[0]

# lly tenth
santhoshi_image = face_recognition.load_image_file("ComputerVisionImages/santhoshi1.jpg")
santhoshi_face_encoding = face_recognition.face_encodings(santhoshi_image)[0]

# lly eleventh
prabhakar_image = face_recognition.load_image_file("ComputerVisionImages/prabhakar1.jpg")
prabhakar_face_encoding = face_recognition.face_encodings(prabhakar_image)[0]

# lly twelveth
gangadhar_image = face_recognition.load_image_file("ComputerVisionImages/gangadhar1.jpg")
gangadhar_face_encoding = face_recognition.face_encodings(gangadhar_image)[0]

# lly thirteenth
sravani_image = face_recognition.load_image_file("ComputerVisionImages/sravani1.jpg")
sravani_face_encoding = face_recognition.face_encodings(sravani_image)[0]

# lly fourteenth
sandhya_image = face_recognition.load_image_file("ComputerVisionImages/sandhya1.jpg")
sandhya_face_encoding = face_recognition.face_encodings(sandhya_image)[0]

# lly fifteenth
kalyan_image = face_recognition.load_image_file("ComputerVisionImages/kalyan1.jpg")
kalyan_face_encoding = face_recognition.face_encodings(kalyan_image)[0]


# lly sixteenth
shyam_image = face_recognition.load_image_file("ComputerVisionImages/shyam1.jpg")
shyam_face_encoding = face_recognition.face_encodings(shyam_image)[0]

#jayant_image = face_recognition.load_image_file("ComputerVisionImages/jayant1.jpg")
#jayant_face_encoding = face_recognition.face_encodings(jayant_image)[0]


#part3A
# Create arrays of known face encodings and their names
known_face_encodings = [bvraju_face_encoding,rajsekhar_face_encoding, manoj_face_encoding, 
                        balu_face_encoding, satyasir_face_encoding, vasu_face_encoding,
                        santhosh_face_encoding, satyanarayana_face_encoding,
                        ranjitha_face_encoding, santhoshi_face_encoding,
                        prabhakar_face_encoding, gangadhar_face_encoding,
                        sravani_face_encoding, sandhya_face_encoding, kalyan_face_encoding,
                        shyam_face_encoding, #jayant_face_encoding
                        ]
known_face_names = ["BVRaju","RajSekhar", "Manoj", "Balu", "SatyaSir", "Vasu",
                    "Santhosh", "Satyanarayana", "Ranjitha", "Santhoshi", "Prabhakar",
                    "Gangadhar", "Sravani", "Sandhya", "Kalyan", "Shyam",
                    ]

#part3B
def getKnownFaceEncodings():
    return known_face_encodings

def getKnownFaceNames():
    return known_face_names

