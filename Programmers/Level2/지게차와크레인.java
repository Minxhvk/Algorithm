import java.util.*;

class Solution {
    public int solution(String[] storage, String[] requests) {
        final int H = storage.length, W = storage[0].length();
        
        char[][] board = new char[H][W];
        for (int i = 0; i < H; i++) board[i] = storage[i].toCharArray();
        
        int minus = 0;
        int ans = H * W;
        int[] dx = {0, 0, 1, -1};
        int[] dy = {1, -1, 0, 0};
        
        for (String req: requests) {
            char target = req.charAt(0);
            
            // 지게차
            if (req.length() == 1) {
                List<int[]> toRemove = new ArrayList<>();
                
                for (int i=0; i < H; i++) {
                    for (int j=0; j < W; j++) {
                        if (board[i][j] != target) continue;
                        
                        if (i == 0 || i == H-1 || j == 0 || j == W-1) {
                            toRemove.add(new int[]{i, j});
                            continue;
                        }
                        
                        boolean canMoveOut = false;
                        boolean[][] vis = new boolean[H][W];
                        
                        Deque<int[]> q = new ArrayDeque<>();
                        q.add(new int[]{i, j});
                        vis[i][j] = true;
                        
                        while (!q.isEmpty() && !canMoveOut) {
                            
                            int[] cur = q.poll();
                            int x = cur[0], y = cur[1];
                            
                            for (int k=0; k < 4; k++) {
                                
                                int curX = x + dx[k];
                                int curY = y + dy[k];

                                if (curX < 0 || curX >= H || curY < 0 || curY >= W) {
                                    canMoveOut = true;
                                    break;
                                }

                                if (!vis[curX][curY] && board[curX][curY] == '#') {
                                    vis[curX][curY] = true;
                                    q.add(new int[]{curX, curY});
                                }
                            }
                        }
                        
                        if (canMoveOut) {
                            toRemove.add(new int[]{i, j});
                        }
                    }
                }
                
                for (int[] remove: toRemove) {
                    board[remove[0]][remove[1]] = '#';
                    ans--;
                }
            } 
            // 크레인
            else {
                for (int i=0; i < H; i++) {
                    for (int j=0; j < W; j++) {
                        if (board[i][j] == target) {
                            board[i][j] = '#';
                            ans--;
                        }
                    }
                }
            }
        }
        
        return ans;
    }
}