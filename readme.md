# Documentation du jeu de données de position

# Guide sur l'installation
Téléchargement des données.
Les différentes sources semblaient conseiller de laisser les données RAWS en ligne puis d'avoir des scripts pour télécharger.
Cela me semble adapté pour ne pas avoir un repository trop lourd.
Un échantillon des données est présent dans "database_presentation"



## Preparation
A définir

## "Requirements"
A définir



# Description des données

## Images 
Exemple de 9 images prisent au même point avec des conditions météorologiques différentes.
![alt text](images_readme/conditions_differentes_9.png)


## Structure des documents
**Proposition pour les images** \
Chaque dossier contient les images prisent en un point avec un seul YAML qui contient la position GPS du point de référence,
le nom de chaque image avec la date et la météo donnée par l'API.
Un fichier JSON est aussi présent avec les mêmes informations. Les deux formats sont présents en attendant qu'un choix définitif du format soit fait.

    .
    ├── pos1
    │   ├── img1.jpg
    │   ├── img2.jpg
    │   ├── ...
    │   └── informations.yaml           
    └── ...

*Strucutre d'informations.yaml:*
```yaml
location:
  longitude: -72.75105721420168
  latitude: 46.57270499758702
nombre_d_images: 15
nombre_de_directions: 2 
camera_informations: null
images:
  - name: position_trigger_11_17_2022-04_31_12.jpg
    date: '2022-11-17 09:31:12.661685+00:00'
    weathercode: 51
    meteo: Light Drizzle
    direction: 0
    heading: null
  - ...
```



## Génération des données


Pour le jeu de données d'images. 8072 points ont été générés sur les routes du Québec. 
![alt text](images_readme/Sampling_points.png)



# License

# Citations

# Travail additionnel
(si on veut citer les autres travaux de IVIS)



