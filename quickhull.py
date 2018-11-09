#QUICKHULL.PY
#by AZKANAB 16013
#Membentuk garis pada titik - titik terluar dari titik - titik yang sudah ada

import random
import math
import matplotlib.pyplot as plt

print()
print(">>>	              __        __           __           __ __ 	<<<")
print(">>>	.-----.--.--.|__|.----.|  |--.______|  |--.--.--.|  |  |	<<<")
print(">>>	|  _  |  |  ||  ||  __||    <|______|     |  |  ||  |  |	<<<")
print(">>>	|__   |_____||__||____||__|__|      |__|__|_____||__|__|	<<<")
print(">>>	   |__|                                                 	<<<")
print("			by Azka Nabilah Mumtaz - 13516013				")
print("===========================================================================")

#LANGKAH 1
#Membentuk list of point secara random
print()
print("=======================     INPUT JUMLAH TITIK     ========================")
print()
ntitik = int(input("Masukan jumlah titik : "))
listpoint = []
for i in range (0, ntitik):
	x = random.randint(-50,50)
	y = random.randint(-50,50)
	point = (x,y)
	listpoint.append(point)
print()
print("================     TITIK YANG AKAN DIBENTUK QUICK-HULL     =============")
print()
print(listpoint)

#LANGKAH 2
#Mencari titik dengan x minimum dan x maksimum

xmin = int(listpoint[0][0])
xmax = int(listpoint[0][0])
for i in range (0, ntitik):
	if listpoint[i][0] >= xmax :
		xmax = int(listpoint[i][0])
		ymax = int(listpoint[i][1])
	if listpoint[i][0] <= xmin :
		xmin = int(listpoint[i][0])
		ymin = int(listpoint[i][1])

#LANGKAH 3
#Mencari titik dengan jarak terjauh dari garis yang dibentuk oleh x minimum dan x maksimum

#Fungsi mencari jarak titik antar garis
def jaraktitik (x1,y1,a1,b1,c1) :
	x = int(x1)
	y = int(y1)
	a = int(a1)
	b = int(b1)
	c = int(c1)
	atas = (a*x) + (b*y) + c
	if atas < 0 :
		atas *= -1 #nilai mutlak
	bawah = math.sqrt((a*a) + (b*b))
	return atas / bawah ;
	
#Fungsi mencari determinan untuk menentukan apakah titik tsb berada di kiri atau kanan garis
def determinan (x1,y1,x2,y2,x3,y3) :
	return (x1 * y2) + (x3 * y1) + (x2 * y3) - (x3 * y2) - (x2 * y1) - (x1 * y3);
	
#Fungsi mencari titik terjauh dari garis yang dibentuk oleh 2 titik
def pointmaks (S,x1,y1,x2,y2) : #x2 harus lebih besar dari x1
	#p,q,r adalah konstanta persamaan garis dengan p.x + q.y + r = 0
	p = y2 - y1
	q = x1 - x2
	r = ((x2 - x1)*y1) - ((y2-y1)*x1)
	jarakmaks = 0
	xjarakmaks = 0
	yjarakmaks = 0
	for i in range (0, len(S)) :
		x = int(S[i][0])
		y = int(S[i][1])
		if jaraktitik(x,y,p,q,r) >= jarakmaks :
			jarakmaks = jaraktitik(x,y,p,q,r)
			xjarakmaks = x
			yjarakmaks = y
	maksimum = (xjarakmaks, yjarakmaks)
	return maksimum;

#LANGKAH 4
#Membuat rekursi convex hull

#x dari p2 > x dari p1
def getleft (Sk,p1,p2) : #Mendapatkan himpunan titik yang berada di kiri garis antara p1 & p2
	Sleft = []
	x1 = p1[0]
	y1 = p1[1]
	x2 = p2[0]
	y2 = p2[1]
	#p,q,r adalah konstanta persamaan garis dengan p.x + q.y + r = 0
	p = y2 - y1
	q = x1 - x2
	r = ((x2 - x1)*y1) - ((y2-y1)*x1)
	for i in range (0, len(Sk)) :
		x3 = Sk[i][0]
		y3 = Sk[i][1]
		if determinan(x1,y1,x2,y2,x3,y3) > 0 :
			poin = (x3,y3)
			Sleft.append(poin)
	return Sleft;

def getright (Sk,p1,p2) : #Mendapatkan himpunan titik yang berada di kanan garis antara p1 & p2
	Sright = []
	x1 = p1[0]
	y1 = p1[1]
	x2 = p2[0]
	y2 = p2[1]
	#p,q,r adalah konstanta persamaan garis dengan p.x + q.y + r = 0
	p = y2 - y1
	q = x1 - x2
	r = ((x2 - x1)*y1) - ((y2-y1)*x1)
	for i in range (0, len(Sk)) :
		x3 = Sk[i][0]
		y3 = Sk[i][1]
		if determinan(x1,y1,x2,y2,x3,y3) < 0 :
			poin = (x3,y3)
			Sright.append(poin)
	return Sright;

#x dari P < x dari Q
def findHull (Sk,P,Q) : #Sk adalah set yang akan dicari convex hullnya
	if len(Sk) == 0 :
		return
	else :
		x1 = P[0]
		y1 = P[1]
		x2 = Q[0]
		y2 = Q[1]
		C = pointmaks(Sk,x1,y1,x2,y2)
		pconhul.append(C)
		SPC = getright(Sk,P,C) #SPC adalah himpunan point berada di kanan garis P-C
		SCQ = getright(Sk,C,Q) #SCQ adalah himpunan point berada di kanan garis C-Q
		findHull(SPC, P, C)
		findHull(SCQ, C, Q)

pconhul = []
pointmin = (xmin,ymin)
pointmax = (xmax,ymax)
pconhul.append(pointmin)
pconhul.append(pointmax)
S1 = getright(listpoint,pointmin,pointmax)
S2 = getleft(listpoint,pointmin,pointmax)
findHull(S1,pointmin,pointmax)
findHull(S2,pointmax,pointmin)

#LANGKAH 5
#Sort titik - titik convex hull (sort point clockwise)

def isMember(P,S) : #apakah poin p termasuk member dari list S
	x = P[0]
	y = P[1]
	for i in range (0, len(S)) :
		if x == S[i][0] and y == S[i][1] :
			return True
	return False

kiri = getleft(listpoint,pointmin,pointmax)
kanan = getright(listpoint,pointmin,pointmax)
kirisort = sorted(kiri, key = lambda p : p[0])
kanansort = sorted(kanan, key = lambda p : p[0], reverse = True)

pconhulsort = []
pconhulsort.append(pointmin)
for i in range (0, len(kiri)) :
	if isMember(kirisort[i], pconhul) :
		pconhulsort.append(kirisort[i])
pconhulsort.append(pointmax)
for i in range (0, len(kanan)) :
	if isMember(kanansort[i], pconhul) :
		pconhulsort.append(kanansort[i])

print()
print("=====================     LIST HASIL QUICK-HULL     ====================== ")
print()
print(pconhulsort)

#LANGKAH 6
#Gambar dan visualisasikan dengan matplotlib

#Membuat titik - titik non convex hull	
for i in range (0, ntitik) :
	if not isMember(listpoint[i], pconhul) :
		plt.plot(listpoint[i][0],listpoint[i][1],'ro')

#Membuat titik - titik convex hull
for i in range (0, len(pconhul)) :
	plt.plot(pconhul[i][0], pconhul[i][1], 'bo')

#Membuat garis convex hull
conhulx = []
conhuly = []
for i in range (0, len(pconhulsort)) :
	conhulx.append(pconhulsort[i][0])
for i in range (0, len(pconhulsort)) :
	conhuly.append(pconhulsort[i][1])
conhulx.append(pconhulsort[0][0])
conhuly.append(pconhulsort[0][1])

plt.plot(conhulx, conhuly)

#Membuat sumbu x dan y
plt.axis([-60, 60, -60, 60])

#Menampilkan gambar
plt.show()
