class Limit{
    static final int MIN = -50000;
    static final int MAX = 50000;
}

class Solution {
    public int solution(int num1, int num2) {
        int result = 0;
        
        if(Limit.MIN <= num1 && num1 <= Limit.MAX && Limit.MIN <= num2 && num2 <= Limit.MAX) {
            result = num1 + num2;
        }
        
        return result;
    }
}