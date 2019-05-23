import java.io.*;
import java.math.*;
import java.text.*;
import java.util.*;
import java.util.regex.*;

public class plusMinus {

    /*
     * Complete the plusMinus function below.
     */
    static void plusMinus(int[] arr) {
        float neg = 0, pos = 0, zeros = 0, len = arr.length;

        for(int i= 0; i<len ;i++){
            if(arr[i]<0){
                neg++;
            }
            else if(arr[i]>0){
                pos++;
            }
            else if (arr[i] == 0){
                zeros++;
            }
        }
        System.out.println(pos/len);
        System.out.println(neg/len);
        System.out.println(zeros/len);
    }

    private static final Scanner scan = new Scanner(System.in);

    public static void main(String[] args) {
        int n = Integer.parseInt(scan.nextLine().trim());

        int[] arr = new int[n];

        String[] arrItems = scan.nextLine().split(" ");

        for (int arrItr = 0; arrItr < n; arrItr++) {
            int arrItem = Integer.parseInt(arrItems[arrItr].trim());
            arr[arrItr] = arrItem;
        }

        plusMinus(arr);
    }
}
