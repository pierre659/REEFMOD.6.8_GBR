#%%
import pandas as pd
from pathlib import Path


#%%
repot = Path('/c/Users/josep/Documents/Mines/crise/REEFMOD.6.8_GBR')
pd.read_csv(str(repot / ))

#%%


json_root = {     'type': 'FeatureCollection',     'crs': {         'type': 'name',         'properties': {             'name': 'urn:ogc:def:crs:OGC:1.3:CRS84'         }     },     'meta': {         'name': OUTPUT_NAME,     } }  for t in range(output_meta['n_timesteps']):     path = JSON_OUTPATH + f't{t}.geojson'     feature_list = []     for reef in range(output_meta['n_reefs']):         feature_list.append({             'type': 'Feature',             'properties': {                 'reef_id': reef,                 'label': OUTPUT_NAME,                 'radius': 1000. * np.random.rand(),                 'value': outputs_df[t][reef],             },             'geometry': {                 'type': 'Point',                 'coordinates': [lat[reef], lon[reef]]             }         })      json_root['features'] = feature_list     json_root['meta']['time_step'] = t     json_root['meta']['IPCC_scenario'] = 'IPCC_scenario_name'     with open(path, 'w') as out:         json.dump(json_roo
# build JSON :
# root level : a list of length n_timesteps
#   level 1 : a list of objects of the form
#   {'x': longitude, 'y': latitude, 'label': OUTPUT_NAME, 'value': a float value}
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

for t in range(nyears):
    t_str = t + 1985
    path = JSON_OUTPATH + f't{t_str}.geojson'
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
                'coordinates': [lon[reef], lat[reef]]
            }
        })

    json_root['features'] = feature_list
    json_root['meta']['time_step'] = t
    json_root['meta']['IPCC_scenario'] = 'IPCC_scenario_name'
    with open(path, 'w') as out:
        json.dump(json_root, out, indent=2) 