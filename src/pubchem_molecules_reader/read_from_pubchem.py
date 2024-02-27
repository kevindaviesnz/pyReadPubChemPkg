# See https://packaging.python.org/en/latest/tutorials/packaging-projects/
# See https://realpython.com/api-integration-in-python/

# python -m pip install requests
# To package:
# python3 -m pip install --upgrade build
# python3 -m build

import requests
from settings import SettingsProvider

def read_from_pubchem(SMILES:str):
    
    pubchem_url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/smiles/{SMILES}/property/{','.join(SettingsProvider.PUBCHEM_PROPERTIES)}/JSON"

    # print(response.json())
    response = requests.get(pubchem_url)
    return response.json()

