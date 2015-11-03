import java.util.*;
import java.lang.Math.*;
public class Euler6{
    public static void main(String[] args){
        long holder = 0;
        long holder2 = 0;
        for(long i = 1; i <= 100; i++){
            holder += (i*i);
        }
        for(long i = 1; i <= 100; i++){
            holder2 += (i);
        }
        holder2 *= holder2;
        System.out.println(holder2 - holder);
    }
}
