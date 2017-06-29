from django.http import JsonResponse#, HttpResponse, Http404
from django.shortcuts import render
from scipy.misc import imread, imresize#, imsave
from keras.models import load_model
from io import BytesIO
import numpy as np
import base64
import cv2
import re

def page(request):
	if request.POST:
		model = load_model('/path/to/model/mnist_model.h5')
		#model.load_weights('/path/to/weights/mnist_weights.h5')

		im = imread(BytesIO(base64.b64decode(re.search(r'base64,(.*)',request.POST['img']).group(1))),mode='L')
		im = np.invert(im)

		_, contours, hierarchy = cv2.findContours(cv2.threshold(im,127,255,0)[1],cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
		x,y,w,h                = cv2.boundingRect(contours[0])
		im                     = imresize(im[y:y+h,x:x+w],(28,28))

		#imsave('output_resized.png', im)

		out      = model.predict(im.reshape((1,28,28,1)))
		response = np.array_str(np.argmax(out,axis=1))
		return JsonResponse({'response':response})
	return render(request, 'mnist.html')
