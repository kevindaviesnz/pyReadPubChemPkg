# See https://packaging.python.org/en/latest/tutorials/packaging-projects/
# See https://realpython.com/api-integration-in-python/

# python -m pip install requests
# To package:
# python3 -m pip install --upgrade build
# python3 -m build
# https://test.pypi.org/account/register/
# https://test.pypi.org/manage/account/#api-tokens
# python3 -m pip install --upgrade twine
# python3 -m twine upload --repository testpypi dist/pubchem_chemical*
# https://test.pypi.org/project/pubchem-chemical-reader/0.0.1/

# To install:
# python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps pubchem_chemical_reader

import requests
import sys

from settings import SettingsProvider

# @todo Add logging
def read_from_pubchem(SMILES:str):
    properties = SettingsProvider.PUBCHEM_PROPERTIES
    pubchem_url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/smiles/{SMILES}/property/{','.join(properties)}/JSON"
    response = requests.get(pubchem_url)
    return response.json()

if __name__ == "__main__":
    # python3 read_from_pubchem.py SMILES
    SMILES: str = sys.argv[1]
    chemical_from_pubchem = read_from_pubchem(SMILES)
    print(chemical_from_pubchem)
