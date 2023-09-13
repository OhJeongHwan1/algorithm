import java.io.BufferedReader;
import java.io.InputStreamReader;
public class Main {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int first = Integer.parseInt(br.readLine());
        int newNum = first;
        int count = 0;
        do{
            newNum = ((newNum % 10)*10) + ((newNum/10 + newNum%10)%10);
            count++;
        }while(first != newNum);
        System.out.println(count);
    }
}