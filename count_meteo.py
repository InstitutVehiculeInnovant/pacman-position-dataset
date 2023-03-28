import os
import json
import matplotlib.pyplot as plt

"""
Compte le nombre de météos de chaque type
"""
source = "../DATASET/images_V3/"
file = "position_metadata.json"

count_nones = 0
output = {}
for location in os.listdir(source):
    if not os.path.isdir(source + location): continue
    with open(source + location + "/" + file) as f:
        data = json.load(f)
        for image in data["images"]:
            if image["meteo"] is None:
                count_nones += 1
            if image["meteo"] not in output:
                output[image["meteo"]] = 0
            output[image["meteo"]] += 1


fig, ax = plt.subplots()
print("nombre de Null:",count_nones)
print(output)
wedges, texts = ax.pie(output.values(), labels=output.keys())
# pourcentage: autopct='%1.1f%%'
# ax.legend(wedges, [meteo for meteo, value in output.items() if value < 500],
#           title = "Meteo",loc = "center right")
plt.savefig("images_readme/meteo_pie.png")
plt.show()


