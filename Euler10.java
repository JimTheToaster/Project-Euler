import java.util.*;
import java.lang.Math.*;
public class Euler10{
    public static void main(String[] args){
        long holder = 0;
        final int limit = 2000000;
        boolean[] primeList = new boolean[limit];
        for(int i = 0; i < limit; i++) primeList[i] = true;
        primeList[0] = false;
        primeList[1] = false;
        int stop = (int)Math.sqrt(limit) + 1;
        for(int i = 2; i <= stop; i++){
            for(int j = 2*i; j < limit; j+= i) primeList[j] = false;
        }
        for(int i = 0; i < limit; i++){
            if(primeList[i])holder+= i;
        }
        System.out.println(holder);
    }
}
