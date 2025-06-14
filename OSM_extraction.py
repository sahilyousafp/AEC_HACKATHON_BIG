import osmnx as ox
import matplotlib.pyplot as plt

# --- STEP 1: Define Coordinates for Bounding Box (e.g., a small area in Barcelona) ---
north, south, east, west = 41.400, 41.390, 2.175, 2.160  # Modify with your desired location
Location = [north, south, east, west]

# --- STEP 2: Define Amenity Tags from OSM Wiki ---
# You can add more amenity types as needed
tags = {
    'amenity': [
        'restaurant', 'cafe'
    ]
}

# --- STEP 3: Download OSM Features for Given Tags ---
print("Downloading OSM data...")
amenities = ox.features_from_bbox(Location, tags)

# --- STEP 4: Plot Amenities ---
fig, ax = plt.subplots(figsize=(12, 12))
amenities.plot(ax=ax, column='amenity', legend=True, cmap='tab20', markersize=30)

# Add labels (names of amenities)
for idx, row in amenities.iterrows():
    name = row.get('name')
    if name:
        try:
            centroid = row.geometry.centroid
            ax.text(centroid.x, centroid.y, name, fontsize=7)
        except:
            pass

ax.set_title("OSM Amenities in Selected Area", fontsize=16)
ax.set_xlabel("Longitude")
ax.set_ylabel("Latitude")
plt.grid(True)
plt.tight_layout()
plt.show()
