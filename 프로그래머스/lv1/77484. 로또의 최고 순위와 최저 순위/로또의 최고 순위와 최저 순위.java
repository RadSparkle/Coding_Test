import java.util.Arrays;

class Solution {
    public int[] solution(int[] lottos, int[] win_nums) {
        int unknownCount = 0; // 알아볼 수 없는 번호의 개수
        int matchCount = 0; // 일치하는 번호의 개수

        // 알아볼 수 없는 번호의 개수와 일치하는 번호의 개수를 센다
        for (int lotto : lottos) {
            if (lotto == 0) {
                unknownCount++;
            } else if (Arrays.stream(win_nums).anyMatch(num -> num == lotto)) {
                matchCount++;
            }
        }

        // 최고 순위 = 일치하는 번호의 개수 + 알아볼 수 없는 번호의 개수
        // 최저 순위 = 일치하는 번호의 개수
        int[] answer = new int[]{getRank(matchCount + unknownCount), getRank(matchCount)};
        return answer;
    }

    // 일치하는 번호의 개수를 기반으로 순위를 반환하는 메서드
    private int getRank(int matchCount) {
        if (matchCount == 6) {
            return 1;
        } else if (matchCount == 5) {
            return 2;
        } else if (matchCount == 4) {
            return 3;
        } else if (matchCount == 3) {
            return 4;
        } else if (matchCount == 2) {
            return 5;
        } else {
            return 6;
        }
    }
}
