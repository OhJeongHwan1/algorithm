import java.io.BufferedReader;
import java.io.InputStreamReader;
public class Main {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int f = Integer.parseInt(br.readLine());

        int front = n/100*100;
        int num = front / f * f;
        if(num%100 != 0)
            num = num + f;
        int back = num - front;
        if(back/10 == 0){
            System.out.println("0"+back);
        }
        else{
            System.out.println(back);
        }
    }

}