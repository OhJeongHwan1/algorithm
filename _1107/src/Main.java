import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws Exception {

        Scanner sc = new Scanner(System.in);

        int start = 100;
        int clicks_1;
        int goal = sc.nextInt();
        int real_goal = goal;
        int num_error = sc.nextInt();
        ArrayList<Integer> error_numbers = new ArrayList<>(10);
        ArrayList<Integer> mins = new ArrayList<>(3);
        for(int i=0; i<10; i++){
            error_numbers.add(-1);
        }
        for(int i=0; i<num_error; i++){
            int error_number = sc.nextInt();
            for(int j =0; j<10; j++) {
                if (j == error_number) {
                    error_numbers.set(j, error_number);
                }
            }
        }
        //이 아래는 자리수 구해내는 알고리즘 이여
        int size = goal;
        int real_size = 0;  // 자리수 나타내는 것
        while(size != 0){
            size = size/10;
            real_size++;
        }

        clicks_1 = Math.abs(start-goal); //그냥 +,- 조절로 도달할 수 있는 횟수
        mins.add(clicks_1);
        ArrayList<Integer> all_numbers = new ArrayList<>(10);
        for(int i=0; i<10; i++){
            all_numbers.add(i);
        }
        for(int i=0; i<10; i++){     // 여기를 거친 후에 all_numbers 에는 살아있는 버튼만이 남아있음.
            if(error_numbers.get(i) != -1){
                all_numbers.set(i,-1);
            }
        }
        ArrayList<Integer> bests = new ArrayList<>(6);
        ArrayList<Integer> tmp = new ArrayList<>(10);
        for(int i=0; i<10; i++){
            tmp.add(0);
        }
        int clicks_2 = 0;
        int best = 0;
        for(int i = real_size; i>0; i--){
            int min = 500000;
            for(int j = 0; j <10; j++){
                tmp.set(j,(int)(all_numbers.get(j)*Math.pow(10,i-1)));
                if(goal <= 0) break;
                if((int)(goal/Math.pow(10,i-1)) == all_numbers.get(j)){
                    best = j;
                    break;
                }
                else if(Math.abs(tmp.get(j)-goal) < min){
                    min = Math.abs(tmp.get(j)-goal);
                    best = j;
                }
            }
            if(goal > 0){
                bests.add(best);
            }
            else if(goal <= 0 && all_numbers.get(0) != 0){
                for(int k =0; k<10; k++){
                    if(all_numbers.get(k) >0){
                        bests.add(all_numbers.get(k));
                        break;
                    }
                }
            }
            goal = goal-(best*(int)Math.pow(10,i-1));
            clicks_2++;
        }
        int guess = 0;
        for(int i = real_size; i>0; i--){
            guess = guess + bests.get(real_size-i)*(int)Math.pow(10,i-1);
        }
        clicks_2 = clicks_2 + Math.abs(real_goal-guess);
        mins.add(clicks_2);
        int clicks_3 = 0;
        ArrayList<Integer> bests2 = new ArrayList<>(6);
        for(int i = 0; i<real_size-1; i++){
            for(int k = 9 ; k>=0; k--){
                if(all_numbers.get(k) >0){
                    bests2.add(all_numbers.get(k));
                    clicks_3++;
                    break;
                }
            }
        }
        int guess2 = 0;
        for(int i = real_size-1; i>0; i--){
            guess2 = guess2 + bests2.get(real_size-1-i)*(int)Math.pow(10,i-1);
        }
        clicks_3 = clicks_3 + Math.abs(real_goal-guess2);
        mins.add(clicks_3);
        System.out.println(Collections.min(mins));
    }
}