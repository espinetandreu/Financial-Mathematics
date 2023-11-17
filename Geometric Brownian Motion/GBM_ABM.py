"""
Plot paths for the Geometric Brownian Motion S(t) and 
Arithmetic Browninan motion X(t)
@author: espinet
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from scipy.stats import norm, lognorm


def GeneratePaths(NPaths,NSteps,T,r,sigma,S_0):    
    ''' Generates simulated paths for the GBM and ABM'''
    
    # Create matrices
    np.random.seed(72)
    Z = np.random.normal(0.0,1.0,[NPaths,NSteps])
    X = np.zeros([NPaths, NSteps+1])
    time = np.zeros([NSteps+1])
        
    X[:,0] = np.log(S_0)
    
    dt = T / float(NSteps)
    for i in range(0,NSteps):
        # Standarize make sure each column has mean 0 and variance 1
        if NPaths > 1:
            Z[:,i] = (Z[:,i] - np.mean(Z[:,i])) / np.std(Z[:,i])
        X[:,i+1] = X[:,i] + (r - 0.5 * sigma **2 ) * dt + sigma * np.power(dt, 0.5)*Z[:,i]
        time[i+1] = time[i] + dt
        
    #Compute exponent of ABM
    S = np.exp(X)
    paths = {"time":time, "X":X, "S":S}
    return paths


def PlotPaths(timeGrid, X, S):
    ''' Plots the simulated paths'''
    
    # Create the subplots
    fig = plt.figure(figsize=(12, 6))
    gs = GridSpec(1, 2)
    ax1 = plt.subplot(gs[0, 0])
    ax2 = plt.subplot(gs[0, 1])

    # X(t)
    ax1.plot(timeGrid, np.transpose(X))   
    ax1.set_xlabel("time")
    ax1.set_ylabel("X(t)")
    ax1.set_title("ABM")

    # S(t)
    ax2.plot(timeGrid, np.transpose(S))   
    ax2.set_xlabel("time")
    ax2.set_ylabel("S(t)")
    ax2.set_title("GBM")
    

def PlotDistribution(NPaths, NSteps, X, S):
    ''' Plots the final time distribution '''
    
    fig = plt.figure(figsize=(12, 6))
    gs = GridSpec(1, 2, wspace=0.3)
    ax1 = plt.subplot(gs[0, 0])
    ax2 = plt.subplot(gs[0, 1])
      
    ax1.hist(X[:,-1], bins=25, density=True, alpha=0.6, color='b') 
    ax1.set_ylim(bottom=0)
    mu, std = norm.fit(X[:,-1])
    xmin, xmax = ax1.get_xlim() 
    x = np.linspace(xmin, xmax, 100) 
    p = norm.pdf(x, mu, std) 
    ax1_right = ax1.twinx()
    ax1_right.set_ylim(bottom=0) 
    ax1_right.plot(x, p, 'k', linewidth=2)
    ax1_right.set_ylim(bottom=0)
    ax1.set_xlabel("X(t)")
    ax1.set_ylabel("Normal PDF")
    ax1.set_title("ABM")
    
    ax2.hist(S[:,-1], bins=25, density=True, alpha=0.6, color='b')
    ax2.set_ylim(bottom=0)
    shape, loc, scale = lognorm.fit(S[:,-1])
    xmin, xmax = ax2.get_xlim()
    x = np.linspace(xmin, xmax, 100) 
    p = lognorm.pdf(x, shape, loc=loc, scale=scale) 
    ax2_right = ax2.twinx()
    ax2_right.plot(x, p, 'k', linewidth=2)
    ax2_right.set_ylim(bottom=0)
    ax2.set_xlabel("S(t)")
    ax2.set_ylabel("Log-Normal PDF")
    ax2.set_title("GBM")


def main():
    ''' Function to be executed'''
    
    # Parameters
    NPaths = 500
    NSteps = 500
    T = 1
    r = 0.05
    sigma = 0.4
    S_0 = 100
    
    # Generate Paths
    Paths = GeneratePaths(NPaths,NSteps,T,r,sigma,S_0)
    timeGrid = Paths["time"]
    X = Paths["X"]
    S = Paths["S"]
    
    # Plot Paths
    PlotPaths(timeGrid, X, S)
    
    # Plot Final Distribution
    PlotDistribution(NPaths, NSteps, X, S)
    
    
main()