#> wtmsb:tick

execute as @a at @s run function wtmsb:tick_player
scoreboard players reset * wtmsbClick

tag @e[type=minecraft:area_effect_cloud,tag=wtmsb_pre_changing_spray,sort=random,limit=10] add wtmsb_changing_spray
execute as @e[type=minecraft:area_effect_cloud,tag=wtmsb_changing_spray] at @s run function mrcd:generic/start
kill @e[type=minecraft:area_effect_cloud,tag=wtmsb_changing_spray,tag=!mrcd_touch_edge]
execute as @e[type=minecraft:area_effect_cloud,tag=wtmsb_changing_spray] at @s run function wtmsb:private/turn_a_spray_into_paint
