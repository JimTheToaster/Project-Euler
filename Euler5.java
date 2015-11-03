import java.util.*;
import java.lang.Math.*;
public class Euler5{
    public static void main(String[] args){
        long holder = 1;
        for(long i = 1; true; i++){
            for(long j = 1; j <= 20; j++){
                if((i%j) != 0) break;
                if(j == 20) holder = i;
            }
            if(holder != 1) break;
        }
        System.out.println(holder);
    }
}
