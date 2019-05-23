import java.io.*;
import java.math.*;
import java.text.*;
import java.util.*;
import java.util.regex.*;

public class staircase {

    /*
     * Complete the staircase function below.
     */
    static void staircase(int n) {
        for (int i = 0; i<n ; i++){
            for(int z = n; z-1>i ; z--){
                System.out.print(" ");
            }
            for(int j = 0; j<= i; j++){
                System.out.print("#");
            }
            System.out.println();
        }

    }

    private static final Scanner scan = new Scanner(System.in);

    public static void main(String[] args) {
        int n = Integer.parseInt(scan.nextLine().trim());

        staircase(n);
    }
}
