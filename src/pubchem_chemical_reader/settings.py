from pydantic_settings import BaseSettings, SettingsConfigDict
import logging
import os


class Settings(BaseSettings):
     LOG_LEVEL: int = logging.INFO
     PUBCHEM_PROPERTIES: list = ["IUPACName", "MolecularFormula", "MolecularWeight",
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
 
SettingsProvider = Settings()
