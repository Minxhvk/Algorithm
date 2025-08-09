class Solution {
    public int solution(String[][] board, int h, int w) {
        int answer = 0;
        
        int[] dx = {1, -1, 0, 0};
        int[] dy = {0, 0, 1, -1};
        
        int maxX = board.length;
        int maxY = board[0].length;
        
        String curColor = board[h][w];
        
        for(int i=0; i<4; i++) {
            int curX = h + dx[i];
            int curY = w + dy[i];
            
            if (curX < 0 || curX >= maxX || curY < 0 || curY >= maxY) continue;
            
            if (board[curX][curY].equals(curColor)) answer++;
        }
        
        return answer;
    }
}