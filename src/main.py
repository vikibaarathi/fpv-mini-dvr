
# import the opencv library
import cv2
import json
from cv2 import VideoWriter
from cv2 import VideoWriter_fourcc
from RHManager import RHManager
  
config_json = open("config.json")
config =  json.load(config_json)
vid_source = config["source"]
DISPLAY_STATUS = ""
  
# define a video capture object
vid = cv2.VideoCapture(vid_source)

width = int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
file_path = "media/heat1.mp4"
fps = 15

fourcc = VideoWriter_fourcc('m', 'p', '4', 'v')
writer = VideoWriter(file_path,fourcc,fps,(width,height))

#Create an instance of the Rotor Hazard Manager
rh = RHManager()

counter = 0
 
while(True):
      
    # Capture the video frame
    # by frame
    ret, frame = vid.read()
    font = cv2.FONT_HERSHEY_SIMPLEX
  
    # Use putText() method for
    # inserting text on video

    #Fire the API every 30 frames
    if counter > 30:
        counter = 0
        status = rh.getLiveRaceState()

        #Log and save if status changed
        if DISPLAY_STATUS != status:
            DISPLAY_STATUS = status
            print(DISPLAY_STATUS)


    cv2.putText(frame, DISPLAY_STATUS, (50, 50), font, 1, (3, 3, 3), 2, cv2.LINE_4)
    counter = counter + 1
    # Display the resulting frame
    cv2.imshow('frame', frame)
    
    #Record and stop only when race is running
    if DISPLAY_STATUS == "Get Ready" or DISPLAY_STATUS == "Race Started":    
        writer.write(frame)  


    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
  
# After the loop release the cap object
vid.release()
writer.release()

cv2.destroyAllWindows()