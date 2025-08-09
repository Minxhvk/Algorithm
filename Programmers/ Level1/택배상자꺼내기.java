class Solution {
    public int solution(int n, int w, int num) {
        
        int nLevel = (n-1) / w;
        int curLevel = (num-1) / w;
        
        int answer =  nLevel - curLevel ;
        
        int curIndex = 0;
        int nIndex = 0;
        
        if (curLevel % 2 == 0) {
            curIndex = num % w - 1;
            if (curIndex == -1) curIndex = w-1;
        } else {
            curIndex = w - (num % w);
            if (curIndex == w) curIndex = 0;
        }
        
        if (nLevel % 2 == 0) {
            nIndex = n % w - 1;
            if (nIndex == -1) nIndex = w-1;
            
            if (nIndex < curIndex) answer--;
        } else {
            nIndex = w - (n % w);
            if (nIndex == w) nIndex = 0;
            if (nIndex > curIndex) answer--;
        }
        
        return answer + 1;
    }
}