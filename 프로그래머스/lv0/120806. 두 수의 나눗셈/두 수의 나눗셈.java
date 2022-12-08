class Solution {
    public int solution(int num1, int num2) {
        
        int answer = 0;
        
        if ( num1 < 0 || num1 > 100 || num2 <0 || num2 > 100) {
            return 0;
        }
        
        double result = (double)num1 / num2 * 1000;

        answer = (int)result;

        return answer;
    }
}