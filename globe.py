from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
from iss_location import ISSlocation
# set up orthographic map projection with
# perspective of satellite looking down at 50N, 100W.
# use low resolution coastlines.
location = ISSlocation()
plt.ion()

for i in range(10):
    location.step()
    print(location)
    plt.clf()
    map = Basemap(projection='ortho',lat_0=location.lat,lon_0=location.long,resolution='l')
    # draw coastlines, country boundaries, fill continents.
    map.drawcoastlines(linewidth=0.25)
    map.drawcountries(linewidth=0.25)
    map.fillcontinents(color='coral',lake_color='aqua')
    # draw the edge of the map projection region (the projection limb)
    map.drawmapboundary(fill_color='aqua')
    # draw lat/lon grid lines every 30 degrees.
    map.drawmeridians(np.arange(0,360,30))
    map.drawparallels(np.arange(-90,90,30))
    # make up some data on a regular lat/lon grid.
    # nlats = 73; nlons = 145; delta = 2.*np.pi/(nlons-1)
    # lats = location.lat
    # loqns = location.long
    # wave = 0.75*(np.sin(2.*lats)**8*np.cos(4.*lons))
    # mean = 0.5*np.cos(2.*lats)*((np.sin(2.*lats))**2 + 2.)
    # # compute/ native map projection coordinates of lat/lon grid.
    # x, y = map(lons*180./np.pi, lats*180./np.pi)
    # contour data over the map.
    cs = map.plot(location.lat,location.long,'mo',markersize=12,latlon=True)
    plt.title('contour lines over filled continent background')
    plt.pause(0.05)
plt.show()