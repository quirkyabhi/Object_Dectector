import cv2
import os
from tkinter import *
from tkinter import messagebox
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
# import numpy as np
import re
import time
def get_cam():
    camop = {}
    cams_test = 10
    for i in range(0, cams_test):
        cap = cv2.VideoCapture(i)
        test, frame = cap.read()
        if test:
            if i ==0:
                camop["Integrated Camera"] = 0
            else:
                camop["External Camera %d " % i] = i
    return camop
        

def open_cam(selcam):
    cam = cv2.VideoCapture(selcam)

    ic = 0
    while True:
        test, frame = cam.read()
        cv2.imshow("PRESS SPACE TO CAPTURE AND ESC TO CLOSE", frame)
        if not test:
            break
        k = cv2.waitKey(1)

        if k%256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            messagebox.showinfo("Processing","No pictures = %d\n Click to process further!\nPLEASE BE PATIENT TILL THE PROCESS COMPLETES"  % ic)
            break
        elif k%256 == 32:
            # SPACE pressed
            img_name = "img\\image_%d.jpg" % ic
            ic = ic + 1
            cv2.imwrite(img_name, frame)
            print("{} written!".format(img_name))

    cam.release()

    cv2.destroyAllWindows()

    
    ################################################################
    
    from imageai.Detection import ObjectDetection
    import os
    st=time.time()
    execution_path = os.getcwd()
    obj={}
    detector = ObjectDetection()
    detector.setModelTypeAsRetinaNet()
    detector.setModelPath( os.path.join(execution_path , "resnet50_coco_best_v2.0.1.h5"))
    detector.loadModel( )

    count = 0
    for i in range(0, ic):
        detections,extracted = detector.detectObjectsFromImage(input_image=os.path.join(execution_path , "img\\image_%d.jpg" % i), output_image_path=os.path.join(execution_path , "img\\imagenew_%d.jpg" %i), extract_detected_objects=True)
        df=pd.DataFrame(detections)
#         df1=pd.DataFrame(extracted)
        df["Extracted Img"]=extracted
        print(df)
    
    #creating excel sheet
    
        print("img\\image_%d.jpg" % i)
        base=os.path.basename("img\\image_%d.jpg" % i)
        writer = pd.ExcelWriter(r'countexcel/%s.xlsx'%base, engine='xlsxwriter')
        df.to_excel(writer, sheet_name='Sheet1')
        writer.save()
        print(base)

         
        for eachObject in detections:
            if eachObject["name"] == "person":
                count = count + 1
            print(eachObject["name"] , " : " , eachObject["percentage_probability"] )
            obj[eachObject["name"]]= eachObject["percentage_probability"]
    print("No of person is %d" % count)
    en=time.time()
    total=en-st
    print(total)
    #print('\n'.join(obj))

#     for i in range(0, ic):
        #os.remove(os.path.join(execution_path , r"img/image_%d.jpg" %i))
        #os.remove(os.path.join(execution_path , r"img/imagenew_%d.jpg" %i))
    return count,ic,obj
    
    ################################################################
def browse(filename):
    from imageai.Detection import ObjectDetection
    st=time.time()
    execution_path = os.getcwd()
    obj={}
    detector = ObjectDetection()
    detector.setModelTypeAsRetinaNet()
    detector.setModelPath( os.path.join(execution_path , "resnet50_coco_best_v2.0.1.h5"))
    detector.loadModel( )

    count = 0
    ic=1
    base=os.path.basename(filename)
    for i in range(0, ic):
        detections,extracted = detector.detectObjectsFromImage(input_image=os.path.join(execution_path,"%s" %filename), output_image_path = "img\\%s%i.jpg" %(base,i),extract_detected_objects=True)
        for eachObject in detections:
            if eachObject["name"] == "person":
                count = count + 1
            print(eachObject["name"] , " : " , eachObject["percentage_probability"] )
            obj[eachObject["name"]]= eachObject["percentage_probability"]
    print("No of person is %d" % count)
    en=time.time()
    #dataframe creation

    print(detections)
    print(extracted)
    df=pd.DataFrame(detections)
    df["Extracted Img"]=extracted
    print(df)
    
    #creating excel sheet
    
    print(filename)
    base=os.path.basename(filename)
    writer = pd.ExcelWriter(r'countexcel/%s.xlsx'%base, engine='xlsxwriter')
    df.to_excel(writer, sheet_name='Sheet1')
    writer.save()
    print(base)

    #for i in range(0, ic):
        #os.remove(os.path.join(execution_path , "%s%s" %(filename,i)))
        #os.remove(os.path.join(execution_path , "img/imagenew_%d.jpg" %i))
    total=en-st
    print(total)
    return count,ic,obj
    
