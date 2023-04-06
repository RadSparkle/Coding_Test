import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int h = Integer.parseInt(st.nextToken());
        int w = Integer.parseInt(st.nextToken());
        int n = Integer.parseInt(br.readLine());
        int[][] stk = new int[n][2];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            stk[i][0] = Integer.parseInt(st.nextToken());
            stk[i][1] = Integer.parseInt(st.nextToken());
        }
        int result = 0;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                int r1 = stk[i][0];
                int c1 = stk[i][1];
                int r2 = stk[j][0];
                int c2 = stk[j][1];
                if ((r1 + r2 <= h && Math.max(c1, c2) <= w) || (Math.max(r1, r2) <= h && c1 + c2 <= w)) {
                    result = Math.max(result, r1 * c1 + r2 * c2);
                }
                if ((c1 + r2 <= h && Math.max(r1, c2) <= w) || (Math.max(c1, r2) <= h && r1 + c2 <= w)) {
                    result = Math.max(result, r1 * c1 + r2 * c2);
                }
                if ((c1 + c2 <= h && Math.max(r1, r2) <= w) || (Math.max(c1, c2) <= h && r1 + r2 <= w)) {
                    result = Math.max(result, r1 * c1 + r2 * c2);
                }
                if ((r1 + c2 <= h && Math.max(c1, r2) <= w) || (Math.max(r1, c2) <= h && c1 + r2 <= w)) {
                    result = Math.max(result, r1 * c1 + r2 * c2);
                }
            }
        }
        System.out.println(result);
    }
}
