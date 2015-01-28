#!/usr/bin/python

#Author: Duncan Campbell
#Written: July 9, 2013
#Yale University
#Description: Read in ascii Bolshoi Rockstar halo catalogue and save as HDF5 files.

###packages###
import numpy as np
from astropy.io import ascii
from astropy.io import fits
from astropy import table
import h5py
import custom_utilities as cu


def main():

    filepath = cu.get_data_path()+'Multidark/Bolshoi/particle_catalogues/'
    savepath = cu.get_output_path()+'processed_data/Multidark/Bolshoi/particle_catalogues/'

    catalogue = 'bolshoi_a1.0003_2e5_particles'
    
    print 'reading in:', catalogue
    filename = catalogue
    
    hdulist = fits.open(filepath+catalogue+'.fits')
    header = hdulist[1]
    
    print header.data
    
    x = np.array(header.data['POS'][:,0])
    y = np.array(header.data['POS'][:,1])
    z = np.array(header.data['POS'][:,2])
    
    data = np.recarray((len(x),), formats=['f4','f4','f4'], names=['x','y','z'])
    
    data['x']=x
    data['y']=y
    data['z']=z
    
    filename = catalogue
    f = h5py.File(savepath+filename+'.hdf5', 'w')
    dset = f.create_dataset(catalogue, data=data)
    f.close()
    
    filename = catalogue
    data_table = table.table.Table(data=data)
    ascii.write(data_table, savepath+filename+'.dat')
    print data_table
    

if __name__ == '__main__':
  main()