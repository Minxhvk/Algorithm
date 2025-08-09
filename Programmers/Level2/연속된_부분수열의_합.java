class Solution {
    public int[] solution(int[] sequence, int k) {
        int n = sequence.length;
        int left = 0;
        long sum = 0;
        int bestL = 0, bestR = n; // bestR-bestL를 크게 시작

        for (int right = 0; right < n; right++) {
            sum += sequence[right];

            while (left <= right && sum > k) sum -= sequence[left++];

            if (sum == k) {
                if (right - left < bestR - bestL) { // 더 짧은 구간만 갱신 (같은 길이면 앞선 구간 유지)
                    bestL = left;
                    bestR = right;
                }
            }
        }
        return new int[]{bestL, bestR};
    }
}
