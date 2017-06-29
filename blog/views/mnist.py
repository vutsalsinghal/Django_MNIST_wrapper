from django.http import JsonResponse#, HttpResponse, Http404
from django.shortcuts import render
from scipy.misc import imread, imresize#, imsave
from keras.models import load_model
import base64
import numpy as np
import re

def convertImage(imgData1):
	imgstr = re.search(r'base64,(.*)',imgData1).group(1)
	with open('output.png','wb') as output:
		output.write(base64.b64decode(imgstr))

def page(request):
	if request.POST:
		#print('[INFO] Loding saved model and weights from disk...')
		model = load_model('blog/NN_model/mnist_model.h5')
		#model.load_weights('blog/NN_model/mnist_weights.h5')

		convertImage(request.POST['img'])
		x        = imread('output.png',mode='L')
		x        = np.invert(x)
		x        = imresize(x,(28,28))
		#imsave('output1.png', x)
		out      = model.predict(x.reshape((1,28,28,1)))
		response = np.array_str(np.argmax(out,axis=1))
		return JsonResponse({'response':response})
	return render(request, 'mnist.html')