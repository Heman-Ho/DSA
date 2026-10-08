class Solution:
    # [2 4 -4 -1]
    # asteroid = 0
    # stack: [2]
    # res: []
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res = [] 
        stack = [] 

        # stack holding all asteroids going right
        for asteroid in asteroids:
            if asteroid > 0:
                stack.append(asteroid)

            # if asteroid is going left,
            else:
                # collide the asteroid going left with ones going right
                while stack and -asteroid > stack[-1]:
                    stack.pop()
                if stack and stack[-1] == -asteroid:
                    stack.pop()
                elif not stack:
                    res.append(asteroid)
                    
        return res + stack