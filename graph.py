#import numpy as np
import pandas as pd
import csv





fi = pd.read_csv("AnimeData.csv", on_bad_lines='skip')
fi = pd.DataFrame(fi)
#fi = fi.sample(frac=1)
print(fi)

