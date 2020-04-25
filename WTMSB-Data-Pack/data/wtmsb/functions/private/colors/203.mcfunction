execute if score colorCode wtmsbTmp matches 200 run data merge entity @s {Particle: "minecraft:dust 1.0000 0.6000 0.2000 0.28", Radius: 0.02f}
execute unless score colorCode wtmsbTmp matches 200 run function wtmsb:private/colors/204
