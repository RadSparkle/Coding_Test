class Solution {
    public int[] solution(int rows, int columns, int[][] queries) {
        int[][] matrix = new int[rows][columns];
        int[] answer = new int[queries.length];
        
        // 행렬 초기화
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < columns; j++) {
                matrix[i][j] = i * columns + j + 1;
            }
        }
        
        // 쿼리 수행
        for (int i = 0; i < queries.length; i++) {
            int x1 = queries[i][0] - 1;
            int y1 = queries[i][1] - 1;
            int x2 = queries[i][2] - 1;
            int y2 = queries[i][3] - 1;
            
            int temp = matrix[x1][y1];
            int min = temp;
            
            // 왼쪽 변 회전
            for (int j = x1; j < x2; j++) {
                matrix[j][y1] = matrix[j + 1][y1];
                min = Math.min(min, matrix[j][y1]);
            }
            
            // 아래쪽 변 회전
            for (int j = y1; j < y2; j++) {
                matrix[x2][j] = matrix[x2][j + 1];
                min = Math.min(min, matrix[x2][j]);
            }
            
            // 오른쪽 변 회전
            for (int j = x2; j > x1; j--) {
                matrix[j][y2] = matrix[j - 1][y2];
                min = Math.min(min, matrix[j][y2]);
            }
            
            // 위쪽 변 회전
            for (int j = y2; j > y1; j--) {
                matrix[x1][j] = matrix[x1][j - 1];
                min = Math.min(min, matrix[x1][j]);
            }
            
            matrix[x1][y1 + 1] = temp;
            answer[i] = min;
        }
        
        return answer;
    }
}