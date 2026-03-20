import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

matches_path = os.path.join(BASE_DIR, "data", "raw", "matches.csv")
deliveries_path = os.path.join(BASE_DIR, "data", "raw", "deliveries.csv")

matches = pd.read_csv(matches_path)
deliveries = pd.read_csv(deliveries_path)

print(matches.shape)
print(deliveries.shape)