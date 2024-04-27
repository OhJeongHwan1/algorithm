import java.io.*;
import java.util.*;

public class Main {
    static int[][] move = {
        {1, 0},
        {0, 1},
        {-1, 0},
        {0, -1}
    };
    static StringBuilder sb;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader((System.in)));
        sb = new StringBuilder();
        String[] input = br.readLine().split(" ");
        int n = Integer.parseInt(input[0]);
        int m = Integer.parseInt(input[1]);
        int[][] map = new int[n][m];
        int[][] visited = new int[n][m];
        HashMap<Integer,Integer> grCnt = new HashMap<>();

        for(int i=0; i<n; i++){
            input = br.readLine().split("");
            for(int j=0; j<m; j++){
                map[i][j] = Integer.parseInt(input[j]);
            }
        }
        Queue<int[]> queue = new LinkedList<>();
        
        int group_id = 1;
        for(int i=0; i<n; i++){
            for(int j=0; j<m; j++){
                if (map[i][j] == 0 && visited[i][j] == 0){
                    visited[i][j] = group_id;
                    queue.add(new int[]{i,j});
                    int[] xy;
                    int cnt = 0;
                    while(queue.size() != 0){
                        xy = queue.poll();
                        cnt += 1;
                        
                        for(int[] dir : move){
                            int nx = xy[0] + dir[0];
                            int ny = xy[1] + dir[1];
                            if (0<=nx&&nx<n&&0<=ny&&ny<m&&map[nx][ny] == 0 && visited[nx][ny] == 0){
                                visited[nx][ny] = group_id;
                                queue.add(new int[]{nx,ny});
                            }
                        }
                    }
                    grCnt.put(group_id,cnt);
                    group_id += 1;
                }
            }
        }

        for(int i=0; i<n; i++){
            for(int j=0; j<m; j++){
                if(map[i][j] == 0){
                    sb.append(0);
                }
                else{
                    int count = 1;
					Set<Integer> set = new HashSet<>();
                    for(int[] dir : move){
                        int nx = i + dir[0];
                        int ny = j + dir[1];
                        if (0<=nx&&nx<n&&0<=ny&&ny<m&&map[nx][ny] == 0&&visited[nx][ny]!=0){
                            set.add(visited[nx][ny]);
                        }
                    }
                    for(int group : set){
                        count += grCnt.get(group);
                    }
                    sb.append(count%10);
                }
            }
            sb.append("\n");
        }
        System.out.println(sb);
    }
}
