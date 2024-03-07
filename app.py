import matplotlib.pyplot as plt
import numpy as np
from shiny.express import ui, input, render
import seaborn as sn


@render.plot(alt="A histogram")
def draw_histogram():
    np.random.seed(19680801)
    x = 100 + 15 * np.random.randn(437)
    plt.hist(x, input.n(), density=True)

# Set page options for PyShiny App
ui.page_opts(title="PyShiny App with Plot", fillable=True)

# Create a sidebar with an input slider for the number of bins
with ui.sidebar():
    ui.input_slider("selected_number_of_bins", "Number of Bins", 0, 100, 20)

# Define a plot function for rendering a histogram
@render.plot(alt="A histogram")
def histogram():
    # Set a random seed for reproducibility
    np.random.seed(3)

 # Generate random data for the histogram
    x = 100 + 15 * np.random.randn(437)

    # Plot the histogram using the specified number of bins and change the color to purple
    plt.hist(x, input.selected_number_of_bins(), density=True, color='blue')


# Define a function to generate a heatmap
from shiny.express import ui, input, render
from palmerpenguins import load_penguins
import seaborn as sns

def server(input,output,session):
    @output
    @render.plot
    def myplot(): 
        penguins=load_penguins()

import seaborn as sns
from palmerpenguins import load_penguins
from shiny import render
from shiny.express import input, ui

penguins = load_penguins()

ui.input_slider("n", "Number of bins", 1, 100, 20)

@render.plot(alt="A Seaborn histogram on penguin body mass in grams.")  
def sub_plot():  
    ax = sns.histplot(data=penguins, x="body_mass_g", bins=input.n())  
    ax.set_title("Palmer Penguins")
    ax.set_xlabel("Mass (g)")
    ax.set_ylabel("Count")
    return ax  

