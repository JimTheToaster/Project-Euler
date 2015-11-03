import java.util.*;
import java.lang.Math.*;
public class Euler7{
    public static void main(String[] args){
        long holder = 1;
        for(long i = 0; i <= 10001;){
            for(long j = 1; true; j++){
                if(getFactor(j) == 1){
                    i++;
                    System.out.println("Found prime #" + i + " at " + j);
                    holder = j;
                    if(i > 10001) break;
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
