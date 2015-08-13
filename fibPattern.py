print 'Welcome to FEI Strata DB235 FIB Patterning software'
print '---------------------------------------------------'
print 'This software creates an array pattern.'

rows = input('Enter number of rows: ')
cols = input('Enter number of columns: ')

# Circle pattern only for now

nos = rows*cols
name = 'Circle'
rin = 0.000000          # in um
ro = 0.200000           # in um
patType = 7
beam = 1                # 1=10pA
matFile = 'C:\\xP\Pattern\si.mtr'
depth = 0.100000
dwell = 0.000001000     # in secs
overlap = 50.000000
time = 5                # in secs
gis = 0
epd = 0
rot = 0.000000
ppm = 47.157898         # Pixels per micron

dim = 100               # Dimensions of scan window in um
stepX = 3               # Distance between two columns in um
stepY = 3               # Distance between two rows in um
centerX = 0             # Center of rows
centerY = 0             # Center of columns

i = 0
text = '[Pattern_Summary]\nVersion=2.00\nPatterns='+str(nos)
for row in range(0,rows):
    maxX = -(rows-1)*stepX/2.0
    x = centerX + maxX + row*stepX
    for col in range(0,cols):
        i += 1
        maxY = -(cols-1)*stepY/2.0
        y = centerY + maxY + col*stepY
        text += '\n[Pattern_'+str(i)+']\n'
        text += 'Name='+name+'\n'
        text += 'InnerRadius='+str('{0:.6f}'.format(rin))+'\n'
        text += 'OuterRadius='+str('{0:.6f}'.format(ro))+'\n'
        text += 'CenterX='+str('{0:.6f}'.format(x))+'\n'
        text += 'CenterY='+str('{0:.6f}'.format(y))+'\n'
        text += 'Type='+str(patType)+'\n'
        text += 'Beam='+str(beam)+'\n'
        text += 'MaterialFile='+matFile+'\n'
        text += 'Depth='+str('{0:.6f}'.format(depth))+'\n'
        text += 'Dwell='+str('{0:.9f}'.format(dwell))+'\n'
        text += 'Overlap='+str('{0:.6f}'.format(overlap))+'\n'
        text += 'Time='+str('{0:.6f}'.format(time))+'\n'
        text += 'GIS='+str(gis)+'\n'
        text += 'EPD='+str(epd)+'\n'
        text += 'Rotation='+str('{0:.6f}'.format(rot))+'\n'
        text += 'PixelsPerMicron='+str('{0:.6f}'.format(ppm))
        #print x,',',y

file = open('test.pat', 'w')
file.write(text)
file.close()