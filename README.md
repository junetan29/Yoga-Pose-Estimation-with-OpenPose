# Demo
1. Download and install CMake, add the installation path to the system environment variable Path
![image](https://github.com/junetan29/Yoga-Pose-Estimation-with-OpenPose/assets/95990839/4fb7c780-e52f-4726-aa2f-5c35e5d35492)
2. Download Openpose from the link https://github.com/CMU-Perceptual-Computing-Lab/openpose/archive/refs/tags/v1.7.0.zip
3. Unzip the file, and create a new folder ‘build’ in the source root directory. This folder is used to store the files generated by compilation
4. Download other zip files for the following task. The links of the zip files are given below.

   caffe - https://github.com/CMU-Perceptual-Computing-Lab/caffe/tree/b5ede488952e40861e84e51a9f9fd8fe2395cc8a
   
   pybind11 - https://github.com/pybind/pybind11/tree/085a29436a8c472caaaf7157aa644b571079bcaa
5. Unzip files and store them in ‘3rdparty\caffe’ and ‘3rdparty\pybind11’
6. Open CMake-gui, fill in the source code location and the location of the compiled files, which is the 'build' directory just created above
![image](https://github.com/junetan29/Yoga-Pose-Estimation-with-OpenPose/assets/95990839/5f838fc0-85b9-415f-8caa-f98b2721fc06)
7. Click the ‘Configure’ button below. In this step, several main dependencies will be downloaded, including ‘opencv’, ‘caffe’, ‘caffe3rdparty’, and the model files that need to be used in the project.
![image](https://github.com/junetan29/Yoga-Pose-Estimation-with-OpenPose/assets/95990839/030aa1d0-c9e5-44e1-949e-94ad24d1db6b)
![image](https://github.com/junetan29/Yoga-Pose-Estimation-with-OpenPose/assets/95990839/513bc617-d4cd-4549-854b-6c657050e9b3)
8. Click ‘Generate’ to generate the Visual Studio solution
![image](https://github.com/junetan29/Yoga-Pose-Estimation-with-OpenPose/assets/95990839/9aa086bd-5c54-4db6-b362-10507df22f2f)
9. Click ‘Open Project’ to enter Visual Studio
![image](https://github.com/junetan29/Yoga-Pose-Estimation-with-OpenPose/assets/95990839/5f86e985-dc04-486c-b441-e347baaf0799)
10. Right-click ‘OpenPoseDemo’ in the solution, select ‘Build’, and start compiling
![image](https://github.com/junetan29/Yoga-Pose-Estimation-with-OpenPose/assets/95990839/c5742ab1-3b68-470d-8361-a2be59118f72)
![image](https://github.com/junetan29/Yoga-Pose-Estimation-with-OpenPose/assets/95990839/19ba9876-0eac-40a0-bb3d-b4e1342c8746)
11. Right-click ‘OpenPoseDemo’ again and select ‘Set as Startup Project’
![image](https://github.com/junetan29/Yoga-Pose-Estimation-with-OpenPose/assets/95990839/f4b26f6f-68e9-4bde-b2db-de0b3d2c0a3d)
12. Add command line parameters in Visual Studio by right-clicking ‘OpenPoseDemo’ in the solution and select ‘Properties’ or by pressing Alt+Enter
![image](https://github.com/junetan29/Yoga-Pose-Estimation-with-OpenPose/assets/95990839/3efb7f67-7d0d-4316-b960-8eb48f3adea8)
13. Select ‘Debugging’, then add the command ```OpenPoseDemo.exe --image_dir [the path of image directory] --write_json [the path to save the json file] --net_resolution 160x160``` in ‘Command Arguments’
![image](https://github.com/junetan29/Yoga-Pose-Estimation-with-OpenPose/assets/95990839/df584a94-95a2-4203-9cdf-2510fe7939ea)
14. Click at the ‘Local Windows Debugger’
![image](https://github.com/junetan29/Yoga-Pose-Estimation-with-OpenPose/assets/95990839/b14458e0-0dfd-40ef-b43e-55663cf2ac7d)
15. The keypoints of the pose will be saved in json file as the image shown below 
![image](https://github.com/junetan29/Yoga-Pose-Estimation-with-OpenPose/assets/95990839/030cfcc2-8919-427d-808b-89aa032f2151)
 
# Reference
https://github.com/CMU-Perceptual-Computing-Lab/openpose