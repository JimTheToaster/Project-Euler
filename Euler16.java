import java.util.*;
import java.lang.Math.*;
import java.math.BigInteger;
public class Euler16{
    static int answer = 0;
    public static void main(String[] args){
        String bigNum = BigInteger.valueOf(2).pow(1000).toString();
        for(int i = 0; i < bigNum.length(); i++){
            answer += Integer.parseInt(bigNum.substring(i, i+1));
        }
        System.out.println(answer);
    }
}
