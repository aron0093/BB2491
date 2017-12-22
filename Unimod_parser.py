# -*- coding: utf-8 -*-
"""
Auth:Revant Gupta

HTA Project 8
"""

import pandas as pd
import sys

fil = open(sys.argv[1])# Enter the obo unimod data as the first argument
dat = fil.readlines()

dic = {} # Dictionary to store unimod id data

for line in dat:
    if line[:2] =='id':

        indx = dat.index(line)+1
        itr = indx+1
        
        while itr < len(dat) and dat[itr] != '\n':
            itr += 1              

        dic[line[:-1]] = dat[indx:itr]

dat_mass = pd.DataFrame(index = dic.keys(),
                        columns = ['name', 'mono_mass', 'avg_mass', 'PTM']) # Dataframe to store the various types of modifications (by ID) and their mass.

for key, value in dic.items():

    PTM = 'No'

    name = value[0].split()[1]

    for row in value:

        if row.split()[1] == 'delta_mono_mass':
            mono_mass = float(row.split()[2][1:-1])
            
        if row.split()[1] == 'delta_avge_mass':    
            avg_mass = float(row.split()[2][1:-1])

        for word in row.split():

            if word[1:-1] == 'Post-translational':
                PTM = 'Yes'

    dat_mass.loc[key] = [name, mono_mass, avg_mass, PTM]
        
