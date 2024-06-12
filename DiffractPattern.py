import numpy as np
from matplotlib import pyplot as plt
import streamlit as st

#----- LAYOUT ------#
st.title("Diffraction Slit Experiment")
st.text("This app visualize the interference pattern of waves when propagates through \nnarrow slit(s)")
wavecol, intenscol = st.columns([100, 88])
sliders = st.container()

#----- CALCULATION -----#
# Window Size
xmin, xmax = 0, 20
ymin, ymax = -10, 10
xpoints, ypoints = 200, 200                 # Plot resolution

# Coordinate System
x = np.linspace(xmin, xmax, xpoints)
y = np.linspace(ymin, ymax, ypoints)
X, Y, = np.meshgrid(x, y)
points = np.concatenate([X.reshape(-1, 1), Y.reshape(-1, 1)], axis = 1)

# System Parameter
rangedisable = False
singleslit = st.toggle("Single Slit")
if singleslit:
    range = 0
    width_min = 1.0
    width_max = 3.0
    rangedisable = True
else:
    range = range
    width_min = 1.0
    width_max = 3.0
    range = sliders.slider("Distance Between Slit", min_value=1.0, max_value=5.0, step=0.5, disabled=rangedisable)
wavel = sliders.slider("Wavelength", min_value=0.4, max_value=0.7, step=0.05)       # Wavelength
width = sliders.slider("Slit Width", width_min, width_max, step=0.2)               # Slit width
s_pos1 = 0 + range/2       # Slit 1 position (on Y axis)
s_pos2 = 0 - range/2       # Slit 2 position (on Y axis)

# Wave Displacement on a Point

# Wave Source
source_res = 0.1              # Distance between wave source points
source_points1 = np.arange(s_pos1-(width/2), s_pos1+(width/2)+source_res, source_res).tolist()
source_points2 = np.arange(s_pos2-(width/2), s_pos2+(width/2)+source_res, source_res).tolist()
source_points = source_points1 + source_points2
    # Use range instead of linspace to avoid resolution loss when slit width increasing
    # But doesn't represent actual slit width if resolution is too low

# Wave Displacement on every point
Z = np.zeros(xpoints*ypoints)
for source in source_points:
    pos = points - np.array([0, source])
    # Source points is on Y axis, so only calculate Y axis range as pos

    # Wave Displacement on a Point
    wd = np.sin(2*np.pi/wavel * (pos[:,0]**2 + pos[:,1]**2)**0.5)
    Z = Z + wd               # Sum of every source points contribution
I = Z**2                    # Intensity of wave on every points

# Intensity on X maximum (Wave intensity on screen)
Y = np.linspace(ymin, ymax, ypoints)
Ixmax = (((np.sin(np.pi*width*Y/(wavel*(xmax**2+Y**2)**0.5)))/(np.pi*width*Y/(wavel*(xmax**2+Y**2)**0.5)))**2
         * (np.cos(np.pi*range*Y/(wavel*(xmax**2+Y**2)**0.5))**2))

#----- PLOTTING -----#
waveplot = plt.figure(figsize=(5, 5))
plt.xlim(xmin, xmax)
plt.ylim(ymin, ymax)
plt.xlabel ("x (mm)")
plt.ylabel ("y (mm)")
plt.scatter(points[:, 0], points[:, 1], c = Z)

colorlist = { 0.4 :'#FF009F'   #397.406nm
            , 0.45:'#003FFF'   #448.795nm
            , 0.5 :'#00FF9F'   #498.961nm
            , 0.55:'#9FFF00'   #548.938nm
            , 0.6 :'#FFBF00'   #599.855nm
            , 0.65:'#FF1F00'   #640.427nm
            , 0.7 :'#FF0000'   #700.000nm
            }

intensplot, (ax1, ax2) = plt.subplots(1, 2, figsize=(5, 5),
                                      gridspec_kw={'width_ratios':[1, 20]})
plt.ylabel ("y (mm)")
plt.xlabel ("Relative intensity")
ax2.plot(Ixmax, Y, lw = 2, color = 'r')
barlength = np.zeros(ypoints)
ax1.scatter(barlength, Y, color=colorlist[wavel], alpha=Ixmax)
ax1.axis('off')

#----- LAYOUT -----#
wavecol.markdown("### Wave Interference")
wavecol.pyplot(waveplot)
intenscol.markdown("### Intensity Plot")
# intenscol.markdown(colorlist[wavel])
intenscol.pyplot(intensplot)

