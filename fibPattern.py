print 'Welcome to FEI Strata DB235 FIB Patterning software'
print '---------------------------------------------------'
print 'This software creates an array pattern.'

rows = input('Enter number of rows: ')
cols = input('Enter number of columns: ')

# Circle pattern only for now

nos = rows*cols
name = 'Circle'
rin = 0.000000
ro = 0.200000
patType = 7
beam = 1   # 1=10pA
matFile = 'C:\\xP\Pattern\si.mtr'
depth = 0.100000
dwell = 0.000001000 # in secs
overlap = 50.000000
time = 5 # in secs
gis = 0
epd = 0
rot = 0.000000
ppm = 47.157898 # Pixels per micron

dim = 100   # Dimensions of scan window

text = '[Pattern_Summary]\nVersion=2.00\nPatterns='+str(nos)+'\n'
for row in range(0,rows):
    for col in range(0,cols):
        text += '[Pattern_'+str(row+col+1)+']\n'
        text += 'Name='+name+'\n'
        text += 'InnerRadius='+str(rin)+'\n'
        text += 'OuterRadius='+str(ro)+'\n'
        text += 'CenterX='+str(rin)+'\n'
        text += 'CenterY='+str(rin)+'\n'
        text += 'Type='+str(patType)+'\n'
        text += 'Beam='+str(beam)+'\n'
        text += 'MaterialFile='+matFile+'\n'
        text += 'Depth='+str(depth)+'\n'
        text += 'Dwell='+str(dwell)+'\n'
        text += 'Overlap='+str(overlap)+'\n'
        text += 'Time='+str(time)+'\n'
        text += 'GIS='+str(gis)+'\n'
        text += 'EPD='+str(epd)+'\n'
        text += 'Rotation='+str(rot)+'\n'
        text += 'PixelsPerMicron='+str(ppm)+'\n'

print text