# Documentation du jeu de données de position


# Guide sur l'installation
Un échantillon des données est présent dans "database_presentation"

# Description des données

## Images 
Exemple de 9 images prisent au même point avec des conditions météorologiques différentes.
![alt text](images_readme/conditions_differentes_9.png)


## Structure des documents
Chaque dossier contient les images prisent en un point avec un seul JSON qui contient la position GPS du point de référence, le nom de chaque image avec la date et la météo donnée par l'API (Open-Meteo).

Différents véhicules ont été utilisés pour générer la base de données, ceux-ci ont des calibrations de caméra différentes qui sont spécifiées pour chacun. Chaque image pointe vers une calibration.


    .
    ├── pos1
    │   ├── img1.jpg
    │   ├── img2.jpg
    │   ├── ...
    │   └── informations.json         
    ├── camera_calibration.json
    └── ...

*Strucutre d'**informations.json**:*
```json
{
  "location": {
    "longitude": -72.68331306797108,
    "latitude": 46.63511346710158
  },
  "n_images": 10,
  "images": [
    {
      "name": "position_trigger_11_18_2022-07_17_43.jpg",
      "date": "2022-11-18 12:17:43.758705+00:00",
      "weathercode": 1.0,
      "meteo": "Mainly Clear",
      // "camera_informations": null
    },
    {"...":"..."} 
  ]
}
```

## Meteo 
Chaque image contient "weathercode" et "meteo", ces deux informations sont redondantes. "weathercode" est le code de la météo donné par l'API (Open-Meteo) et "meteo" est la signification du code.

| Code | Condition | Traduction française |
| --- | --- | --- |
| 0 | Clear Sky | Ciel dégagé |
| 1 | Mainly Clear | Principalement dégagé |
| 2 | Partly Cloudy | Partiellement nuageux |
| 3 | Overcast | Couvert |
| 45 | Fog | Brouillard |
| 48 | Depositing Rime Fog | Brouillard givrant |
| 51 | Light Drizzle | Légère bruine |
| 53 | Moderate Drizzle | Bruine modérée |
| 55 | Dense Intensity Drizzle | Bruine forte |
| 56 | Light Freezing Drizzle | Légère bruine verglaçante |
| 57 | Dense Intensity Freezing Drizzle | Bruine verglaçante forte |
| 61 | Slight Rain | Pluie légère |
| 63 | Moderate Rain | Pluie modérée |
| 65 | Heavy intensity Rain | Pluie forte |
| 66 | Light Freezing Rain | Légère pluie verglaçante |
| 67 | Heavy Intensity Freezing Rain | Pluie verglaçante forte |
| 71 | Slight Snow fall | Légère chute de neige |
| 73 | Moderate Snow fall | Chute de neige modérée |
| 75 | Heavy Intensity Snow fall | Chute de neige forte |
| 77 | Snow Grains | Grains de neige |
| 80 | Slight Rain Showers | Légères averses de pluie |
| 81 | Moderate Rain Showers | Averses de pluie modérées |
| 82 | Violent Rain Showers | Averses de pluie violentes |
| 85 | Slight Snow Showers | Légères averses de neige |
| 86 | Heavy Snow Showers | Averses de neige fortes |
| 95 | Thunderstorm | Orage |
| 96 | Thunderstorm With Slight | Orage avec légère pluie |
| 99 | Thunderstorm With Heavy Hail | Orage avec fortes chutes de grêle |


## Génération des données
8072 points ont été générés sur les routes du Québec. 
![alt text](images_readme/Sampling_points.png)


