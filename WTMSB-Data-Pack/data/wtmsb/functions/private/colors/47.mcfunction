execute if score colorCode wtmsbTmp matches 12 run data merge entity @s {Particle: "minecraft:dust 0.0000 0.2000 1.0000 0.28", Radius: 0.02f}
execute unless score colorCode wtmsbTmp matches 12 run function wtmsb:private/colors/48
