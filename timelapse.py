import cv2, time

video = cv2.VideoCapture(0)

number_of_frames = 0

while True:
    number_of_frames += 1
    check, frame = video.read()

    print(check)
    print(frame)

    cv2.imshow("Capturing", frame)

    key=cv2.waitKey(1)

    if number_of_frames%500 == 0:
        cv2.imwrite(str(number_of_frames)+'.jpg', frame)

    if key==ord('q'):
        break

print(number_of_frames)
video.release()
cv2.destroyAllWindows()
