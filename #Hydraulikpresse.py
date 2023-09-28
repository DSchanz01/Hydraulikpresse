#Hydraulikpresse
not_aus = False
riegel = False
sicherheitsbereich = False
zylinder_start_position = True
zylinder_endposition = False
schalter1 = False
schalter2 = False
hupe1 = False
hupe2 = False
lichtschranke_start = True # also unterbrochen
lichtschranke_end = False # also nicht unterbrochen


if lichtschranke_start:
	zylinder_start_position = True
	zylinder_endposition = False
elif lichtschranke_start and lichtschranke_end == True:
	zylinder_start_position = False
	zylinder_endposition = False
else:
	zylinder_endposition == True

while schalter1 and schalter2:
	if not_aus == False and sicherheitsbereich == False and zylinder_start_position == True:
		zylinder_start_position = False
		zylinder_endposition = True

if zylinder_endposition == True:
	5 sec warten
	zylinder_endposition = False
	zylinder_startposition = True
	
if not_aus == True:
	zylinder_start_position = True
	riegel = True
	hupe1 = True Böhp 3x

if not_aus == False:
	hupe = False
	riegel = False

if sicherheitsbereich == True:
	zylinder_start_position = True
	hupe2 = True wiuh 3x

	


	


