# Let's play around with some videos

import cv2 as cv
import numpy as np
import os

vid = cv.VideoCapture(0)

fourcc = cv.VideoWriter_fourcc(*'XVID')
clip = list()
while True:
    
    ret, frame = vid.read()
    cv.imshow('frame', frame)

    # Save the clip
    clip.append(frame)
    if len(clip) > 90:
        clip.pop(0)

    pressedKey = cv.waitKey(1)
    if pressedKey == -1:
        continue
    elif pressedKey == ord('q'):
        break
    else:
        # Save the clip
        # Check for highest clip_num corresponding to that key press
        # This might be a little slow, but it keeps it organized and only needed for training
        dir = os.listdir()
        outputs_chr = [f for f in dir if f.startswith('output_'+chr(pressedKey))]
        next_clip_num = np.max([int(f.split('_')[2].split('.')[0]) for f in outputs_chr]) + 1 if len(outputs_chr) > 0 else 0
        
        out = cv.VideoWriter('output_'+chr(pressedKey)+'_'+str(next_clip_num)+'.avi', fourcc, 20.0, (640, 480))
        for i in range(len(clip)):
            out.write(clip[i])
        out.release()


vid.release()
cv.destroyAllWindows()