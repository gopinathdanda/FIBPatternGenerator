print 'Welcome to FEI Strata DB235 FIB Patterning software'
print '---------------------------------------------------'
print 'This software creates an array pattern.'

rows = input('Enter number of rows: ')
cols = input('Enter number of columns: ')

# Circle pattern only for now

nos = str(rows*cols)
name = 'Circle'
rin = str(0.000000)
ro = str(0.200000)
patType = str(7)
beam = str(1)   # 1=10pA
matFile = 'C:\\xP\Pattern\si.mtr'
depth = str(0.100000)
dwell = str(0.000001000) # in secs
overlap = str(50.000000)
time = str(5) # in secs
gis = str(0)
epd = str(0)
rot = str(0.000000)
ppm = str(47.157898) # Pixels per micron

text = '[Pattern_Summary]\nVersion=2.00\nPatterns='+nos+'\n'
for row in range(0,rows):
    for col in range(0,cols):
        text += '[Pattern_'+str(row+col+1)+']\n'
        text += 'Name='+name+'\n'
        text += 'InnerRadius='+rin+'\n'
        text += 'OuterRadius='+ro+'\n'
        text += 'CenterX='+rin+'\n'
        text += 'CenterY='+rin+'\n'
        text += 'Type='+patType+'\n'
        text += 'Beam='+beam+'\n'
        text += 'MaterialFile='+matFile+'\n'
        text += 'Depth='+depth+'\n'
        text += 'Dwell='+dwell+'\n'
        text += 'Overlap='+overlap+'\n'
        text += 'Time='+time+'\n'
        text += 'GIS='+gis+'\n'
        text += 'EPD='+epd+'\n'
        text += 'Rotation='+rot+'\n'
        text += 'PixelsPerMicron='+ppm+'\n'

print text