#> wtmsb:private/summon_a_spray
# @params
# - xRotation wtmsbTmp
# - yRotation wtmsbTmp
# - zRotation wtmsbTmp

# Summon.
summon minecraft:area_effect_cloud ~ ~ ~ {Tags: ["newly_summoned", "mrcd_bullet", "wtmsb_spray"], CustomName: '"WTMSB spray"', Duration: 1000, Color: -1}

scoreboard players operation @e[tag=newly_summoned] wtmsbUid = @s wtmsbUid

# Set color.
scoreboard players operation @e[tag=newly_summoned,limit=1,distance=..0.01,type=minecraft:area_effect_cloud] wtmsbTmp = colorCode wtmsbTmp

# Do an ray trancing.
scoreboard players operation @e[tag=newly_summoned,limit=1,distance=..0.01,type=minecraft:area_effect_cloud] mrcd_x0 = xRotation wtmsbTmp
scoreboard players operation @e[tag=newly_summoned,limit=1,distance=..0.01,type=minecraft:area_effect_cloud] mrcd_y0 = yRotation wtmsbTmp
scoreboard players operation @e[tag=newly_summoned,limit=1,distance=..0.01,type=minecraft:area_effect_cloud] mrcd_z0 = zRotation wtmsbTmp

# Checkout.
tag @e remove newly_summoned
