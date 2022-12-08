class Solution {
    public int solution(int n, int k) {
        int yangPrice = 12000 * n;
        
        int drinkPirce = (k - n/10) * 2000;
        
        int result = yangPrice + drinkPirce;
        
        return result;
    }
}