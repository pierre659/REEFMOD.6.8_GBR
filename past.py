
# %%
from pathlib import Path

import numpy as np
import pandas as pd
import scipy.io

# %%
repot = Path('c:\\Users\\josep\\Documents\\Mines\\crise\\REEFMOD.6.8_GBR')
mat_DHW = scipy.io.loadmat(str(
    repot / 'data/Climatology/Past/GBR_past_DHW_CRW_5km_1985_2020.mat'))['GBR_PAST_DHW']


# %%

gps_coords = pd.read_csv('GBR_REEF_POLYGONS_2022.csv')
gps_coords.set_index('Reef_ID', inplace=True)

gps_coords['DHW'] = list(mat_DHW)
