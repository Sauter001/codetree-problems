n = int(input())
blocks = [int(input()) for _ in range(n)]
num_blocks = sum(blocks)

# Please write your code here.
blocks_per_pos = num_blocks // n
blocks_to_move = [x - blocks_per_pos if x > blocks_per_pos else 0 for x in blocks]

print(sum(blocks_to_move))