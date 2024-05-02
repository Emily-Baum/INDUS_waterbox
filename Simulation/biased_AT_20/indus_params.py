import MDAnalysis as mda
import matplotlib.pyplot as plt
import statistics as s
import numpy as np

def count_waters_spherical(radius=6,center=[20,20,20],equilibration=200):
   
    """

    Parameters
    ----------
    radius : float, opt
    
        The radius of the spherical control volume in angstroms. The default is 6.

    center : 1x3 list of float, opt

        The centerpoint coordinates of the control volume in angstroms. The default is [20, 20, 20].

    equilibration : int, opt

        The number of timesteps to skip to account for system equilibration. The default is 200.

    Returns
    -------

    ts.txt : file

        A file containing a timeseries of the number of water molecules in the control volume.
        This is intended to be used with WHAM.

    nbox : list of int

        The number of water molecules in the control volume at each timestep.

    """

    # select water O atoms
    u = mda.Universe('parm7','03_Prod.nc',topology_format='PARM7')
    os = u.select_atoms('type OW')
    
    nbox = []
    # count at all times after equilibration
    for i in range(len(u.trajectory[equilibration:])):
        # update timestep
        u.trajectory[i+len(u.trajectory[:equilibration])]
        # get atom coords
        pos = os.positions
        count = 0
        # calculate whether atom is in control volume
        for xyz in pos:
            r = ((xyz[0]-center[0])**2 + (xyz[1]-center[1])**2 + (xyz[2]-center[2])**2)**.5
            if r <= radius:
                count += 1
        # store count at each timestep
        nbox.append(count)
        # write the count to ts.txt for WHAM
        with open('ts2.txt','a') as tsfile:
            tsfile.write('{:.1f} {:.1f}\n'.format(i,count))
    # return the counts at each timestep
    return nbox

nbox = count_waters_spherical()

# make a list of N and log(P(N))
nbox = sorted(nbox)
dct = {x:nbox.count(x) for x in nbox}
y = np.array([i for i in dct.values()])
y = np.log(y/sum(y))

# plot log(P(N)) vs N, save the figure
plt.plot(dct.keys(),y,'--o')
plt.xlabel('N')
plt.ylabel('log P(N)')
plt.savefig('prob_dist.png')

