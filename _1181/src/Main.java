import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int num = Integer.parseInt(br.readLine());
        ArrayList<String> words = new ArrayList<String>(50);

        for(int i = 0; i<num; i++){
            String word = br.readLine();
            words.add(word);
        }
        String tmp;
        for(int i=0; i<words.size(); i++){
            for(int j=i; j<words.size(); j++){
                if((words.get(i)).compareTo(words.get(j))>0){
                    tmp = words.get(i);
                    words.set(i,words.get(j));
                    words.set(j,tmp);
                }

                if((words.get(i)).length()>(words.get(j)).length()){
                    tmp = words.get(i);
                    words.set(i,words.get(j));
                    words.set(j,tmp);
                }

            }
        }
        System.out.println(words.get(0));
        for(int i = 1; i<words.size();i++){
            if(!((words.get(i)).equals(words.get(i-1)))){
                System.out.println(words.get(i));
            }
        }
    }
}