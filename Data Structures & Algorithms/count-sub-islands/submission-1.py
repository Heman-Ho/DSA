class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        rows,cols=len(grid2),len(grid2[0]);answer=0
        for r in range(rows):
            for c in range(cols):
                if grid2[r][c]==0:continue
                stack=[(r,c)];grid2[r][c]=0;good=True
                while stack:
                    u,v=stack.pop()
                    if grid1[u][v]==0:good=False
                    for x,y in [(u-1,v),(u+1,v),(u,v-1),(u,v+1)]:
                        if 0<=x<rows and 0<=y<cols and grid2[x][y]:grid2[x][y]=0;stack.append((x,y))
                answer+=good
        return answer
