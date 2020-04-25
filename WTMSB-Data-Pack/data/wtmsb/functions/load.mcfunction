#> wtmsb:load
# @manual
# # How to Add a Paint?
# 1. Add the paint to `storage wtmsb:`, located in function `wtmsb:image_data`.
# 2. Update function `wtmsb:private/set_buffer`, so players can copy this paint into buffer.
# 3. Add color(s) in function `wtmsb:colors` if you want to introduce new color(s).

# Objectives.
scoreboard objectives add wtmsbClick minecraft.used:minecraft.carrot_on_a_stick "WTMSB player right click"
scoreboard objectives add wtmsbUid dummy "WTMSB unique identifier"
scoreboard objectives add wtmsbTmp dummy "WTMSB temp"
scoreboard objectives add wtmsbType dummy "WTMSB player's spray type"
scoreboard objectives add wtmsbCool dummy "WTMSB player's cooldown"

# Consts
scoreboard players set $max wtmsbCool 50

# `buffer` stores the current drawing paint.
data modify storage wtmsb: {} merge value {buffer: []}

# Stores pixels in this paint in 'S' shape:
# --------->
# <---------
# --------->
# <---------
# Note: the first two bytes represent wtmsbXMax and wtmsbYMax.
function wtmsb:private/image_data
