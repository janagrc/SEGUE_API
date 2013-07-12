import astropy.units as u
import math

def lbdtoXYZ(L,B,heliod)
	
	l=L*u.deg
	b=B*u.deg
	d = heliod*u.kpc
		
	assert hasattr(l,'unit')
	assert hasattr(b,'unit')

	suntocenter = 8.3*u.kpc

	x = d*sin(0.5-math.pi*b.rad)*math.cos(l.rad)-suntocenter
	y = d*sin(0.5-math.pi*b.rad)*math.sin(l.rad)
	z = d*cos(0.5-math.pi*b.rad)
	return x,y,z