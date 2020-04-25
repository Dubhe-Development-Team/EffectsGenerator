#> wtmsb:private/paint
# @as player

function wtmsb:private/set_buffer

# Kill old paint.
tag @s add wtmsb_self
execute as @e[tag=wtmsb_spray] if score @s wtmsbUid = @a[limit=1,tag=wtmsb_self] wtmsbUid run kill @s
execute as @e[tag=wtmsb_paint] if score @s wtmsbUid = @a[limit=1,tag=wtmsb_self] wtmsbUid run kill @s
tag @a remove wtmsb_self

# Set ray tracing markers.
scoreboard players set scanDirection wtmsbTmp 1
scoreboard players set xCursor wtmsbTmp 0
scoreboard players set yCursor wtmsbTmp 0
# Get players's rotation in three axises.
execute positioned 0.0 0.0 0.0 run summon minecraft:area_effect_cloud ^ ^ ^4 {Tags: ["wtmsb_rotation_marker"]}
execute store result score xRotation wtmsbTmp run data get entity @e[limit=1,type=minecraft:area_effect_cloud,tag=wtmsb_rotation_marker] Pos[0] 1000
execute store result score yRotation wtmsbTmp run data get entity @e[limit=1,type=minecraft:area_effect_cloud,tag=wtmsb_rotation_marker] Pos[1] 1000
execute store result score zRotation wtmsbTmp run data get entity @e[limit=1,type=minecraft:area_effect_cloud,tag=wtmsb_rotation_marker] Pos[2] 1000
kill @e[type=minecraft:area_effect_cloud,tag=wtmsb_rotation_marker]
## SPRAY TRACING!
### No `anchored eyes` since it doesn't change gradually.
execute anchored eyes positioned ^0.4 ^0.4 ^ anchored feet run function wtmsb:private/summon_at_each_point

# Checkout.
scoreboard players operation @s wtmsbCool = $max wtmsbCool

# Effect.
playsound wtmsb:item.spray_can.use player @a
