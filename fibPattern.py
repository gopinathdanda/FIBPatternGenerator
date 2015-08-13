from pyx import *
import datetime
print 'Welcome to FEI Strata DB235 FIB Patterning software'
print '---------------------------------------------------'
print 'This software creates an array pattern.'
print '---------------------------------------------------'

rows = input('Enter number of rows: ')
cols = input('Enter number of columns: ')


nos = rows*cols
name = 'Circle'         # Circle pattern only (for now)
rin = 0.000000          # in um
ro = 0.200000           # in um
patType = 7
beam = 1                # 1=10pA
matFile = 'C:\\xP\Pattern\si.mtr'
depth = 0.100000
dwell = 0.000001000     # in secs
overlap = 50.000000
time = 7.000000         # in secs
gis = 0
epd = 0
rot = 0.000000
ppm = 47.157898         # Pixels per micron

# For magnification: 3.5kX

dimX = 85               # Dimensions of scan window in x-dirn in um
dimY = 75               # Dimensions of scan window in y-dirn in um
borderX = 5.0             # Distance of array from x border in um
borderY = 5.0             # Distance of array from y border in um
stepX = (dimX-2*borderX)/(cols-1)   # Distance between two columns in um
stepY = (dimY-2*borderY)/(rows-1)   # Distance between two rows in um
centerX = 0             # Center of rows
centerY = 0             # Center of columns

c = canvas.canvas()
c.stroke(path.rect(-dimX/2.0,-dimY/2.0,dimX,dimY))  # scan window
c.stroke(path.rect(-dimX/2.0+borderX,-dimY/2.0+borderY,dimX-borderX*2,dimY-borderY*2))  # border
i = 0
text = '[Pattern_Summary]\nVersion=2.00\nPatterns='+str(nos)
for row in range(0,rows):
    maxY = -(rows-1)*stepY/2.0
    y = centerY + maxY + row*stepY
    for col in range(0,cols):
        i += 1
        maxX = -(cols-1)*stepX/2.0
        x = centerX + maxX + col*stepX
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
        c.fill(path.circle(x, y, ro), [color.rgb(0,0,0)])
        c.fill(path.circle(x, y, rin), [color.rgb(1,1,1)])
        #print x,',',y

print '---------------------------------------------------'
print 'Total time required = '+str(datetime.timedelta(seconds=time*nos))
c.writeEPSfile("path")
c.writePDFfile("path")
file = open('output.pat', 'w')
file.write(text)
file.close()