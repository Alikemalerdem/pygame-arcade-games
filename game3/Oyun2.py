import sys
import pygame
import random
from pygame.locals import *
pygame.init()
surface = pygame.display.set_mode((720,800))
font=pygame.font.SysFont('Arial',60)

fps=60
cdurum='runc'
değer=1
deger2=1
deger3=1
deger4=1
topx=350
topy=600
click=0
kural=0
kural1=0
kural2=0
kural3=0
kural4=0
hız=10
cb=80
ca=1200
b=80
a=640
hızrun=4
hızjump=3
hızkarakterx=13
zipyuk=30
karakterx=False
karaktery=False
canavarx=False
canavary=True
hata=7
durum='idle'
sarkı=0
sarkı1=0
sarkı3=0
sarkı4=0
butonsol='çek'
butonsağ='çek'
butonaş='çek'
butonyuk='çek'
background=pygame.image.load('background.png')
background=pygame.transform.scale(background,(720,1280))
run1c=pygame.image.load('run1c.png')
run1c=pygame.transform.scale(run1c,(250,250))
run2c=pygame.image.load('run2c.png')
run2c=pygame.transform.scale(run2c,(250,250))
run3c=pygame.image.load('run3c.png')
run3c=pygame.transform.scale(run3c,(250,250))
yok1=pygame.image.load('yok1.png')
yok1=pygame.transform.scale(yok1,(250,250))
yok2=pygame.image.load('yok2.png')
yok2=pygame.transform.scale(yok2,(250,250))
yok3=pygame.image.load('yok3.png')
yok3=pygame.transform.scale(yok3,(250,250))
yok4=pygame.image.load('yok4.png')
yok4=pygame.transform.scale(yok4,(250,250))
yok5=pygame.image.load('yok5.png')
yok5=pygame.transform.scale(yok5,(250,250))
yok6=pygame.image.load('yok6.png')
yok6=pygame.transform.scale(yok6,(250,250))
yok7=pygame.image.load('yok7.png')
yok7=pygame.transform.scale(yok7,(250,250))
idle1=pygame.image.load('idle1.png')
idle2=pygame.image.load('idle2.png')
run1=pygame.image.load('run1.png')
run2=pygame.image.load('run2.png')
run3=pygame.image.load('run3.png')
run4=pygame.image.load('run4.png')
jump1=pygame.image.load('jump1.png')
jump2=pygame.image.load('jump2.png')
jump3=pygame.image.load('jump3.png')
jump4=pygame.image.load('jump4.png')
top=pygame.image.load('a.png')
butsol=pygame.image.load('butsol.png')
butsağ=pygame.image.load('butsağ.png')
butyuk=pygame.image.load('butyuk.png')
butaş=pygame.image.load('butaş.png')
butsolk=pygame.image.load('butsolk.png')
butsağk=pygame.image.load('butsağk.png')
butyukk=pygame.image.load('butyukk.png')
butaşk=pygame.image.load('butaşk.png')
while True:
	for event in pygame.event.get():
		if event.type == QUIT:
				pygame.quit()
		if event.type == pygame.MOUSEBUTTONDOWN:
			click=1
			pygame.mouse.get_rel()
		if event.type == pygame.MOUSEBUTTONUP:
			click=0
			pygame.mouse.get_rel()
	mousex,mousey=pygame.mouse.get_pos()
	surface.fill((0,0,0))
	pygame.time.Clock().tick(fps)
	surface.blit(background,(0,0))
	yazı=font.render(str(ca),1,(0,0,0))
	
	if sarkı4==0:
		pygame.mixer.Sound('anamüzik.ogg').play()
	sarkı4+=1
	if sarkı4==1100:
		sarkı4=0
	if butonsol=='çek' and butonsağ=='çek' and butonaş=='çek' and butonyuk=='çek':
		durum='idle'
	if butonsağ=='baskı':
		durum='run'
	if butonsol=='baskı' :
		durum='run'
	if butonyuk=='baskı':
		durum='jump'
	if butonsağ=='çek':
		sarkı=0
	if butonsağ=='baskı':
		if sarkı==0:
			pygame.mixer.Sound('yürüme.ogg').play()
		sarkı+=1
		if sarkı==9:
			sarkı=0
		if a<1150:
			a+=hızkarakterx
		karaktery=False
		hata=7
	if butonyuk=='baskı':
		if sarkı3==0:
			pygame.mixer.Sound('zıplama.ogg').play()
		sarkı3+=1
		if sarkı3==24:
			sarkı3=0
	if butonyuk=='çek':
		sarkı3=0
	if butonsol=='çek':
		sarkı1=0
	if butonsol=='baskı':
		if sarkı1==0:
			pygame.mixer.Sound('yürüme.ogg').play()
		sarkı1+=1
		if sarkı1==9:
			sarkı1=0
		if a>0:
			a-=hızkarakterx
		karaktery=True
		hata=-7
	if durum=='idle':
		if kural<7:
			surface.blit(pygame.transform.flip(idle1,karakterx,karaktery),(b,a))
		if kural>=7:
			surface.blit(pygame.transform.flip(idle2,karakterx,karaktery),(b,a+hata))
		kural+=1
		if kural>14:
			kural=0
	if durum=='run':
		if kural1<hızrun:
			surface.blit(pygame.transform.flip(run1,karakterx,karaktery),(b,a))
		if 2*hızrun>kural1>=hızrun:
			surface.blit(pygame.transform.flip(run2,karakterx,karaktery),(b,a))
		if 3*hızrun>kural1>=2*hızrun:
			surface.blit(pygame.transform.flip(run3,karakterx,karaktery),(b,a))
		if 4*hızrun>kural1>=3*hızrun:
			surface.blit(pygame.transform.flip(run4,karakterx,karaktery),(b,a))
		if 5*hızrun>kural1>=4*hızrun:
			surface.blit(pygame.transform.flip(run3,karakterx,karaktery),(b,a))
		if 6*hızrun>kural1>=5*hızrun:
			surface.blit(pygame.transform.flip(run2,karakterx,karaktery),(b,a))
		if 7*hızrun>kural1>=6*hızrun:
			surface.blit(pygame.transform.flip(run1,karakterx,karaktery),(b,a))
		kural1+=1
		if kural1>=7*hızrun:
			kural1=0
	if butonyuk=='çek':
		if 0<kural2<24:
			durum='jump'
	if durum=='jump':
		if kural2<3:
			surface.blit(pygame.transform.flip(jump1,karakterx,karaktery),(b,a))
		if 6>kural2>=3:
			b+=zipyuk
			surface.blit(pygame.transform.flip(jump2,karakterx,karaktery),(b,a))
		if 9>kural2>=6:
			b+=zipyuk
			surface.blit(pygame.transform.flip(jump3,karakterx,karaktery),(b,a))
		if 15>kural2>=9:
			b+=0.5*zipyuk
			surface.blit(pygame.transform.flip(jump4,karakterx,karaktery),(b,a))
		if 18>kural2>=15:
			b-=zipyuk
			surface.blit(pygame.transform.flip(jump3,karakterx,karaktery),(b,a))
		if 21>kural2>=18:
			b-=zipyuk
			surface.blit(pygame.transform.flip(jump2,karakterx,karaktery),(b,a))
		if 24>kural2>=21:
			b-=zipyuk
			surface.blit(pygame.transform.flip(jump1,karakterx,karaktery),(b,a))
		kural2+=1
		if kural2>=24:
			kural2=0
	if 0<ca<1280 and not cdurum=='yok':
		ca-=5
		cdurum='runc'
	if cdurum=='runc':
		if kural3<hızrun:
			surface.blit(pygame.transform.flip(run1c,canavarx,canavary),(cb,ca))
		if 2*hızrun>kural3>=hızrun:
			surface.blit(pygame.transform.flip(run2c,canavarx,canavary),(cb,ca))
		if 3*hızrun>kural3>=2*hızrun:
			surface.blit(pygame.transform.flip(run3c,canavarx,canavary),(cb,ca))
		if 4*hızrun>kural3>=3*hızrun:
			surface.blit(pygame.transform.flip(run3c,canavarx,canavary),(cb,ca))
		if 5*hızrun>kural3>=4*hızrun:
			surface.blit(pygame.transform.flip(run2c,canavarx,canavary),(cb,ca))
		if 6*hızrun>kural3>=5*hızrun:
			surface.blit(pygame.transform.flip(run1c,canavarx,canavary),(cb,ca))
		kural3+=1
		if kural3>=6*hızrun:
			kural3=0
	if b-100<cb<b+100 and a-80<ca<a:
		cdurum='yok'
	if cdurum=='yok':
		if kural4<hızrun:
			surface.blit(pygame.transform.flip(yok1,canavarx,canavary),(cb,ca))
		if 2*hızrun>kural4>=hızrun:
			surface.blit(pygame.transform.flip(yok2,canavarx,canavary),(cb,ca))
		if 3*hızrun>kural4>=2*hızrun:
			surface.blit(pygame.transform.flip(yok3,canavarx,canavary),(cb,ca))
		if 4*hızrun>kural4>=3*hızrun:
			surface.blit(pygame.transform.flip(yok4,canavarx,canavary),(cb,ca))
		if 5*hızrun>kural4>=4*hızrun:
			surface.blit(pygame.transform.flip(yok5,canavarx,canavary),(cb,ca))
		if 6*hızrun>kural4>=5*hızrun:
			surface.blit(pygame.transform.flip(yok6,canavarx,canavary),(cb,ca))
		if 7*hızrun>kural4>=6*hızrun:
			surface.blit(pygame.transform.flip(yok7,canavarx,canavary),(cb,ca))
		kural4+=3
		if kural4>=6*hızrun:
			kural4=0
			ca=1200
			cdurum='runc'
	
	if değer==1:
		sart1=0
		butonsol='çek'
		surface.blit(butsol,(130,0))
	if değer==0 and click==1:
		sart1=1
		butonsol='baskı'
		surface.blit(butsolk,(140,0))
	else:
		değer=1
	if deger2==1:
		sart2=0
		butonsağ='çek'
		surface.blit(butsağ,(130,260))
	if deger2==0 and click==1:
		sart2=1
		butonsağ='baskı'
		surface.blit(butsağk,(140,270))
	else:
		deger2=1
	if deger3==1:
		sart3=0
		butonaş='çek'
		surface.blit(butaş,(0,130))
	if deger3==0 and click==1:
		sart3=1
		butonaş='baskı'
		surface.blit(butaşk,(0,140))
	else:
		deger3=1
	if deger4==1:
		sart4=0
		butonyuk='çek'
		surface.blit(butyuk,(260,130))
	if deger4==0 and click==1:
		sart4=1
		butonyuk='baskı'
		surface.blit(butyukk,(270,140))
	else:
		deger4=1
	if 130<mousex<260 and 0<mousey<130 and click==1:
		değer=0
	if 130<mousex<260 and 260<mousey<390 and click==1:
		deger2=0
	if 0<mousex<130 and 130<mousey<260 and click==1:
		deger3=0
	if 260<mousex<390 and 130<mousey<260 and click==1:
		deger4=0
	
	pygame.display.update()
	for event in pygame.event.get():
		if event.type == QUIT:
				pygame.quit()
		if event.type == pygame.MOUSEBUTTONDOWN:
			click=1
			pygame.mouse.get_rel()
		if event.type == pygame.MOUSEBUTTONUP:
			click=0
			pygame.mouse.get_rel()