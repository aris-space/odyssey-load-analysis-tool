# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 10:13:03 2022

@author: Simon Höhener
"""

### library imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#from math import pi
##For Plotting
from matplotlib.patches import Rectangle
from matplotlib.patches import Polygon


def test_1():
    ###Skeleton Config (here launch config)
    #AirframeInputData=pd.read_excel(r'C:\Users\simon\Documents\00_ETH\4-ARIS\00_Odyssey\ALAT\test.xlsx', sheet_name='test')
    #print(AirframeInputData)

    ##Airframe Definition
    #Nose Cone
    NC_top_z=0.0
    NC_top_diameter=0.0
    NC_length=0.8
    NC_bottom_z=NC_length
    NC_bottom_diameter=0.3
    NC_number_node=2
    NC_mass=8.0
    NC_CoG_z=0.5
    #NC discretization
    NC_z=np.linspace(NC_top_z, NC_bottom_z, num=NC_number_node)
    NC_z = np.append (NC_z,NC_CoG_z)
    #NC_z=np.sort(NC_z)

    #Recovery Fairing
    RF_top_z=NC_bottom_z
    RF_top_diameter=0.3
    RF_length=1.5
    RF_bottom_z=RF_top_z+RF_length
    RF_bottom_diameter=0.3
    RF_number_node=2
    RF_mass=4.0
    RF_CoG_z=(RF_bottom_z+RF_top_z)/2
    #RF discretization
    RF_z=np.linspace(RF_top_z, RF_bottom_z, num=RF_number_node)
    RF_z = np.append (RF_z,RF_CoG_z)
    #Avionics Fairing
    AF_top_z=RF_bottom_z
    AF_top_diameter=0.3
    AF_length=0.8
    AF_bottom_z=AF_top_z+AF_length
    AF_bottom_diameter=0.3
    AF_number_node=2
    AF_mass=5.0
    AF_CoG_z=(AF_bottom_z+AF_top_z)/2
    #AF discretization
    AF_z=np.linspace(AF_top_z, AF_bottom_z, num=AF_number_node)
    AF_z = np.append (AF_z,AF_CoG_z)
    #Propulsion Fairing
    PF_top_z=AF_bottom_z
    PF_top_diameter=0.3
    PF_length=3.65
    PF_bottom_z=PF_top_z+PF_length
    PF_bottom_diameter=0.3
    PF_number_node=2
    PF_mass=9.0
    PF_CoG_z=(PF_bottom_z+PF_top_z)/2
    #PF discretization
    PF_z=np.linspace(PF_top_z, PF_bottom_z, num=PF_number_node)
    PF_z = np.append (PF_z,PF_CoG_z)
    #Fins
    FI_top_z=6.25
    FI_root_cord=0.4
    FI_bottom_z=FI_top_z+FI_root_cord
    FI_span=0.2
    FI_number_fins=4
    FI_mass_per_fin=1.8
    #Boattail
    BT_top_z=PF_bottom_z
    BT_top_diameter=0.3
    BT_length=0.2
    BT_bottom_z=BT_top_z+BT_length
    BT_bottom_diameter=0.2
    BT_number_node=2
    BT_CoG_z=BT_top_z+0.4*BT_length
    BT_mass=4.0
    #BT discretization
    BT_z=np.linspace(BT_top_z, BT_bottom_z, num=BT_number_node)
    BT_z = np.append (BT_z,BT_CoG_z)


    #====================================================
    ##Load mass config
    MassConfigInput=pd.read_excel(r'C:\Users\simon\Documents\00_ETH\4-ARIS\00_Odyssey\ALAT\MassConfig.xlsx', sheet_name='mass_config')
    MassMatrix= MassConfigInput[['Group ID', 'Mass [kg]','CoG_z','LiP1','LiP2']]
    #TO DO sorting MassMatrix
    #helper
    print(MassConfigInput)
    #print(len(MassConfigInput))




    #====================================================
    #Graphical representation
    lineOffset=0.01
    fig, ax = plt.subplots()

    #create simple line plot
    #ax.plot()


    #------------Stick-Model-------------------------------------
    Rocket=np.concatenate((NC_z, RF_z,AF_z,PF_z,BT_z))
    y = np.zeros(len(Rocket))
    ax.plot(Rocket, y, '.-',lw = '1',color='k', markerfacecolor='k',markeredgecolor='k')


    #------------Wireframe---------------------------------------
    RowIndex_MassConfigInput=0
    for RowIndex_MassConfigInput in range(len(MassConfigInput)):
        if MassConfigInput.iloc[RowIndex_MassConfigInput,2]==0:
            print(MassConfigInput.iloc[RowIndex_MassConfigInput,0])
            
            ax.add_patch(Rectangle((MassConfigInput.iloc[RowIndex_MassConfigInput,7], (-MassConfigInput.iloc[RowIndex_MassConfigInput,10])/2.0), MassConfigInput.iloc[RowIndex_MassConfigInput,9], MassConfigInput.iloc[RowIndex_MassConfigInput,10],
                        edgecolor = 'k',
                        facecolor = 'blue',
                        fill=False,
                        lw=1))
            
            print('done')

    RowIndex_MassConfigInput+=1
    
    #print(MassConfigInput.iloc[3,0])






    #add NC 
    ax.add_patch(Polygon([(NC_length,NC_bottom_diameter/2), (0,0), (NC_length,-NC_bottom_diameter/2),],
                        edgecolor = 'blue',
                        facecolor = 'blue',
                        fill=False,
                        lw=1))
    #add RF
    ax.add_patch(Rectangle((RF_top_z+lineOffset, -RF_top_diameter/2), RF_length-lineOffset, RF_top_diameter,
                edgecolor = 'red',
                facecolor = 'blue',
                fill=False,
                lw=1))
    #add AF
    ax.add_patch(Rectangle((AF_top_z+lineOffset, -AF_top_diameter/2), AF_length-lineOffset, AF_top_diameter,
                edgecolor = 'green',
                facecolor = 'blue',
                fill=False,
                lw=1))
    #add PF
    ax.add_patch(Rectangle((PF_top_z+lineOffset, -PF_top_diameter/2), PF_length-lineOffset, PF_top_diameter,
                edgecolor = 'purple',
                facecolor = 'blue',
                fill=False,
                lw=1))
    #add BT
    ax.add_patch(Polygon([(BT_top_z+lineOffset,BT_top_diameter/2), (BT_bottom_z,BT_bottom_diameter/2), (BT_bottom_z,-BT_bottom_diameter/2),(BT_top_z+lineOffset,-BT_top_diameter/2),],
                        edgecolor = 'yellow',
                        facecolor = 'blue',
                        fill=False,
                        lw=1))
    # FI - TO DO
    ax.add_patch(Polygon([(FI_top_z,PF_top_diameter/2), (FI_top_z+0.05,PF_top_diameter/2+FI_span), (FI_bottom_z-0.05,PF_top_diameter/2+FI_span), (FI_bottom_z,PF_top_diameter/2),],
                        edgecolor = 'brown',
                        facecolor = 'blue',
                        fill=False,
                        lw=1))
    ax.add_patch(Polygon([(FI_top_z,-PF_top_diameter/2), (FI_top_z+0.05,-(PF_top_diameter/2+FI_span)), (FI_bottom_z-0.05,-(PF_top_diameter/2+FI_span)), (FI_bottom_z,-PF_top_diameter/2),],
                        edgecolor = 'brown',
                        facecolor = 'blue',
                        fill=False,
                        lw=1))

    #display plot
    plt.axis('scaled')
    plt.show()