import java.util.*;
import java.lang.Math.*;
public class Euler3{
    public static void main(String[] args){
        long total = 600851475143L;
        long stop = (long)Math.sqrt(total);
        long holder = 1;
        for(long i = 1; i <= stop; i++){
            if(total%i == 0L){
                if(getFactor(i) == 1){
                    holder = i;
                }
            }
        }
        System.out.println(holder);
    }
    public static long getFactor(long l){
        long holder = 1;
        long stop = (long)Math.sqrt(l);
        for(long i = 1; i <= stop; i++){
            if(l%i == 0L) holder = i;
        }
        return holder;
    }
}
