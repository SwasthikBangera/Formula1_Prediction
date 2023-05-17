#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 16 09:33:24 2023

@author: SwasthikBangera
@project: Formula1 winner prediction

"""

# Importing the dependencies

import pandas as pd
import numpy as np



constructor_df = pd.read_csv('constructors.csv')

print(constructer_df)

driver_df = pd.read_csv('drivers.csv')