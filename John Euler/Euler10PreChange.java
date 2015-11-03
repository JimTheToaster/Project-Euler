import java.util.*;
import java.lang.Math.*;
public class Euler10PreChange{
    public static void main(String[] args){
        double holder = 0;
        for(long i = 2; i < 2000000; i++){
            System.out.println(i);
            if(getFactor(i) == 1) holder += i;
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