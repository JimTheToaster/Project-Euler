import java.util.*;
import java.lang.Math.*;
public class Euler14{
    public static void main(String[] args){
        long lC = 0; //Longest chain
        long lcn = 0; //Number for longest chain
        long cC = 0; //Current chain
        for(long i = 2; i < 1000000; i++){
            cC = chain(i);
            if(cC > lC){
                lC = cC;
                lcn = i;
            }
        }
        System.out.println(lcn);
    }
    private static long chain(long n){
        long count = 0;
        while(n > 1){
            if(n%2 == 0) n /= 2;
            else n = (3*n) + 1;
            count++;
        }
        return count;
    }
}