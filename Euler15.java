import java.util.*;
import java.lang.Math.*;
public class Euler15{
    static long answer = 0;
    public static void main(String[] args){
        short x = 20, y = 20, x2 = 0, y2 = 0;
        recursive(x2, y2, x, y);
        System.out.println(answer);
    }
    private static void recursive(short x, short y, short xMax, short yMax){
        if(x == xMax || y == yMax) answer ++;
        else{
            recursive((short)(x+1), y, xMax, yMax);
            recursive(x, (short)(y+1), xMax, yMax);
        }
    }
}
