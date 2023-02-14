# Documentation du jeu de données de position

# Guide sur l'installation
Un échantillon des données est présent dans "database_presentation"



# Description des données

## Images 
Exemple de 9 images prisent au même point avec des conditions météorologiques différentes.
![alt text](images_readme/conditions_differentes_9.png)


## Structure des documents
Chaque dossier contient les images prisent en un point avec un seul YAML qui contient la position GPS du point de référence, le nom de chaque image avec la date et la météo donnée par l'API (Open-Meteo).
Un fichier JSON est aussi présent avec les mêmes informations. Les deux formats sont présents en attendant qu'un choix définitif du format soit fait.

Différents véhicules ont été utilisés pour générer la base de données, ceux-ci ont des calibrations de caméra différentes qui sont spécifiées pour chacun. Chaque image pointe vers une calibration.



    .
    ├── pos1
    │   ├── img1.jpg
    │   ├── img2.jpg
    │   ├── ...
    │   ├── informations.json
    │   └── informations.yaml           
    ├── camera_calibration.yaml
    └── ...

*Strucutre d'**informations.yaml**:*
```yaml
location:
  longitude: -72.75105721420168
  latitude: 46.57270499758702
nombre_d_images: 15
images:
  - name: position_trigger_11_17_2022-04_31_12.jpg
    date: '2022-11-17 09:31:12.661685+00:00'
    weathercode: 51
    meteo: Light Drizzle
    heading: null
    camera_informations: null
  - ...
```

*Strucutre de **camera_calibration.yaml**:*
```yaml
calibrations:
  cam1: null
  cam2: null
  ...
```


## Génération des données
8072 points ont été générés sur les routes du Québec. 
![alt text](images_readme/Sampling_points.png)


