#Recipe_2b.py
import numpy as np
import matplotlib.pyplot as plt

def x_y_axis_labeling(x,y,x_lables,y_lables,figure_no):
    plt.figure(figure_no)
    plt.plot(x,y,'+r')
    plt.margins(0.2)
    plt.xticks(x,x_lables,rotation='vertical')
    plt.yticks(y,y_lables,)

def plot_heat_map(x,figure_no):
    plt.figure(figure_no)
    plt.pcolor(x)
    plt.colorbar()

if __name__ == "__main__":
    plt.close('all')
    x = np.array(range(1,6))
    y = np.array(range(100,600,100))
    x_label = ['element 1','element 2','element 3','element 4','element 5']
    y_label = ['weight 1','weight 2','weight 3','weight 4','weight 5']

    x_y_axis_labeling(x,y,x_label,y_label,1)
    x = np.random.normal(loc=0.5, scale=0.2,size=(10,10))
    plot_heat_map(x,2)

    plt.show()