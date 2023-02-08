# Documentation des datasets d'images et de conduite
Ce readme est pour le futur repository github des datasets mais le repo n'existe pas encore.




# Guide sur l'installation
Téléchargement des données.
Les différentes sources semblaient conseiller de laisser les données RAWS en ligne puis d'avoir des scripts pour télécharger.
Cela me semble adapter parce que je trouve intéressant de pouvoir télécharger les données dans des arrangements différents (trié par point ou par météo). Sauf si on arrive à faire un package qui garde ces deux informations et permet une séparation facile pour l'utilisateur. 

## Preparation
A définir

## "Requirements"
A définir



# Description des données

## Images 
Exemple de 9 images prisent au même point avec des conditions météorologiques différentes.
![alt text](data/images_readme/conditions_differentes_9.png)

## Rosbag
Qu'est-ce que c'est un Rosbag?
C'est quoi un topic?

Liste des topics:
Unités et signification de chacun, ce qu'il peut contenir. La fréquence



## Structure des documents
**Proposition pour les images** \
Chaque dossier contient les images prisent en un point avec un seul YAML qui contient la position GPS du point de référence,
le nom de chaque image avec la date et la météo donnée par l'API.

    .
    ├── pos1
    │   ├── img1.jpg
    │   ├── img2.jpg
    │   ├── ...
    │   └── informations.yaml           
    └── ...

*Strucutre d'informations.yaml:*
```yaml
localisation : (-73,45)
nombre_d_images: 15
nombre_de_directions: 2
images:
  - img:
    name: "nomDeLimage.jpg"
    weathercode: 75
    meteo:  soleil
    date: 2023-01-22
    direction: 0 
  - img:
    ...
```


**Proposition pour les enregistrements** \
Quatres dossiers séparent le type de route. Ensuite chaque sous-dossier contient tous les bags associés à une position.
Un YAML global référence tous les bags avec leur date, et la météo. (copie en json pour avoir un avis du MTQ sur leurs préférences)

    .
    ├── position1
    │   ├── position_trigger1.bag
    │   │   ├── metadata.yaml
    │   │   └── position_trigger1.bag_0.db3
    │   ├── position_trigger2.bag
    │   ├── ...
    │   ├── informations.json
    │   └── informations.yaml
    ├── position2
    └── ...

Les "metadata.yaml" sont déjà présents dans la base de données et contiennent les infos relatives à chaque bag.

*Strucutre d'informations.yaml:*
```yaml
- position:
  nom_folder: "position1"
  localisation : (-73,45)
  nombre_de_bags: 17
  bags:
    - bag:
      name: "nomDuBag.bag"
      weathercode: 75
      meteo:  soleil
      timestamp: 2022_01_27-10h00 (format exemple)
      type: Intersection
      essui-glace: true
    - bag:
      ...
- position:
    ...
```




> **Discussions**
>
> Est-ce qu'il vaut mieux un YAML par position ou un YAML global qui référence tout?





## Génération des données


Pour le jeu de données d'images. 8072 points ont été générés sur les routes du Québec. 
![alt text](data/images_readme/Sampling_points.png)


EN: (For the images, random sample points were created on the map.
For the driving videos, sample points were chosen on specific type of roads:
-Straight roads
-Curvy roads
-intersection between two roads
-Starting/exit of highway

Multiple cars were equiped with gps to trigger when they passed through these points.)



# License

# Citations

# Travail additionnel
(si on veut citer les autres travaux de IVIS)



