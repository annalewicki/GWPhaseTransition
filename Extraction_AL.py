import numpy as np
import matplotlib.pyplot as plt

from TransitionListener.observability import GW_analysis_one_point

# Create an instance of GW_analysis_one_point
gw_analysis = GW_analysis_one_point()

spectrum_plot = gw_analysis.plot_spectrum()
#h2omega = gw_analysis.h2Omega_0()
#h2omega_sum = gw_analysis.h2Omega_0_sum()


# Now you can use the plot_spectrum method
'''
Aditi: this is where im having trouble. Now that I get the plot directly from observability I'm trying to extract the data so that we can re-plot it 
and compare it with our digitized constraints. Once we have this raw data we can use your bifurcation code to see if the black line intersects with 
the constraints. So the next steps that I was thinking of doing are to get the data from the plot (without digitizing from a pdf/image because that 
incorporates a lot of error) and finding a way to change the variables directly form here, and then add your code to this file to then see which lines 
with certain values intersect the digitized constraints. 
'''

xdata, ydata = spectrum_plot()  #in observability, plot_spectrum: i set xdata = frequencies_Hz and ydata = self.h2Omega(self,frequencies_Hz))

print("X data points for the plot are: ", xdata)
print("Y data points for the plot are: ", ydata) #have to import h2Omega_0 function before i can call the y_data, will probs have to use h2Omega_0_sum too.



'''
vev_values = np.linspace(0, 1e4, num=10)  # Example range for vev
xi_values = np.linspace(0, 2, num=10)  # Example range for xi
def my_point_comparison(vev_values, xi_values):
    # Perform calculations and generate the plot
# Define the range of parameter values
    #vev_values = np.linspace(0, 1e4, num=10)  # Example range for vev
    #xi_values = np.linspace(0, 2, num=10)  # Example range for xi
# Iterate over the parameter values
    #for vev in vev_values:
        #for xi in xi_values:
            # Call my_point_comparison() with the current parameter values
            ####plot = My_point_comparison(vev, xi)

            # Perform operations based on the results
            # Extract the black line data
            #points = scanner.GW_params(vev,xi) # Modify this line based on how the black line is obtained in your code
            #points = scanner.grid_analysis(self)

my_point_comparison(vev_values,xi_values)
            # Return the black line data
            ####return black_line

            # Adjust parameter values based on the comparison results

            # Continue the loop until the desired condition is met

            # Store successful parameter values

x_data = np.array(
[2.44269061e-11, 3.20009389e-11, 4.19234465e-11, 5.49226187e-11,
 7.19524348e-11, 9.42626733e-11, 1.23490631e-10, 1.61781280e-10,
 2.11944683e-10, 2.77662215e-10, 3.63756734e-10, 4.76546517e-10,
 6.24308946e-10, 8.17887962e-10, 1.07148988e-09, 1.40372596e-09,
 1.83897824e-09, 2.40918887e-09, 3.15620429e-09, 4.13484623e-09,
 5.41693497e-09, 7.09656001e-09, 9.29698516e-09, 1.21796945e-08,
 1.59562434e-08, 2.09037841e-08, 2.73854051e-08, 3.58767775e-08,
 4.70010635e-08, 6.15746488e-08, 8.06670548e-08, 1.05679429e-07,
 1.38447372e-07, 1.81375647e-07, 2.37614661e-07, 3.11291664e-07,
 4.07813641e-07, 5.34264117e-07, 6.99923000e-07, 9.16947610e-07,
 1.20126488e-06, 1.57374020e-06, 2.06170867e-06, 2.70098116e-06,
 3.53847240e-06, 4.63564394e-06, 6.07301464e-06, 7.95606983e-06,
 1.04230026e-05, 1.36548553e-05, 1.78888062e-05, 2.34355752e-05,
 3.07022268e-05, 4.02220438e-05, 5.26936633e-05, 6.90323487e-05,
 9.04371584e-05, 1.18478942e-04, 1.55215620e-04, 2.03343213e-04,
 2.66393694e-04, 3.48994191e-04, 4.57206563e-04, 5.98972266e-04,
 7.84695156e-04, 1.02800501e-03, 1.34675776e-03, 1.76434595e-03,
 2.31141540e-03, 3.02811428e-03, 3.96703945e-03, 5.19709646e-03,
 6.80855633e-03, 8.91968039e-03, 1.16853991e-02, 1.53086823e-02,
 2.00554341e-02, 2.62740078e-02, 3.44207701e-02, 4.50935930e-02,
 5.90757303e-02, 7.73932985e-02, 1.01390582e-01, 1.32828685e-01,
 1.74014778e-01, 2.27971412e-01, 2.98658340e-01, 3.91263112e-01,
 5.12581777e-01, 6.71517632e-01, 8.79734611e-01, 1.15251327e+00,
 1.50987222e+00, 1.97803719e+00, 2.59136573e+00, 3.39486859e+00,
 4.44751300e+00, 5.82655009e+00, 7.63318419e+00, 1.00000000e+01])

z_data = np.array(
[1.00000000e+00, 1.14529847e+00, 1.31157292e+00, 1.50188052e+00,
 1.71972381e+00, 1.96911602e+00, 2.25465715e+00, 2.58162021e+00,
 2.95605165e+00, 3.38488556e+00, 3.87607597e+00, 4.43875025e+00,
 5.08338325e+00, 5.82200354e+00, 6.66842067e+00, 7.63850322e+00,
 8.75048745e+00, 1.00253417e+01, 1.14871890e+01, 1.31637946e+01,
 1.50871319e+01, 1.72940473e+01, 1.98271039e+01, 2.27398409e+01,
 2.60934233e+01, 2.99567942e+01, 3.44104813e+01, 3.95487228e+01,
 4.54820223e+01, 5.23402219e+01, 6.02762292e+01, 6.94704932e+01,
 8.01364285e+01, 9.25269756e+01, 1.06942527e+02, 1.23740532e+02,
 1.43347052e+02, 1.66270754e+02, 1.93119762e+02, 2.24621913e+02,
 2.61649166e+02, 3.05246842e+02, 3.56668710e+02, 4.17419006e+02,
 4.89302668e+02, 5.74485544e+02, 6.75566150e+02, 7.95661610e+02,
 9.38510348e+02, 1.10859469e+03, 1.31128781e+03, 1.55302918e+03,
 1.84153446e+03, 2.18604678e+03, 2.59763829e+03, 3.08956957e+03,
 3.67771980e+03, 4.38110814e+03, 5.22250754e+03, 6.22917889e+03,
 7.43376872e+03, 8.87536274e+03, 1.06007406e+04, 1.26659089e+04,
 1.51379144e+04, 1.80970024e+04, 2.16392252e+04, 2.58795498e+04,
 3.09555657e+04, 3.70319158e+04, 4.43055889e+04, 5.30122361e+04,
 6.34336804e+04, 7.59068435e+04, 9.08343218e+04, 1.08696913e+05,
 1.30068339e+05, 1.55632517e+05, 1.86203599e+05, 2.22749062e+05,
 2.66415970e+05, 3.18560210e+05, 3.80778215e+05, 4.54940181e+05,
 5.43222592e+05, 6.48137057e+05, 7.72550836e+05, 9.19694392e+05,
 1.09314730e+06, 1.29679727e+06, 1.53477418e+06, 1.81137225e+06,
 2.13099562e+06, 2.49821291e+06, 2.91797339e+06, 3.39596752e+06,
 3.93913823e+06, 4.55620557e+06, 5.25813064e+06, 6.05795314e+06])

plt.plot(x_data, z_data)
plt.show()

'''
