import sys
import pygame
import random
from pygame.locals import *
x=0
y=0

top = pygame.image.load("images.jpg")
top2=pygame.image.load("images.jpg")
top3=pygame.image.load("images.jpg")
top4=pygame.image.load("images.jpg")
top5= pygame.image.load("images.jpg")
top6=pygame.image.load("images.jpg")
top7=pygame.image.load("images.jpg")
top8=pygame.image.load("images.jpg")
top9=pygame.image.load("images.jpg")
top10=pygame.image.load("images.jpg")
top11=pygame.image.load("images.jpg")
top12=pygame.image.load("images.jpg")
tops=pygame.image.load("a.png")
(cu,ck)=top.get_size()

pygame.init()
surface = pygame.display.set_mode((720,800))
font=pygame.font.SysFont("Arial", 59
)
font2=pygame.font.SysFont('Arial',80)
yazı=font.render('BAŞLAMAK İÇİN DOKUN',1,(255,255,255))
bitis_yazı=font.render('GAME OVER ',1,(0,0,255))
bitis_yazı2=font.render('Tekrar Oynamak İçin Dokun',1,(255,255,255))
skor=0
a=200
direk_1=0
direk_2=0
direk_3=0
direk_4=0
direk_5=0
direk_6=0
z=0
p=700
acıklık=300
mesafe=200
t=0
sfrl1=0
sfrl2=0
sfrl3=0
sfrl4=0
sfrl5=0
hız=10
sart=0
artı=0
deney=0
fps=60


while True:
	skor1=font2.render(str(skor),1,(255,255,255))
	skor2=font2.render('SKOR',1,(255,255,255))
	surface.fill((255, 0 ,80))
	pygame.time.Clock().tick(fps)
	mousex,mousey=pygame.mouse.get_pos()
	if artı==0:
		mousex=0
		mousey=0
	if sart <=1:
		if z==0:
			a+=10
		if z==1:
			a-=10
		if a==700:
			z=1
		if a==200:
		
			z=0
		if t==0:
			p-=10
		if t==1:
			p+=10
		if p==200:
			t=1
		if p==700:
			t=0
		if random.randint(1,2)==1 and sfrl1==0:
			sans1=a
			sfrl1=1
		if sfrl1==0:
			sans1=p
			sfrl1=2
		if random.randint(1,2)==1 and sfrl2==0:
			sans2=a
			sfrl2=1
		if sfrl2==0:
			sans2=p
			sfrl2=2
		if random.randint(1,2)==1 and sfrl3==0:
			sans3=a
			sfrl3=1
		if sfrl3==0:
			sans3=p
			sfrl3=2
		if random.randint(1,2)==1 and sfrl4==0:
			sans4=a
			sfrl4=1
		if sfrl4==0:
			sans4=p
			sfrl4=2
		if random.randint(1,2)==1 and sfrl5==0:
			sans5=a
			sfrl5=1
		if sfrl5==0:
			sans5=p
			sfrl5=2
		if sfrl1==1:
			sans1=a
		if sfrl1==2:
			sans1=p
		if sfrl2==1:
			sans2=a
		if sfrl2==2:
			sans2=p
		if sfrl3==1:
			sans3=a
		if sfrl3==2:
			sans3=p
		if sfrl4==1:
			sans4=a
		if sfrl4==2:
			sans4=p
		if sfrl5==1:
			sans5=a
		if sfrl5==2:
			sans5=p
		if not mousex==0 and not mousey==0:
			if mousex<sans1-300 and direk_1<mousey<direk_1+ck:
				sart+=1
			if sans1-300+acıklık<mousex and direk_1<mousey<direk_1+ck:
				sart+=1
			if mousex<sans2-250 and direk_2+mesafe-55<mousey<direk_2+mesafe+ck:
				sart+=1
			if mousex>sans2-330+acıklık and direk_2+mesafe-55<mousey<direk_2+mesafe+ck:
				sart+=1
			if mousex<sans3-350 and direk_3+2*mesafe-55<mousey<direk_3+2*mesafe+ck:
				sart+=1
			if mousex>sans3-50 and direk_3+2*mesafe-55<mousey<direk_3+2*mesafe+ck:
				sart+=1
			if mousex<sans4-200 and direk_4+3*mesafe-55<mousey<direk_4+3*mesafe+ck:
				sart+=1
			if mousex>sans4-350+acıklık and direk_4+3*mesafe-55<mousey<direk_4+3*mesafe+ck:
				sart+=1
			if mousex<sans5-350 and direk_5+4*mesafe-55<mousey<direk_5+4*mesafe+ck:
				sart+=1
			if mousex>sans5-50 and direk_5+4*mesafe-55<mousey<direk_5+4*mesafe+ck:
				sart+=1
			if mousex<a-330 and direk_6+5*mesafe-55<mousey<direk_6+5*mesafe+ck:
				sart+=1
			if mousex>a-50 and direk_6+5*mesafe-55<mousey<direk_6+5*mesafe+ck:
				sart+=1
			if direk_1<=1280:
				direk_1+=hız
			else:
				skor+=1
				direk_1=0
			if direk_2<=1080:
				direk_2+=hız
			else:
				skor+=1
				direk_2=-1*mesafe
			if direk_3<=880:
				direk_3+=hız
			else:
				skor+=1
				direk_3=-2*mesafe
			if direk_4<=680:
				direk_4+=hız
			else:
				skor+=1
				direk_4=-3*mesafe
			if direk_5<=480:
				direk_5+=hız
			else:
				skor+=1
				direk_5=-4*mesafe
			if direk_6<=280:
				direk_6+=hız
			else:
				skor+=1
				direk_6=-5*mesafe
			
		if mousex==0 and mousey==0:
			surface.blit(yazı,(50,475))
		surface.blit(top,(sans1+50,direk_1))
		surface.blit(top2,((50+sans1-cu-acıklık-40),direk_1))
		surface.blit(top3,(sans2,direk_2+mesafe))
		surface.blit(top4,(sans2-cu-acıklık+50,direk_2+mesafe))
		surface.blit(top5,(sans3,direk_3+2*mesafe))
		surface.blit(top6,(sans3-cu-acıklık-50,direk_3 +2*mesafe))
		surface.blit(top7,(sans4,direk_4+3*mesafe))
		surface.blit(top8,(sans4-cu-acıklık+100,direk_4+3*mesafe))
		surface.blit(top9,(sans5,direk_5+4*mesafe))
		surface.blit(top10,(sans5-cu-acıklık-75,direk_5+4*mesafe))
		surface.blit(top11,(a,direk_6+5*mesafe))
		surface.blit(top12,(a-cu-acıklık,direk_6+5*mesafe))
		
		if not mousex==0 and not mousey==0:
			surface.blit(tops,(mousex,mousey))
			surface.blit(skor1,(450,100))
			surface.blit(skor2,(250,100))
	if sart >1:
		surface.blit(bitis_yazı,(200,600))
		surface.blit(bitis_yazı2,(0,800))
		if deney==0:
			artı=0
		deney+=1
		if artı==1:
			a=200
			direk_1=0
			direk_2=0
			direk_3=0
			direk_4=0
			direk_5=0
			direk_6=0
			z=0
			p=700
			acıklık=300
			mesafe=200
			t=0
			sfrl1=0
			sfrl2=0
			sfrl3=0
			sfrl4=0
			sfrl5=0
			hız=10
			sart=0
			skor=0
			artı=0
			deney=0
			
	pygame.display.update()
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
		if event.type == pygame.MOUSEBUTTONDOWN:
			artı+=1
			pygame.mouse.get_rel()
			
