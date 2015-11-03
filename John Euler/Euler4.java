import java.util.*;
import java.lang.Math.*;
public class Euler4{
    public static void main(String[] args){
        long holder = 1, holder2 = 1, holder3 = 1;
        long multiple;
        long[] digits = new long[6];
        for(int i = 0; i < 6; i++) digits[i] = 0;
        for(long i = 100; i < 1000; i++){
            for(long j = 100; j < 1000; j++){
                multiple = j*i;
                for(int x = 0; x < 6; x++){
                    digits[x] = multiple % 10;
                    multiple/=10;
                }
                multiple = j*i;
                if(digits[0] == digits[5] && digits[1] == digits[4] && digits[2] == digits[3] && multiple > holder){
                    holder = j*i;
                    holder2 = j;
                    holder3 = i;
                }
            }
        }
        System.out.println(holder);
        System.out.println(holder2);
        System.out.println(holder3);
    }
}
