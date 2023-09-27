import cv2
import numpy as np
resp = int(input("Menu\n1-Red\n2-Green\n3-Yellow\n4-Blue\n5-Brown\n6-Orange\n7-Violet\nEnter your choice:" ))
cap = cv2.VideoCapture(0)
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 150)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 100)
if resp==1:
	L_limit=np.array([136,87,111]) # setting the red lower limit
	U_limit=np.array([180,255,255]) # setting the red upper limit
elif resp==2:
	L_limit=np.array([25,52,72]) # setting the green lower limit
	U_limit=np.array([102,255,255]) # setting the green upper limit
elif resp==3:
	L_limit=np.array([20,100,100]) # setting the yellow lower limit
	U_limit=np.array([30,255,255]) # setting the yellow upper limit
elif resp==4:
	L_limit=np.array([98,50,50]) # setting the blue lower limit
	U_limit=np.array([139,255,255]) # setting the blue upper limit
elif resp==5:
	L_limit=np.array([10,100,20]) # setting the brown lower limit
	U_limit=np.array([20,255,200]) # setting the brown upper limit
elif resp==6:
	L_limit=np.array([10,100,20]) # setting the orange lower limit
	U_limit=np.array([25,255,255]) # setting the orange upper limit
else:
	L_limit=np.array([121,77,56]) # setting the violet lower limit
	U_limit=np.array([140,255,255]) # setting the violet upper limit

while 1:
	success,frame =cap.read() #read the image
	hsv =cv2.cvtColor(frame,cv2.COLOR_BGR2HSV) #converts to hsv image
	img_mask=cv2.inRange(hsv,L_limit,U_limit) #declaring the range for selection
	colour_mask=cv2.bitwise_and(frame,frame,mask=img_mask) #produce colour mask
	cv2.imshow('Original',frame) # to display the original frame
	cv2.imshow('Colour detector',colour_mask) # to display the blue object output
	if cv2.waitKey(1)==27:
		break 
cap.release()
cv2.destroyAllWindows()