import numpy as np
import matplotlib.pyplot as plt

def main():
    
    x = np.linspace(0,2*np.pi,1000)
    y = np.sin(x)
    
    from astropy.table import Table
    from astropy.io import ascii
    from astropy.io import fits
    
    mytable = Table()
    mytable['x'] = x
    mytable['y'] = y
    
    print(mytable)
    
    #data = Table([x,y],names=['x', 'y'])
    #ascii.write(data, 'table.txt', format='commented_header')
    #data_in = ascii.read('table.txt')
    
if __name__=="__main__":
    main()