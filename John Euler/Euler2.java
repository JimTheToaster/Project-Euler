import java.util.*;
public class Euler2{
    public static void main(String[] args){
        long total = 2;
        int num1 = 1;
        int num2 = 2;
        int holder;
        while(num2 <= 4000000){
            holder = num1;
            num1 = num2;
            num2 += holder;
            if((num2 % 2) == 0) total += num2;
        }
        System.out.println(total);
    }
}
