import java.util.*;
import java.lang.Math.*;
public class Euler9{
    public static void main(String[] args){
        double holder = 1;
        double c = 1;
        for(double a = 5; a <= 1000; a++){
            for(double b = 5; b <= 1000; b++){
                c = (double)Math.sqrt(((b*b)+(a*a)));
               double holder2 = a+b+c;
                if(Math.abs(1000-holder2) < .0001){
                    holder = a*b*c;
                    System.out.println(holder2);
                    System.out.println(a);
                    System.out.println(b);
                    System.out.println(c);
                    break;
                }
            }
            if(holder != 1) break;
        }
        System.out.println(holder);
    }
}
