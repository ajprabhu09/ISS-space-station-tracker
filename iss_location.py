from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
plt.ion()
import random
import requests
import json
class ISSlocation:
    '''
    A library to get the location of the International Space Station
    '''
    def __init__(self,url='http://api.open-notify.org/iss-now.json'):
        '''
        pass in the url to get the json response

        default:'http://api.open-notify.org/iss-now.json
        '''
        self.url = url
        self.lat = None
        self.long = None 
        self.timestamp = None
        self.json_string = None
        self.dictionary = None
        self.prev_lats = []
        self.prev_longs = []
        
    def step(self):
        '''
        class step everytime you want to update the location by getting a new response
        '''
        self.dictionary = requests.get(self.url).json()
        if self.dictionary['message'] == 'success':
            self.lat = float(self.dictionary['iss_position']['latitude'])
            self.long = float(self.dictionary['iss_position']['longitude'])
            self.timestamp = self.dictionary['timestamp']
            self.prev_lats.append(self.lat)
            self.prev_longs.append(self.long)
        else:
            '''
            for python2 
            '''
            raise BaseException("Unable to contact ISS server")
            
            '''
            for python3
            raise ConnectionError("Unable to contact ISS server")

            '''

    def __str__(self):
        '''
        returns current Lat and Lon
        '''
        return str(self.__class__.__name__)+"("+str(self.lat)+","+str(self.long)+")"

    def plot_on_globle(self,iterations=10):
        '''
        pass in number of iterations to plot on map number of times
        default iterations=10
        '''
        for i in range(iterations):
            self.step()
            print(self)
            plt.clf()
            map = Basemap(projection='ortho',lat_0=self.lat,lon_0=self.long,resolution='l')
            
            map.drawcoastlines(linewidth=0.01)
            map.drawcountries(linewidth=0.01)
            map.fillcontinents(color='coral',lake_color='aqua')
           
            map.drawmapboundary(fill_color='aqua')

            map.drawmeridians(np.arange(0,360,30))
            map.drawparallels(np.arange(-90,90,30))
            cs = map.plot(self.prev_lats,self.prev_longs,'mo',markersize=12,latlon=True)
            plt.title('contour lines over filled continent background')
            plt.pause(0.05)
        

if __name__=='__main__':
    lo = ISSlocation()
    lo.plot_on_globle()
    