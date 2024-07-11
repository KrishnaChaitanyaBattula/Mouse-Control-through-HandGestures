import numpy as np
def get_angle(a , b , c):
    radians=np.arctan2(c[1]-b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1] , a[0] - b[0])
    ang=np.abs(np.degrees(radians))
    return ang
def get_distance(landmark_list):
    if len(landmark_list)<2:
        return
    
    (x1 ,y1) , (x2 , y2) = landmark_list[0] , landmark_list[1]
    L=np.hypot(x2 - x1 ,y2 - y1)
    #to transform value from 0-1 to 0-1000
    return np.interp(L , [0,1] , [0 , 1000])