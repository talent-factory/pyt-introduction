import json

notebook = '01-Introduction-to-Python.ipynb'

with open(notebook) as f:
    data = json.load(f)

for cell in data['cells']:
    if cell['cell_type'] == 'code':
        if cell['execution_count'] is None:
            cell['execution_count'] = 1

with open(notebook, 'w') as f:
    json.dump(data, f, indent=4)
#%%
