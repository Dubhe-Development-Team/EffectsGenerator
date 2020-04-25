#> wtmsb:private/turn_a_spray_into_paint
# @as [tag=wtmsb_spray]

# Summon.
summon minecraft:area_effect_cloud ~ ~ ~ {Tags: ["newly_summoned", "wtmsb_paint"], CustomName: '"WTMSB paint"', Duration: 1000, Color: -1}

scoreboard players operation @e[tag=newly_summoned] wtmsbUid = @s wtmsbUid

# Set color.
scoreboard players operation colorCode wtmsbTmp = @s wtmsbTmp
execute as @e[tag=newly_summoned,limit=1,distance=..0.01,type=minecraft:area_effect_cloud] run function wtmsb:private/colors/1

# Checkout.
tag @e remove newly_summoned
kill @s
