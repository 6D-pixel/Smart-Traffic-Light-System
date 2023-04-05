from pyfirmata import Arduino, util
import time
from model import get_total_time
# Board configuration
board = Arduino('COM9')  # Change this to match your board's serial port
it = util.Iterator(board)
it.start()
board.analog[0].enable_reporting()  # Enable reporting for digital pins

# Pin configuration
red1 = board.get_pin('d:13:o')
yellow1 = board.get_pin('d:12:o')
green1 = board.get_pin('d:11:o')
red2 = board.get_pin('d:10:o')
yellow2 = board.get_pin('d:9:o')
green2 = board.get_pin('d:8:o')
red3 = board.get_pin('d:7:o')
yellow3 = board.get_pin('d:6:o')
green3 = board.get_pin('d:5:o')
red4 = board.get_pin('d:4:o')
yellow4 = board.get_pin('d:3:o')
green4 = board.get_pin('d:2:o')

def direction(a, b, c, d, e, f, g, h, i, j, k, l,img_path):
    a.write(0)
    b.write(0)
    c.write(1)
    d.write(1)
    e.write(0)
    f.write(0)
    g.write(1)
    h.write(0)
    i.write(0)
    j.write(1)
    k.write(0)
    l.write(0)
    total_time = get_total_time(img_path)
    time.sleep(total_time) #use total time here
    c.write(0)
    b.write(1)
    time.sleep(3)

# Main loop
while True:
    direction(red1, yellow1, green1, red2, yellow2, green2, red3, yellow3, green3, red4, yellow4, green4,'image/frame1.jpg')#pass time here in the funtion
    direction(red2, yellow2, green2, red1, yellow1, green1, red3, yellow3, green3, red4, yellow4, green4,'image/frame2.jpg')
    direction(red3, yellow3, green3, red1, yellow1, green1, red2, yellow2, green2, red4, yellow4, green4,'image/frame3.jpg')
    direction(red4, yellow4, green4, red1, yellow1, green1, red2, yellow2, green2, red3, yellow3, green3,'image/frame4.jpg')
