
# coding: utf-8

# Assignement2" FIND ALL THE BLACK HOLES "

# In[ ]:


import pynbody 
import matplotlib.pylab as plt
plt.switch_backend("agg") 

   # loading the snapshot
s =pynbody.load('/mnt/cptmarvel/cptmarvel.cosmo25cmb.4096g5HbwK1BH.004096/cptmarvel.cosmo25cmb.4096g5HbwK1BH.004096')

   # convert the units 
s.physical_units()

  # the halo that I need is h[5]
h = s.halos()

def findBH(s):
    BHfilter = pynbody.filt.LowPass('tform',0.0)
    BH = s.stars[BHfilter]
    return BH
BH = findBH(s)
print BH

def findBHhalos(s):
    BH = findBH(s)
    BHhalos = BH['amiga.grp']
    return BHhalos
halos = findBHhalos(s)
print halos

for halo in halos:
    
    #the position of black hole
   BHposition=BH['pos']
   print BHposition

   #putting the x-values into a column
   BHx= BHposition[:,0]
   print BHx

   #putting the y-values into a column
   BHy= BHposition[:,1]
   print BHy

   #putting the z-values into a column
   BHz= BHposition[:,2]
   print BHz

   #this is the distance formula
   distance =((BHx**2)+(BHy**2)+(BHz**2))**(.5)
   print distance

