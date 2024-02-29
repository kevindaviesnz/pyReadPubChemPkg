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

def read_from_pubchem(SMILES:str,  properties: list)->str:
    pubchem_url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/smiles/{SMILES}/property/{','.join(properties)}/JSON"
    response = requests.get(pubchem_url)
    return response.json()

if __name__ == "__main__":
    # python3 pubchem_reader.py SMILES
    SMILES: str = sys.argv[1]
    properties: list = ["IUPACName", "MolecularFormula", "MolecularWeight",
        "CanonicalSMILES", "IsomericSMILES", "InChI", "InChIKey",
        "XLogP", "ExactMass", "MonoisotopicMass", "TPSA",
        "Complexity", "Charge", "HBondDonorCount", "HBondAcceptorCount",
        "RotatableBondCount", "HeavyAtomCount", "IsotopeAtomCount", "AtomStereoCount",
        "DefinedAtomStereoCount", "UndefinedAtomStereoCount", "BondStereoCount", "DefinedBondStereoCount",
        "UndefinedBondStereoCount", "CovalentUnitCount", "Volume3D", "XStericQuadrupole3D",
        "YStericQuadrupole3D", "ZStericQuadrupole3D", "FeatureCount3D", "FeatureAcceptorCount3D",
        "FeatureDonorCount3D", "FeatureAnionCount3D", "FeatureCationCount3D", "FeatureRingCount3D",
        "FeatureHydrophobeCount3D", "ConformerModelRMSD3D", "EffectiveRotorCount3D", "ConformerCount3D",
        "Fingerprint2D"]
    chemical_from_pubchem = read_from_pubchem(SMILES=SMILES, properties=properties)
    print(chemical_from_pubchem)
