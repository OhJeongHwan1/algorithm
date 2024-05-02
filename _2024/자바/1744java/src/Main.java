import java.io.*;
import java.util.*;

public class Main {
    static int n;
    static int total = 0;
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        int[] numbers = new int[n];
        for (int i=0; i<n; i++){
            numbers[i] = Integer.parseInt(br.readLine());
        }
        
        if (n == 1) {
            System.out.println(numbers[0]);
        }
        else{
            Arrays.sort(numbers);
            int index = n-1;
            while (index >= 0){
                if (index - 1 == -1){
                    if(numbers[index] >= 1) {
                        total += numbers[index];
                    }
                    break;
                }
                if (numbers[index] <= 1){
                    if(numbers[index] == 1) {
                        total += 1;
                        index -= 1;
                    }else break;
                }
                else if (numbers[index] > 1 && numbers[index-1] > 1){
                    total += numbers[index] * numbers[index-1];
                    index -= 2;
                }
                else if (numbers[index] > 1 && numbers[index-1] <= 1){
                    total += numbers[index];
                    index -= 1;
                }
                
            }
            index = 0;
            while (index < n){
                if (numbers[index] >= 0){
                    break;
                }
                if (index + 1 == n){
                    total += numbers[index];
                    break;
                }
                else if (numbers[index] < 0 && numbers[index+1] < 0){
                    total += numbers[index] * numbers[index+1];
                    index += 2;
                }
                else if (numbers[index] < 0 && numbers[index+1] >= 0){
                    if (numbers[index+1] == 0){
                        total += numbers[index] * numbers[index+1];
                    } else total += numbers[index]; 
                    break;
                }
            }
            System.out.println(total);
        }
        
    }
}
