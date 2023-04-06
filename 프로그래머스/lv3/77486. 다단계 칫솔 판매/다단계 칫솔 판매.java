import java.util.*;

class Solution {
    public int[] solution(String[] enroll, String[] referral, String[] seller, int[] amount) {
        int n = enroll.length;
        Map<String, Integer> indexMap = new HashMap<>();
        Map<String, Node> nodeMap = new HashMap<>();

        for (int i = 0; i < n; i++) {
            indexMap.put(enroll[i], i);
            nodeMap.put(enroll[i], new Node(enroll[i]));
        }

        for (int i = 0; i < n; i++) {
            String parent = referral[i];
            if (!parent.equals("-")) {
                nodeMap.get(enroll[i]).parent = nodeMap.get(parent);
            }
        }

        int m = seller.length;
        for (int i = 0; i < m; i++) {
            Node sellerNode = nodeMap.get(seller[i]);
            int sellAmount = amount[i] * 100;
            while (sellerNode != null && sellAmount > 0) {
                int commission = sellAmount / 10;
                sellerNode.profit += sellAmount - commission;
                sellAmount = commission;
                sellerNode = sellerNode.parent;
            }
        }

        int[] answer = new int[n];
        for (int i = 0; i < n; i++) {
            answer[i] = nodeMap.get(enroll[i]).profit;
        }

        return answer;
    }

    static class Node {
        String name;
        int profit;
        Node parent;

        public Node(String name) {
            this.name = name;
        }
    }
}
