import os, sys
import numpy as np
from netCDF4 import Dataset
from matplotlib import pyplot as plt
from mpl_toolkits.basemap import Basemap # Import the Basemap toolkit
from remap import remap


path = r"C:\Projects\RD\OPIR_GOES\GOES\OR_ABI-L1b-RadC-M3C16_G16_s20180941227206_e20180941229591_c20180941230032.nc"
    
# Open the file using the NetCDF4 library
nc = Dataset(path)
 
# Extract the Brightness Temperature values from the NetCDF
data = nc.variables['Rad'][:]
 
# Show data
plt.imshow(data, cmap='Greys')
plt.show()

for i,k in enumerate(nc.variables.keys()):
    
    if i <5:
        print(k)
    else:
        print("{}: {}".format(k, nc.variables[k][:]))

 

 
# Calculate the image extent required for the reprojection
H = nc.variables['goes_imager_projection'].perspective_point_height
x1 = nc.variables['x_image_bounds'][0] * H
x2 = nc.variables['x_image_bounds'][1] * H
y1 = nc.variables['y_image_bounds'][1] * H
y2 = nc.variables['y_image_bounds'][0] * H 
 
# Print the results
print("x1 = " + str(x1))
print("y1 = " + str(y1))
print("x2 = " + str(x2))
print("y2 = " + str(y2))


# Call the reprojection function
grid = remap(path, extent, resolution, x1, y1, x2, y2)


''' this only works if the data is full disk, not CONUS
# Create the basemap reference for the Satellite Projection
bmap = Basemap(projection='geos', lon_0=-89.5, lat_0=0.0, satellite_height=35786023.0, ellps='GRS80')
 
# Plot GOES-16 Channel using 170 and 378 as the temperature thresholds
bmap.imshow(data, origin='upper', vmin=170, vmax=378, cmap='Greys')
 
# Draw the coastlines, countries, parallels and meridians
bmap.drawcoastlines(linewidth=0.3, linestyle='solid', color='black')
bmap.drawcountries(linewidth=0.3, linestyle='solid', color='black')
bmap.drawparallels(np.arange(-90.0, 90.0, 10.0), linewidth=0.1, color='white')
bmap.drawmeridians(np.arange(0.0, 360.0, 10.0), linewidth=0.1, color='white')
 
# Insert the legend
bmap.colorbar(location='bottom', label='Brightness Temperature [K]')
 

# Export result
DPI = 300
plt.savefig('C:\VLAB\GOES-16_Ch13.png', dpi=DPI, bbox_inches='tight', pad_inches=0)
 
# Show the plot
plt.show()
'''