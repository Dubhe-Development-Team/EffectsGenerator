execute if score colorCode wtmsbTmp matches 64 run data merge entity @s {Particle: "minecraft:dust 0.2000 0.8000 0.6000 0.28", Radius: 0.02f}
execute unless score colorCode wtmsbTmp matches 64 run function wtmsb:private/colors/95
