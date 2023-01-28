# FPV Mini DVR
## A simple personal DVR solution for recording FPV footage with lap time integration (RotorHazard).
### This is work in progress.
If you are trying to achieve faster laps around a race track, you will find yourself reviewing your FPV footage from the training sessions. If you dont have any fancy streaming equipment/goggles already, you would have to remove the SD card from the goggles, load it up on a PC, search for the footage and figure out a way to time the laps again. This given the goggles were recording in the first place. 

This solution is meant to run on a PC or on a small computer such as a Raspberry PI.
The idea is to solve the above problem by:
* Run application on PC / Raspberry PI
* Application detects camera / video source input
* Application detects presence of Rotor Hazard timing system
* App detects that a race has started.
* App overlays lap information on video.
* App records video when race starts and stops when ends
* App pushes video to cloud for easy access with identifiable information such as heat number, round number, channel, etc. 
