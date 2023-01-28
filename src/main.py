
# import the opencv library
import cv2
import json
from cv2 import VideoWriter
from cv2 import VideoWriter_fourcc
  
config_json = open("config.json")
config =  json.load(config_json)
vid_source = config["source"]
  
# define a video capture object
vid = cv2.VideoCapture(vid_source)

width = int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
file_path = "heat1.mp4"
fps = 30

fourcc = VideoWriter_fourcc('m', 'p', '4', 'v')
writer = VideoWriter(file_path,fourcc,fps,(width,height))



  
while(True):
      
    # Capture the video frame
    # by frame
    ret, frame = vid.read()
    font = cv2.FONT_HERSHEY_SIMPLEX
  
    # Use putText() method for
    # inserting text on video
    cv2.putText(frame, 'TEXT ON VIDEO', (50, 50), font, 1, (0, 255, 255), 2, cv2.LINE_4)
    # Display the resulting frame
    cv2.imshow('frame', frame)
    
      
    writer.write(frame)  
    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
  
# After the loop release the cap object
vid.release()
writer.release()
# Destroy all the windows
config.close()
cv2.destroyAllWindows()