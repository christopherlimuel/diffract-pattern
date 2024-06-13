# Wave Diffraction Visualization
https://diffract-pattern.streamlit.app/
## Overview
This program visualizes the interference pattern as they pass through a narrow slit, and the wave interference plot at the end (x maximum). The adjustable parameters include the **number of slits** (double or single), the **distance between slits**, the **slit width**, and the **wavelength** (all units in mm).

## Calculation
Calculations are performed using the assumption of **Fraunhofer diffraction**, where the distance from the slit to the screen is much larger than the slit width, and the wave source is monochromatic with a plane wavefront. According to **Huygens' principle**, each point on the wavefront can be considered a source of new waves. Therefore, each point on the slit acts as a source of new waves.

Source points of wave are aranged within the slit with certain distance (smaller the distance, higher the accuracy). Wave from all the sources for all the coordinate points are calculated and added, resulting the interference pattern of wave from all the sources. 

$Z(x, y) = \sin{\frac{2\pi}{\lambda}\sqrt{x^{2}+y^{2}}}$

For the wave intensity plot on the screen, following equation were used.
![image](https://github.com/christopherlimuel/diffract-pattern/assets/130728527/5d1e38bd-bb4e-470e-915c-bc9d14db567b)

with

$\theta = \frac{y}{\sqrt{x^2 + y^2}}$

$a =$ width of the slit

$\lambda =$ wavelength

$d =$ range between slits ($=0$ if single slit)

https://web.mit.edu/8.02t/www/802TEAL3D/visualizations/coursenotes/modules/guide14.pdf
