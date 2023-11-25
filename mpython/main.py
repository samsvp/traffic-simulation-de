#%%
import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


with open("data.json") as fp:
    data = json.load(fp)
    
print(data.keys())

#%%   
plt.plot(data['vehCount'])

# %%
plt.plot(data['flows'])
plt.title(f"Flow = 3600 * dN/dt (veh/h), dt={data['dtAggr']}")
plt.show()

# %%
plt.plot(data['speeds'])
plt.title(f"Speed = 3.6 * sum(v)/len(v) (km/h)")
plt.show()
plt.plot(data['dens'])
plt.title("Density = flow / speed (veh/km)")
plt.show()

# %%
plt.plot(data['ts'])

# %%
sum(data["vehCount"])

# %%
# Flatten the nested structure and create a list of dictionaries
flat_data = []
for ts, vehicles in zip(data["ts"], data["vehiclesU"]):
    for vehicle in vehicles:
        flat_data.append({"id": vehicle["id"], "u": vehicle["u"], "ts": ts})

# Create a DataFrame from the flattened data
df = pd.DataFrame(flat_data)
# %%
plt.plot(data["speeds"])

# %%
