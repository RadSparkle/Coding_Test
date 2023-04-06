import java.util.*;

class Solution {
    public int[] solution(String[] enroll, String[] referral, String[] seller, int[] amount) {
        Map<String, String> parent = new HashMap<>();
        Map<String, Integer> profit = new HashMap<>();
        for (int i = 0; i < enroll.length; i++) {
            parent.put(enroll[i], referral[i]);
            profit.put(enroll[i], 0);
        }
        for (int i = 0; i < seller.length; i++) {
            String cur = seller[i];
            int curAmount = amount[i] * 100;
            while (!cur.equals("-")) {
                int parentAmount = curAmount / 10;
                int curProfit = curAmount - parentAmount;
                profit.put(cur, profit.get(cur) + curProfit);
                cur = parent.get(cur);
                curAmount = parentAmount;
                if (parentAmount == 0) break;
            }
        }
        int[] answer = new int[enroll.length];
        for (int i = 0; i < enroll.length; i++) {
            answer[i] = profit.get(enroll[i]);
        }
        return answer;
    }
}
