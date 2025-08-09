import java.util.Map;
import java.util.HashMap;

class Solution {
    public int solution(String[] friends, String[] gifts) {
        int answer = 0;
        Map<String, Map<String, Integer>> giftMap = new HashMap<>();
        
        for (String i: gifts) {
            String[] parts = i.split(" ");
            String giver = parts[0], receiver = parts[1];
            
            giftMap
              .computeIfAbsent(giver, k -> new HashMap<>())
              .merge(receiver, 1, Integer::sum);

            giftMap
              .get(giver)
              .merge("score", 1, Integer::sum);

            giftMap
              .computeIfAbsent(receiver, k -> new HashMap<>())
              .merge("score", -1, Integer::sum);
        }
        
        for (String i: friends) {
            
            Map<String,Integer> userMap = giftMap.getOrDefault(i, new HashMap<>());
            int totCount = 0;
            int curScore = userMap.getOrDefault("score", 0);
            
            for (String j: friends) {
                if (i.equals(j)) continue;
                
                int sent = userMap.getOrDefault(j, 0);
                Map<String, Integer> targetMap = giftMap.getOrDefault(j, new HashMap<>());
                int given = targetMap.getOrDefault(i, 0);
                
                if (given < sent) {
                    totCount++;
                } else if (given == sent) {
                    int targetScore = targetMap.getOrDefault("score", 0);
                    
                    if (targetScore < curScore) {
                        totCount++;
                    }
                }   
            }
            
            answer = Math.max(answer, totCount);
        }
        
        return answer;
    }
}