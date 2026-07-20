class Solution:
    def jump(self, nums: list[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0

        # keep count of number of jumps
        jumps = 0

        # keep track of the end of the current jump
        current_jump_end = 0

        # keep track of the farthest point we can reach
        farthest = 0

        # iterate through the array except the last element as we don't need to jump from the last element
        for i in range(n - 1):
            # update farthest point we can reach
            farthest = max(farthest, i + nums[i])

            # if we have reached the end of the current jump, so we have to make a jump
            if i == current_jump_end:
                jumps += 1
                current_jump_end = farthest

                # if we have reached the end of the array, we don't need to jump anymore
                if current_jump_end >= n - 1:
                    break

        return jumps