import java.util.Map;
import java.util.HashMap;

class Solution {
    public int[] solution(String[] name, int[] yearning, String[][] photo) {
        int len = name.length;
        int[] answer = new int[photo.length];
        
        
        Map<String, Integer> board = new HashMap<>();
        
        for (int i=0;i < len; i++) {
            board.put(name[i], yearning[i]);
        }
        
        for (int i=0; i < photo.length; i++) {
            for (int j=0; j < photo[i].length; j++) {
                String cur = photo[i][j];
                
                int score = board.getOrDefault(cur, 0);
                answer[i] += score;
            }
        }
        
        return answer;
    }
}