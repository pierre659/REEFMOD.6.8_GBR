
# %%
import numpy as np
import pandas as pd
import scipy.io

# %%
mat = scipy.io.loadmat('R0_BCA_Moore_MIROC5_45.mat')

meta = mat['META']
vals = meta
keys = meta.dtype.descr
meta_dic = {}
# Assemble the keys and values into variables with the same name as that used in MATLAB
for i in range(len(keys)):
    key = keys[i][0]
    # squeeze is used to covert matlat (1,n) arrays into numpy (1,) arrays.
    val = np.squeeze(vals[key][0][0])
    meta_dic[key] = val

reef_ID_list = meta_dic['reef_ID']

gps_coords = pd.read_csv('GBR_REEF_POLYGONS_2022.csv')
gps_coords.set_index('Reef_ID', inplace=True)
gps_coords = gps_coords.iloc[reef_ID_list]

# %%
coral_cover_per_taxa = mat['coral_cover_per_taxa'].mean(axis=0).sum(axis=-1)
for i, idx in enumerate(reef_ID_list):
    gps_coords[reef_ID_list[i]]['coral_cover'] = coral_cover_per_taxa[i]
# %%
