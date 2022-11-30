class Solution {
    public int[] solution(int denum1, int num1, int denum2, int num2) {
        int mole = (denum1 * num2)+(denum2 * num1); //분자
        int divisor = num1 * num2; //분수
        int num = 1; //최대공약수 초기값

        for(int i = divisor;  i > 1 ;i--){
            if(mole%i ==0 && divisor%i ==0) {
                num = i;
                break;
            }
        }

        int test3 = divisor/num;
        int test4 = mole/num;

        int[] answer = new int[]{test4,test3};

        return answer;
    }
}