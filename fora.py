#
# Autor:    diX - Diego Silva
# GitHub:   https://github.com/diwalker
# Email:    dwalkerserver@gmail.com
#
# Apoie meu trabalho: pix telefone 87988370228
import cvzone
import math
import cv2
from cvzone.ColorModule import ColorFinder
import numpy as np


def main3():
	# Inicialização do Video
	capThree = cv2.VideoCapture('Videos/Vid (1).mp4')

	# localizador de cores
	myColorFinder = ColorFinder(False)
	hsvVals = {'hmin': 8, 'smin': 95, 'vmin': 111, 'hmax': 14, 'smax': 255, 'vmax': 255}

	# Variaveis
	posListX, posListY = [], []
	xList = [item for item in range(0, 1300)]
	prediction = False

	while True:
		# Corte de imagem
		success, img = capThree.read()
		# img = cv2.imread("Ball.png")
		img = img[0:930, :]

		# Localizar a cor da bola
		imgColor, mask = myColorFinder.update(img, hsvVals)

		# Achar a localização da bola
		imgContours, contours = cvzone.findContours(img, mask, minArea=500)

		if contours:
			posListX.append(contours[0]['center'][0])
			posListY.append(contours[0]['center'][1])

		if posListX:
			# Regressão Polinomial y = Ax^2 + Bx + C
			# Achar os coeficientes
			A, B, C = np.polyfit(posListX, posListY, 2)

			for i, (posX, posY) in enumerate(zip(posListX, posListY)):
				pos = (posX, posY)
				cv2.circle(imgContours, pos, 10, (0, 255, 0), cv2.FILLED)

				if i == 0:
					cv2.line(imgContours, pos, pos, (0, 255, 0), 2)

				else:
					cv2.line(imgContours, pos, (posListX[i - 1], posListY[i - 1]), (0, 255, 0), 5)

			for x in xList:
				y = int(A * x ** 2 + B * x + C)
				cv2.circle(imgContours, (x, y), 2, (255, 0, 255), cv2.FILLED)

			if len(posListX) < 10:
				# Predição
				# Valor de X: 330 - 430 | Y: 590
				a = A
				b = B
				c = C - 590

				x = int((-b - math.sqrt(b ** 2 - (4 * a * c))) / (2 * a))
				prediction = 330 < x < 430

			if prediction:
				cvzone.putTextRect(imgContours, "CESTA!! :)", (50, 150),
				                   scale=5, thickness=5, colorR=(0, 255, 0), offset=20)

			else:
				cvzone.putTextRect(imgContours, "ERROU!! :(", (50, 150),
				                   scale=5, thickness=5, colorR=(0, 0, 200), offset=20)

		# Visualização
		imgContours = cv2.resize(imgContours, (0, 0), None, 0.7, 0.7)  # escala
		# cv2.imshow("Image", img)
		cv2.imshow("Basketbot, o preditor de arremessos!", imgContours)
		k = cv2.waitKey(100) & 0xFF
		if k == ord('q'):  # you can put any key here
			cv2.destroyAllWindows()
			break
if __name__ == "__main__":
	main3()
