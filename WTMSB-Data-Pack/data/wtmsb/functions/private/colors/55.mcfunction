execute if score colorCode wtmsbTmp matches 20 run data merge entity @s {Particle: "minecraft:dust 0.0000 0.6000 0.2000 0.28", Radius: 0.02f}
execute unless score colorCode wtmsbTmp matches 20 run function wtmsb:private/colors/56
