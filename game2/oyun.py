import sys
import pygame
import random
from pygame.locals import *

top = pygame.image.load("images1.jpg")
top2=pygame.image.load("images1.jpg")
top3=pygame.image.load("images1.jpg")
top4=pygame.image.load("images1.jpg")
top5= pygame.image.load("images1.jpg")
top6=pygame.image.load("images1.jpg")
top7=pygame.image.load("images1.jpg")
top8=pygame.image.load("images1.jpg")
top9=pygame.image.load("images1.jpg")
top10=pygame.image.load("images1.jpg")
tops=pygame.image.load("a.png")
background= pygame.image.load("background3.jpg")
background=pygame.transform.scale(background,(720,1600))
pygame.init()
surface = pygame.display.set_mode((720,800))
font=pygame.font.SysFont("Freesans", 66,bold=True
)
font2=pygame.font.SysFont('Arial',59)
yazı=font.render('BAŞLAMAK İÇİN DOKUN',1,(255,255,255))
yazı2=font.render('GAME OVER',1,(255,0,0))
yazı3=font2.render('Tekrar Oynamak İçin Dokun',1,(255,255,255))
konum=top.get_rect()
konum2=top2.get_rect()
konum3=top3.get_rect()
konum4=top4.get_rect()
konum5=top5.get_rect()
konum6=top6.get_rect()
konum7=top7.get_rect()
konum8=top8.get_rect()
konum9=top9.get_rect()
konum10=top10.get_rect()
hızx=5
k=400
a=500
b=30
skor=0
c=0
d=0
artı=0
artı2=0
yercekimi=1
şart=0
şart2=0
if random.randint(-10,10)<=0:
	ters1=1
else:
	ters1=-1
if random.randint(-10,10)<=0:
	ters2=1
else:
	ters2=-1
if random.randint(-10,10)<=0:
	ters3=1
else:
	ters3=-1
if random.randint(-10,10)<=0:
	ters4=1
else:
	ters4=-1
if random.randint(-10,10)<=0:
	ters5=1
else:
	ters5=-1
konum=pygame.Rect((0,0),top.get_size())
konum2=pygame.Rect((0,0),top2.get_size())
konum3=pygame.Rect((0,k),top3.get_size())
konum4=pygame.Rect((0,k),top4.get_size())
konum5=pygame.Rect((0,2*k),top5.get_size())
konum6=pygame.Rect((0,2*k),top6.get_size())
konum7=pygame.Rect((0,3*k),top7.get_size())
konum8=pygame.Rect((0,3*k),top8.get_size())
konum9=pygame.Rect((0,4*k),top9.get_size())
konum10=pygame.Rect((0,4*k),top10.get_size())
while True:
	pygame.time.Clock().tick(60)
	skor1=font.render('SKOR',1,(255,255,255))
	skor2=font.render(str(skor),1,(255,255,255))
	surface.blit(background,(0,0))
	if şart==0:
		if şart2==0:
			surface.blit(yazı,(0,600))
		if artı2>0:
			şart=1
		hızx=5
		hızy=5
		k=400
		a=500
		b=30
		c=-5
		skor=0
		artı=0
		yercekimi=1
		if random.randint(-10,10)<=0:
			ters1=1
		else:
			ters1=-1
		if random.randint(-10,10)<=0:
			ters2=1
		else:
			ters2=-1
		if random.randint(-10,10)<=0:
			ters3=1
		else:
			ters3=-1
		if random.randint(-10,10)<=0:
			ters4=1
		else:
			ters4=-1
		if random.randint(-10,10)<=0:
			ters5=1
		else:
			ters5=-1
		konum=pygame.Rect((0,0),top.get_size())
		konum2=pygame.Rect((0,0),top2.get_size())
		konum3=pygame.Rect((0,k),top3.get_size())
		konum4=pygame.Rect((0,k),top4.get_size())
		konum5=pygame.Rect((0,2*k),top5.get_size())
		konum6=pygame.Rect((0,2*k),top6.get_size())
		konum7=pygame.Rect((0,3*k),top7.get_size())
		konum8=pygame.Rect((0,3*k),top8.get_size())
		konum9=pygame.Rect((0,4*k),top9.get_size())
		konum10=pygame.Rect((0,4*k),top10.get_size())

	if şart==1:
		surface.blit(background,(0,0))
		mousex,mousey=pygame.mouse.get_pos()
		(t1x,t1y,t1z,t1f)=konum
		(t2x,t2y,t2z,t2f)=konum2
		(t3x,t3y,t3z,t3f)=konum3
		(t4x,t4y,t4z,t4f)=konum4
		(t5x,t5y,t3z,t3f)=konum5
		(t6x,t6y,t3z,t3f)=konum6
		(t7x,t7y,t3z,t3f)=konum7
		(t8x,t8y,t3z,t3f)=konum8
		(t9x,t9y,t3z,t3f)=konum9
		(t10x,t10y,t3z,t3f)=konum10
		if ters1==1:
			if t1x==500:
				konum2=pygame.Rect((-300,t2y),top2.get_size())
		if ters1==-1:
			if t1x==0 and t1x>-100:
				konum2=pygame.Rect((800,t2y),top2.get_size())
		if ters1==1:
			if t2x==490:
				konum=pygame.Rect((-300,t1y),top.get_size())
		if ters1==-1:
			if t2x==5 and t2x>-100:
				konum=pygame.Rect((800,t1y),top2.get_size())
		if t1y>=1200:
			konum=pygame.Rect((t1x,0),top.get_size())
			if random.randint(-10,10)<=0:
				ters1=1
			else:
				ters1=-1
		if t2y>=1200:
			if a<1200:
				skor+=1
			konum2=pygame.Rect((t2x,0),top2.get_size())
		if ters2==1:
			if t3x==500:
				konum4=pygame.Rect((-300,t4y),top4.get_size())
		if ters2==-1:
			if t3x==0:
				konum4=pygame.Rect((800,t4y),top2.get_size())
		if ters2==1:
			if t4x==490:
				konum3=pygame.Rect((-300,t3y),top3.get_size())
		if ters2==-1:
			if t4x==5:
				konum3=pygame.Rect((800,t3y),top2.get_size())
		if t3y>=1200:
			if a<1200:
				skor+=1
				pygame.mixer.Sound('point.ogg').play()
			konum3=pygame.Rect((t3x,0),top3.get_size())
			if random.randint(-10,10)<=0:
				ters2=1
			else:
				ters2=-1
		if t4y>=1200:
			konum4=pygame.Rect((t4x,0),top4.get_size())
		if ters3==1:
			if t5x==500:
				konum6=pygame.Rect((-300,t6y),top6.get_size())
		if ters3==-1:
			if t5x==0:
				konum6=pygame.Rect((800,t6y),top6.get_size())
		if ters3==1:
			if t6x==490:
				konum5=pygame.Rect((-300,t5y),top5.get_size())
		if ters3==-1:
			if t6x==5:
				konum5=pygame.Rect((800,t5y),top5.get_size())
		if t5y>=1200:
			if a <1200:
				skor+=1
			konum5=pygame.Rect((t5x,0),top5.get_size())
			if random.randint(-10,10)<=0:
				ters3=1
			else:
				ters3=-1
		if t6y>=1200:
			konum6=pygame.Rect((t6x,0),top6.get_size())
		if ters4==1:
			if t7x==500:
				konum8=pygame.Rect((-300,t8y),top8.get_size())
		if ters4==-1:
			if t7x==0:
				konum8=pygame.Rect((800,t8y),top8.get_size())
		if ters4==1:
			if t8x==490:
				konum7=pygame.Rect((-300,t7y),top7.get_size())
		if ters4==-1:
			if t8x==5:
				konum7=pygame.Rect((800,t7y),top7.get_size())
		if t7y>=1200:
			if a<1200:
				skor+=1
			konum7=pygame.Rect((t7x,0),top7.get_size())
			if random.randint(-10,10)<=0:
				ters4=1
			else:
				ters4=-1
		if t8y>=1200:
			konum8=pygame.Rect((t8x,0),top8.get_size())
		if ters5==1:
			if t9x==500:
				konum10=pygame.Rect((-300,t10y),top10.get_size())
		if ters5==-1:
			if t9x==0:
				konum10=pygame.Rect((800,t10y),top10.get_size())
		if ters5==1:
			if t10x==490:
				konum9=pygame.Rect((-300,t9y),top9.get_size())
		if ters5==-1:
			if t10x==5:
				konum9=pygame.Rect((800,t9y),top9.get_size())
		if t9y==1200:
			konum9=pygame.Rect((t9x,0),top9.get_size())
			if random.randint(-10,10)<=0:
				ters5=1
			else:
				ters5=-1
		if t10y==1200:
			konum10=pygame.Rect((t10x,0),top10.get_size())
			
		
		konum=konum.move(ters1*hızx,hızy)
		konum2=konum2.move(ters1*hızx,hızy)
		konum3=konum3.move(ters2*hızx,hızy)
		konum4=konum4.move(ters2*hızx,hızy)
		konum5=konum5.move(ters3*hızx,hızy)
		konum6=konum6.move(ters3*hızx,hızy)
		konum7=konum7.move(ters4*hızx,hızy)
		konum8=konum8.move(ters4*hızx,hızy)
		konum9=konum9.move(ters5*hızx,hızy)
		konum10=konum10.move(ters5*hızx,hızy)
		
		surface.blit(top,konum)
		surface.blit(top2,konum2)
		surface.blit(top3,konum3)
		surface.blit(top4,konum4)
		surface.blit(top5,konum5)
		surface.blit(top6,konum6)
		if t7x<mousex<t7x+300 and t7y-50<a<t7y+50:
			if yercekimi==1:
				yercekimi=0
				b=30
		if t8x<mousex<t8x+300 and t8y-50<a<t8y+50:
			if yercekimi==1:
				yercekimi=0
				b=30
		if t6x<mousex<t6x+300 and t6y-50<a<t6y+50:
			if yercekimi==1:
				yercekimi=0
				b=30
		if t5x<mousex<t5x+300 and t5y-50<a<t5y+50:
			if yercekimi==1:
				yercekimi=0
				b=30
		if t4x<mousex<t4x+300 and t4y-50<a<t4y+50:
			if yercekimi==1:
				yercekimi=0
				b=30
		if t3x<mousex<t3x+300 and t3y-50<a<t3y+50:
			if yercekimi==1:
				yercekimi=0
				b=30
		if t2x<mousex<t2x+300 and t2y-50<a<t2y+50:
			if yercekimi==1:
				yercekimi=0
				b=30
		if t1x<mousex<t1x+300 and t1y-50<a<t1y+50:
			yercekimi=0
			b=30
		if yercekimi==0 and not b==-10:
			if b>-20:
				b-=2
			a-=2*b
		else:
			yercekimi=1
		if yercekimi==1:
			if c<d:
				c+=2
			a+=2*c
		if a>1200:
			if artı >0:
				şart=0
			şart2+=1
			surface.blit(yazı2,(200,600))
			surface.blit(yazı3,(0,700))
		if a<0:
			hızy=25
			d=50
		else:
			hızy=10
			d=26
		surface.blit(tops,(mousex,a))
		surface.blit(skor1,(200,100))
		surface.blit(skor2,(400,100))

	pygame.display.update()
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
		if event.type == pygame.MOUSEBUTTONDOWN:
			artı2+=1
			if a>1200:
				artı+=1
			pygame.mouse.get_rel()
#
