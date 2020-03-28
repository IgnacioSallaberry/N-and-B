# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 00:14:00 2020

@author: ETCasa
"""
# Function to extract frames 
def FrameCapture(path): 
      
    # Path to video file 
    vidObj = cv2.VideoCapture(path) 
  
    # Used as counter variable 
    count = 0
  
    # checks whether frames were extracted 
    success = 1
  
    while success: 
  
        # vidObj object calls read 
        # function extract frames 
        success, image = vidObj.read() 
  
        # Saves the frames with frame-count 
        cv2.imwrite("frame%d.tiff" % count, image) 
  
        count += 1
  
# Driver Code 
if __name__ == '__main__': 
  
    # Calling the function 
    FrameCapture(r'C:\Users\ETCasa\Desktop\sim3-D_1-roi_128-tp_5us-clock_freq_200000_frame_movie.avi') 