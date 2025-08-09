import java.util.Map;
import java.util.HashMap;

class Solution {
    public String[] solution(String[] players, String[] callings) {
        String[] answer = {};
        
        Map<String, Integer> pos = new HashMap<>();
        
        for (int i=0;i<players.length;i++) pos.put(players[i], i);
        
        for (String call: callings) {
            int idx = pos.get(call);
            String temp = players[idx-1];
            
            players[idx-1] = call;
            players[idx] = temp;
            
            pos.put(call, idx-1);
            pos.put(temp, idx);
        }
        
        return players;
    }
}