def can_build(length, num_5m_bricks, num_1m_bricks):
    max_length_with_5m = min(num_5m_bricks * 5, length)
    remaining_length = length - max_length_with_5m
    return remaining_length <= num_1m_bricks

print(can_build(13, 2, 3))
print(can_build(13, 1, 3))
print(can_build(15, 1, 20))
