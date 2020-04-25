#> wtmsb:private/summon_at_each_point
# @description
# Recurse in order to execute a bunch of ray tracings. 
# The number of execution is determined by `wtmsbXMax wtmsbTmp` and `wtmsbYMax wtmsbTmp` defined in `wtmsb:private/image_data`.
# @as player
# @params
# - scanDirection wtmsbTmp: -1 to the left, 1 to the right
# - xCursor wtmsbTmp: The position in the X axis, starting from 0.
# - yCursor wtmsbTmp: The position in the Y axis, starting from 0.
# - wtmsbXMax wtmsbTmp
# - wtmsbYMax wtmsbTmp

# Get the next color code.
execute store result score colorCode wtmsbTmp run data get storage wtmsb: buffer[0]
data remove storage wtmsb: buffer[0]

# Set one pixel.
execute if score colorCode wtmsbTmp matches 1.. run function wtmsb:private/summon_a_spray

# Move xCursor.
scoreboard players operation xCursor wtmsbTmp += scanDirection wtmsbTmp

# Turn to new row...
scoreboard players set shouldTurn wtmsbTmp 0
## while scanning from the left to the right.
### Set shouldTurn.
execute if score xCursor wtmsbTmp > wtmsbXMax wtmsbTmp run scoreboard players set shouldTurn wtmsbTmp 1
### Switch scanDirection.
execute if score xCursor wtmsbTmp > wtmsbXMax wtmsbTmp run scoreboard players set scanDirection wtmsbTmp -1
### Move the cursor back in the range.
execute if score xCursor wtmsbTmp > wtmsbXMax wtmsbTmp run scoreboard players remove xCursor wtmsbTmp 1
## while scanning from the right to the left.
### Do the same things as above.
execute if score xCursor wtmsbTmp matches ..-1 run scoreboard players set shouldTurn wtmsbTmp 1
execute if score xCursor wtmsbTmp matches ..-1 run scoreboard players set scanDirection wtmsbTmp 1
execute if score xCursor wtmsbTmp matches ..-1 run scoreboard players add xCursor wtmsbTmp 1
## Turn actually.
execute if score shouldTurn wtmsbTmp matches 1 run scoreboard players add yCursor wtmsbTmp 1

# Recurse...
## while not finishing the last row...
### if should turn.
execute if score yCursor wtmsbTmp <= wtmsbYMax wtmsbTmp if score shouldTurn wtmsbTmp matches 1 positioned ^ ^-0.05 ^ run function wtmsb:private/summon_at_each_point
### if should not turn...
#### while moving from the left to the right.
execute if score yCursor wtmsbTmp <= wtmsbYMax wtmsbTmp if score shouldTurn wtmsbTmp matches 0 if score scanDirection wtmsbTmp matches 1 positioned ^-0.05 ^ ^ run function wtmsb:private/summon_at_each_point
#### while moving from the right to the left.
execute if score yCursor wtmsbTmp <= wtmsbYMax wtmsbTmp if score shouldTurn wtmsbTmp matches 0 if score scanDirection wtmsbTmp matches -1 positioned ^0.05 ^ ^ run function wtmsb:private/summon_at_each_point
