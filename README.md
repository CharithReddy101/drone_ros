# drone_ros

## Introduction to Whycon Markers
WhyCon is a computer vision based system which can be used to localize mobile robots upto mm precision. Generally we use external localization systems based on GPS, ultrasound, IR, radio, multi camera systems. But they are expensive, complex and also may take more weight. So such systems cannot be used for small robots or swarms if we need a low-cost robot. 


Whycon markers solve this problem by using very less computation, low-cost camera and good precision in pose estimation. They are concentric circles with  a white background. It uses different image processing techniques to localize the robot and estimate the pose.

![](img/whycon.png)

*Note:I will be updating the readme after the implementation. For more information, visit this [repo](https://github.com/lrse/whycon).*


## Introduction to AruCo Markers
AruCo markers are binary sqaure matrices which are used for localization and pose estimation just like WhyCon markers. But the difference is  AruCo markers are more robust when compared to WayCon markers.
![](img/aruco.png)

Let's consider a 7x7 AruCo marker.Divide it equally into rows and columns which will result in 7X7 blocks with binary colors. If we remove the outer black layer, we are left with a 5X5 matrix. In this, 1,3,5 coulmns are parity bits and 2,4 columns are data bits. So we will be left with 10 data bits which can give a combination of 2^10=1024 different AruCo markers. These markers can be used for pose estimation, camera caliberation and many more applications. We can also use these markers to direct a robot in a warehouse by giving different functionalities to different IDs.

*Note:I will be updating the readme after the implementation.*

## Open loop vs Closed loop


## PID Algorithm

