---
level: orange
title: Wanhao d12 230/300
---

## Description

Nous avons deux Wanhao d12 230 et une 300. Nous privilegons la d12 300 pour les grosses pièces et les 230 pour le reste. Les deux sont capable d'imprimer du bicouleur, mais la plupart du temps nous ne faisons que des impressions en mono.

## Utilisation

Il y a trois étapes majeurs pour une imprpession. On parcourera rapidement les trois sans trop rentrer dans certains détails, si vous avez d'autres question n'hésitez pas à demander aux autres staffs ou managers.

### Design de la pièce

Pour le design, vous pouvez utilisez ce que vous voulez: Fusion360, Blender ou autre. Dans le process, n'oubliez pas de penser aux différentes contraintes d'impression.
Voici quelques conseils:

- pensez aux forces qui s'exerçeront sur la pièce.
- les détails trop petits (moins d'un mm).
- éviter les overhang.

### Slice

Pour Slice, nous utilisons Cura, il est installé sur le PC du lab. Commencez par importer votre modèle: `ctrl+o`, ensuite le placer sur la face qui semble la mieux comme base -> grosse surface plane ou alors un plan qui permet d'imprimer la piece avec le moins de supports possible.

Il existe deux profils préconfigurés: un pour la 230 et un autre pour la 300, ils sont update de temps en temps sur le repo `https://github.com/Atelier-Epita/cura`.
Ces profils influent directement sur la qualité des impressions.
Vous pouvez si vous le souhaitez creer votre propre profil en dupliquant un existant.

Voici quelques parametres qui pourraient être interessant à modifier suivant vos besoin (bien sûr je vous invite a aller regarder la doc pour de plus ample déscriptions):

- layer height -> dépends directement de la taille de la buse, en général correspond à la moitié de la taille de la buse.
- line width -> largeur d'une ligne imprimé, dépends aussi de la taille de la buse, la plupart du temps elle correspond a peu pret à la largeur de la buse +/- 10%.
- vitesse d'impression -> plus c'est élevé plus ça va vite, plus ça débite, plus ça fait des patés dégueux à certains endroits.
- infill density -> la densité des remplissages est importante si vous voulez faire des pièces où les contraintes sont importantes. Par défaut entre 15-20%, l'augmenter produira une pièce plus robuste mais demandera plus de temps a imprimer.
- supports -> votre pièce contient-elle des overhangs ? si oui: mettez des supports.
- temperatures -> il y a deux températures que vous pouvez régler si jamais vous imprimer avec du filament autre que celui par défaut: la température de la buse et celle du plateau, faites gaffe les plateaux des wanhao ne montent pas très haut, donc éviter d'y imprimer de l'ABS par exemple (de toute façon ça tiendra pas).
- plate adhesion -> pour certaines pièces, il est fortement recommandé de rajouter un raft ou un brim, ces deux méthodes permettent d'éviter que la pièce "warp" (voir la section troubleshooting pour plus d'information).

Une fois que vous avez des bons settings, vous pouvez appuyer sur le bouton slice en bas à droite. Sauvegardez le sur la SD (il y a des adaptateurs USB->SD qq part sur le bureau pour se faire).

### Impression

Maintenant la partie la plus fun: inserer la SD, puis appuyer sur print. L'imprimante se charge ensuite de lire le GCODE depuis la SD. On peut distinguer 3 séctions dans le gcode:

- start gcode -> la séquence d'instruction exécuté pour toutes les impressions. Elle permet l'initialisation des axes, de la temperature du plateau, de la buse, du néttoyage de la buse
- print -> le gcode généré par le slicer pour imprimer votre pièce.
- end gcode -> la séquence d'instruction de fin: refroidir la buse, le bed, lever la tête et la placer à l'origine.

(*Note: il peut être utile de préchauffer l'imprimante pour eviter de perdre du temps lors du lancement de l'impression*)

## Troubleshooting

Quelques problèmes courant et comment les fix dans la plupart des cas:

- warping -> c'est lorsque l'un bord ou une partie de la pièce ne tient plus sur le bed. Dans 50% des cas c'est dû au design de la pièce, dans le cas écheant, rajouter un brim devrait emplement suffire. dans les 50 autres pourcents restant, recalibrer le plateau peut être une option, néttoyer le plateau, et tout simplement imprimer plus lentement.
- blobs -> dû à une pression trop élevé dans la buse, des petits blobs se font apparaitre aux jointures lorsqu'une rétractation ou une pause a lieux. Pour réduire cet effet il faut réduire la vitesse d'extrusion, ce qui réduit la préssion dans la buse.
- stringing -> c'est quand ya pleins de petits fils dans l'impression, en vrai c'est pas hyper grave.
- l'impression ne démarre pas ? C'est un problème avec la sd. Formatter la carte sd, re-slice le modèle et réessayer.

## Maintenance

- changement de filament -> préchauffer la buse, une fois à température, retirer la bobine en tirant sur la languette. insérer la nouvelle en tirant sur la languette et en poussant jusqu'au bout.
- nettoyage de buse.
- lubrifier les axes.
- changement de buse.

## EPI obligatoire(s)

un maximum de swag.

## Précautions à prendre

Lors de la phase d'impression, faire particulierement attention au premier layer, il est crucial, il faut qu'il y ait une belle adhésion. En cas de doutes, relire la section troubleshooting.

## Après utilisation

- Nettoyer le plateau d'impression, enlever la ligne imprimé par la séquence de démarrage de l'imprimante.
- Si besoin, signaler tout problème en interne.
