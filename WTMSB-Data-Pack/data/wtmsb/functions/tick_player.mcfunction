#> wtmsb:tick_player

execute unless score @s wtmsbUid matches 0.. run function wtmsb:private/get_uid
execute unless score @s wtmsbType matches 1.. run scoreboard players set @s wtmsbType 1

execute if entity @s[scores={wtmsbClick=1..},predicate=wtmsb:is_spraying] run function wtmsb:paint

execute if score @s wtmsbCool matches 1.. run scoreboard players remove @s wtmsbCool 1

tag @e[type=minecraft:area_effect_cloud,tag=wtmsb_spray,sort=nearest,limit=16] add wtmsb_pre_changing_spray
