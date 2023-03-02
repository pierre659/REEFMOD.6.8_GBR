# %%
import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy

# %%
###############################################################################
################# Données DHW ##################################
###############################################################################
repot = Path('c:\\Users\\josep\\Documents\\Mines\\crise\\REEFMOD.6.8_GBR')
outputs_df = pd.read_csv(str(repot / 'geo_DHW.csv'))

OUTPUT_NAME = 'DHW'

json_root = {
    'type': 'FeatureCollection',
    'crs': {
        'type': 'name',
        'properties': {
            'name': 'urn:ogc:def:crs:OGC:1.3:CRS84'
        }
    },
    'meta': {
        'name': OUTPUT_NAME,
    }
}

nyears = len(outputs_df.DHW[0])
json_list = []
JSON_OUTPATH = repot / 'json_files'
for t in range(nyears):
    t_str = t + 1985
    path = JSON_OUTPATH / f't{t_str}.geojson'
    feature_list = []
    for reef in outputs_df.Reef_ID:
        feature_list.append({
            'type': 'Feature',
            'properties': {
                'reef_id': reef,
                'label': OUTPUT_NAME,
                'radius': 1000. * np.random.rand(),
                'value': outputs_df.DHW[t],
            },
            'geometry': {
                'type': 'Point',
                'coordinates': [outputs_df['LON'][reef-1],
                                outputs_df['LAT'][reef-1]]
            }
        })

    json_root['features'] = feature_list
    json_root['meta']['time_step'] = t
    json_root['meta']['IPCC_scenario'] = 'IPCC_scenario_name'
    json_list.append(json_root)


with open(str(JSON_OUTPATH / 'DHW.geosjon'), 'w') as out:
    json.dump(json_root, out, indent=2)

# %%


def mortality(output_mat):
    mat['']
    return 0


# %% list(mat.keys())
repot = Path('c:\\Users\\josep\\Documents\\Mines\\crise\\REEFMOD.6.8_GBR')


mat = scipy.io.loadmat(str(
    repot / 'IPCC_45_2050_MIROC5_45.mat'))

param_plot = 'coral_cover_per_taxa'


def postprocess(data):
    """
    return mean, std
    """
    # sum accross species / size...
    while len(data.shape) > 3:
        data = data.sum(axis=-1)
    # average over
    data = data.mean(axis=1)
    return data.mean(axis=0), data.std(axis=0)


fig, ax = plt.subplots()
data = mat[param_plot]
mean, std = postprocess(data)

nb_steps = 87
x = np.arange(nb_steps)/2+2008
ax.plot(x, mean, color='tab:green', label='RCP 45')
ax.fill_between(x, mean - std, mean +
                std, color='tab:green', alpha=0.2)


mat = scipy.io.loadmat(str(
    repot / 'R0_BCA_Moore_fog_MIROC5_45.mat'))

mean, std = postprocess(mat[param_plot])

ax.plot(x, mean, color='tab:red', label='45 + fog')
ax.fill_between(x, mean - std, mean +
                std, color='tab:red', alpha=0.2)
ax.legend(ncols=2)
ax.set_title(param_plot)

# %%
mat = scipy.io.loadmat(str(
    repot / 'R0_BCA_Moore_IPCC26_2050_MIROC5_26.mat'))
fig, ax = plt.subplots()

data = mat[param_plot]
mean, std = postprocess(data)
fig, ax = plt.subplots()

nb_steps = 87
x = np.arange(nb_steps)/2+2008
ax.plot(x, mean, color='tab:green', label='RCP 26')
ax.fill_between(x, mean - std, mean +
                std, color='tab:green', alpha=0.2)
# %%
