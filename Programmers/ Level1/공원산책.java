import java.util.Map;
import java.util.HashMap;

class Solution {
    public int[] solution(String[] park, String[] routes) {
        int[] answer = {};
        int h = park.length;
        int w = park[0].length();
        
        String[][] board = new String[h][w];
        Map<String, int[]> dir = new HashMap<String, int[]>(){{
            put("E", new int[]{0, 1});
            put("W", new int[]{0, -1});
            put("S", new int[]{1, 0});
            put("N", new int[]{-1, 0});
        }};
        
        
        for (int i = 0; i < h ;i++) {
            for (int j = 0; j < w; j++) {
                char curChar = park[i].charAt(j);
                board[i][j] = String.valueOf(curChar);
                
                if (curChar == 'S') answer = new int[]{i, j};
            }
        }
        
        for (String route: routes) {
            String[] d = route.split(" ");
            String direction = d[0];
            int step = Integer.parseInt(d[1]);
            
            boolean flag = true;
            int[] target = dir.get(direction);
            
            for (int i=1; i < (step + 1); i++) {
                int dx = answer[0] + target[0] * i;
                int dy = answer[1] + target[1] * i;
                
                if (dx < 0 || dx >= h || dy < 0 || dy >= w) {
                    flag = false;
                    continue;
                }
                if (board[dx][dy].equals("X")) {
                    flag = false;
                    break;
                }
            }
            
            if (flag) {
                answer[0] += target[0] * step;
                answer[1] += target[1] * step;
            }
        }
        
        return answer;
    }
}