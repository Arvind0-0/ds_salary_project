# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 12:15:56 2024

@author: as799
"""

import glassdorr_Scrapper as gs

path = "C:/User/as799/OneDrive/Documents/Github/ds_salary/project/chromedriver"

df = gs.get_jobs('data scientist', 10, False, path, 5)