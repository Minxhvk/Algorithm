import java.util.*;

class Solution {
    public int solution(int[][] points, int[][] routes) {
        int answer = 0;
        
        List<List<String>> history = new ArrayList<>();
        history.add(new ArrayList<>()); // 0

        for (int i=0; i<routes.length; i++) {
            int idx = 0;
            int sx = points[routes[i][0] - 1][0] - 1;
            int sy = points[routes[i][0] - 1][1] - 1;
            
            history.get(0).add(sx + "," + sy);

            for (int j=1; j < routes[i].length; j++) {
                int tx = points[routes[i][j] - 1][0] -1;
                int ty = points[routes[i][j] - 1][1] -1;
                idx = recordHistory(idx, history, sx, sy, tx, ty);
                sx = tx; sy = ty;
            }
        }
        
        for (int t = 0; t < history.size(); t++) {
            Map<String, Integer> freq = new HashMap<>();
            for (String pos : history.get(t)) freq.put(pos, freq.getOrDefault(pos, 0) + 1);
            for (int c : freq.values()) if (c > 1) answer++;
        }
        
        return answer;
    }
    
    public int recordHistory(int idx, List<List<String>> history, int sx, int sy, int tx, int ty) {
        int x = sx, y = sy;
        
        int stepx = Integer.compare(tx, sx); // -1, 0, 1
        int stepy = Integer.compare(ty, sy);
        
        while (x != tx) {
            x += stepx;
            idx++;
            while (history.size() <= idx) {
                history.add(new ArrayList<>());
            }
            history.get(idx).add(x + "," + y);
        }
        while (y != ty) { 
            y += stepy; 
            idx++;
            while (history.size() <= idx) {
                history.add(new ArrayList<>());    
            }
            history.get(idx).add(x + "," + y);
        }

        return idx;
    }
}