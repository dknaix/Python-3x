"""
This code is to show use of OpenCV library
The example camera code captures images and stores in current directory
For any querries contact: dknaix.github@gmail.com
"""

try:
    import cv2
except ImportError:
    print("Error in Importing cv2 library!!! plz install dependencies via 'pip'")
    input("Press enter to exit")
    exit()

cam = cv2.VideoCapture(0)

img_counter = 0
print("Press 'spacebar' to capture Images")
while True:
    ret, frame = cam.read()
    cv2.imshow("Python Camera by dknaix", frame)
    if not ret:
        break
    k = cv2.waitKey(1)

    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name = "rqv2_cv2_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1

cam.release()

cv2.destroyAllWindows()
