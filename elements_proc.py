import cv2
from read_input_elements import Reader


def find_element_in_image(target_frame, element):
    method = cv2.TM_SQDIFF_NORMED

    result = cv2.matchTemplate(element, target_frame, method)

    # We want the minimum squared difference
    mn, _, mnLoc, _ = cv2.minMaxLoc(result)

    # Draw the rectangle:
    # Extract the coordinates of our best match
    MPx, MPy = mnLoc

    # Step 2: Get the size of the template. This is the same size as the match.
    trows, tcols = element.shape[:2]

    # Step 3: Draw the rectangle on target_frame
    cv2.rectangle(target_frame, (MPx, MPy), (MPx + tcols, MPy + trows), (0, 0, 255), 2)

    # Display the original image with the rectangle around the match.
    cv2.imshow('output', target_frame)

    # The image is only displayed if we call this
    cv2.waitKey(0)


reader = Reader()
reader.load_gui_elements()
reader.load_video('app_rec.mov')

find_element_in_image(reader.video_frames[0], reader.gui_elements[7])
