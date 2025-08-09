import java.util.Arrays;

class Solution {
    public int solution(int[] diffs, int[] times, long limit) {
        int answer = 0;
        int dL = diffs.length;
        
        int start = 1;
        int end = Arrays.stream(diffs).max().getAsInt();
        int mid = 0;
        
        while (start <= end) {
            
            mid = (end + start) / 2;
            
            long timeSum = 0;
            
            for (int i=0; i<dL; i++) {
                
                if (timeSum > limit) break;
                
                int diff = diffs[i];
                int time = times[i];
                
                if (diff <= mid) {
                    timeSum += time;
                    continue;
                }
                
                timeSum += (diff - mid) * time + time;
                timeSum += times[i-1] * (diff-mid);
            }
            
            if (timeSum <= limit) {
                answer = mid;
                end = mid - 1;
            } else {
                start = mid + 1;
            }
        }
        
        
        return answer;
    }
}