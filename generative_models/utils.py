from IPython.display import display
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.mixture import GaussianMixture
from sklearn import metrics
import seaborn as sns


def load_iris_dataset():
    return sns.load_dataset("iris")

def setup_plotting():
    plt.rcParams["figure.figsize"] = (8,4)

def display_first_n_rows(dataframe, n=3):
    display(dataframe.head(n))

def plot_scatter(dataframe, x, y):
    return sns.scatterplot(data=dataframe, x=x, y=y)

def plot_gmm_clusters(dataframe, x_feature, y_feature, gmm_labels, gmm_means, species_column='species', cluster_centers_color='black', cluster_centers_size=100):
    plot_gmm = sns.scatterplot(data=dataframe, x=x_feature, y=y_feature, style=gmm_labels, hue=dataframe[species_column])
    plot_gmm = sns.scatterplot(x=gmm_means[:, 0], y=gmm_means[:, 1], ax=plot_gmm, color=cluster_centers_color,
                               style=list(range(len(gmm_means))), s=cluster_centers_size, legend=False)
    return plot_gmm

def plot_new_data(new_data, x_label, y_label):
    plot = sns.scatterplot(x=new_data[:,0], y=new_data[:,1])
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    return plot