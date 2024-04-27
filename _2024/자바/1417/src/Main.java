import java.io.*;
import java.util.*;

public class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader((System.in)));
        int n = Integer.parseInt(br.readLine());
        ArrayList<Integer> hubo = new ArrayList<Integer>();
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());

        for (int i=0;i<n;i++){
            hubo.add(Integer.parseInt(br.readLine()));
        }
        int ans = 0;
        int dasom = hubo.get(0);
        hubo.remove(0);
        
        for(int i=0; i<n-1; i++){
            pq.add(hubo.get(i));
        }
        if (n == 1){
            System.out.println(ans);
            
        }
        else{
            int other = 0;
            while(true){
                other = pq.remove();
    
                if (dasom > other){
                    break;
                }
                else{
                    dasom += 1;
                    other -= 1;
                    ans += 1;
                    pq.add(other);
                }
            }
            System.out.println(ans);
        }
    }
}