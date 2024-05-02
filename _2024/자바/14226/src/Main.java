import java.io.*;
import java.util.*;

public class Main {
    static int s;
    static int clib_board;
    static int[] dp;
    static int num,time;
    static boolean[][] visited = new boolean[1001][1001];//[clipboard][total] 
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        s = Integer.parseInt(br.readLine());
        dp = new int[1001];
        for (int i=0; i <= s; i++){
            dp[i] = 1001;
        }
        dp[1] = 0;
        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[]{1,0,0});
        int[] node;
        visited[0][1] = true; 

        while (!queue.isEmpty()){
            node = queue.poll();
            num = node[0];
            clib_board = node[1];
            time = node[2];
            if (num == s){
                System.out.println(time);
                break;
            }
            
            queue.add(new int[]{num,num,time+1});

            if (clib_board != 0 && clib_board+num <=s && !visited[clib_board][clib_board+num]){
                queue.add(new int[]{clib_board+num,clib_board,time+1});
                visited[clib_board][clib_board+num] = true;
            }
            if (num >= 1 && !visited[clib_board][num - 1]){
                queue.add(new int[]{num-1,clib_board,time+1});
                visited[clib_board][num - 1] = true;
            }

        }
    }
}
