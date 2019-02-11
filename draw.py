from display import *

def draw_line( x0, y0, x1, y1, screen, color ):
    if x0 > x1:
        x0, x1 = x1, x0
        y0, y1 = y1, y0

    x = x0
    y = y0
    A = y1 - y0

    if x0 == x1:
        x1 += 1

    B = x0 - x1    
    slope = (y1 - y0) / (x1 - x0)
    
    if slope >= 1:
        d = A + 2*B
        while (y <= y1):
            plot(screen, color, x, y)
            if d < 0:
                x += 1
                d += 2*A
            y += 1
            d += 2*B
                
    elif slope >= 0:
        d = 2*A + B
        while (x <= x1):
            plot(screen, color, x, y)
            if d > 0:
                y += 1
                d += 2*B
            x += 1
            d += 2*A

    elif slope >= -1:
        d = 2*A - B
        while (x <= x1):
            plot(screen, color, x, y)
            if d < 0:
                y -= 1
                d -= 2*B
            x += 1
            d += 2*A        

    elif slope < -1:
        d = A - 2*B
        while (y >= y1):
            plot(screen, color, x, y)
            if d > 0:
                x += 1
                d += 2*A
            y -= 1
            d -= 2*B
        
pass
