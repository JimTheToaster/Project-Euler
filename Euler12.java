import java.util.*;
import java.lang.Math.*;
public class Euler12{
    public static void main(String[] args){                       
        long triNum = 0;
        for(int i = 1; true; i++){
            triNum += (long)i;
            if(getFactors(triNum) > 250) break;
        }
        System.out.println(triNum);
    }
    private static int getFactors(long x){
        int count = 0;
        int limit = ((int)Math.sqrt(x));
        for(int i = 1; i < limit; i++){
            if(x%i == 0) count++;
        }
        return count;
    }
}
