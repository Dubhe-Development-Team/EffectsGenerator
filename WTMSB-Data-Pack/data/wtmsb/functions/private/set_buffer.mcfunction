#> wtmsb:private/set_buffer
# @as player
# @return
# - wtmsbXMax wtmsbTmp
# - wtmsbYMax wtmsbTmp

# Copy buffer.
function wtmsb:private/copy_buffer

# Set resolution.
execute store result score wtmsbXMax wtmsbTmp run data get storage wtmsb: buffer[0]
data remove storage wtmsb: buffer[0]
execute store result score wtmsbYMax wtmsbTmp run data get storage wtmsb: buffer[0]
data remove storage wtmsb: buffer[0]
