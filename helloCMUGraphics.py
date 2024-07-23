# helloCMUGraphics.py VERSION 1.0

from cmu_graphics import *

def redrawAll(app):
    andrewID = 'pvirtue'
    name = 'Pat Virtue'
    margin = 60
    drawRect(margin, margin, app.width-2*margin, app.height-2*margin, fill='hotpink')
    drawLabel(f'Hello, my name is {name}!', app.width/2, app.height/2)
    drawLabel(f'My Andrew ID is {andrewID}', app.width/2, app.height/2+20)
    drawOval(margin, margin, app.width-2*margin, app.height-2*margin, fill='skyblue')

def main():
    runApp()

if __name__ == '__main__':
    main()  

