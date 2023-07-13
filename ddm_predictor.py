import os, sys
from scipy.spatial import distance
from rdkit.Chem import AllChem as Chem
#from rdkit.Chem import Draw
from rdkit.Chem.AllChem import MolFromSmiles
from rdkit.Chem.Draw import MolsToGridImage
from rdkit.Chem.Draw import MolToFile
from rdkit.DataStructs import cDataStructs
from collections import Counter
from sklearn.manifold import TSNE
from math import sqrt
from math import ceil
from datetime import datetime
#Plotting imports
import cairocffi
from cairosvg import svg2png
import numpy as np
import pandas as pd
