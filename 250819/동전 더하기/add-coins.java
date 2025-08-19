import java.util.Scanner;
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();
        int count = 0;
        ArrayList<Integer> arr = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            int v = sc.nextInt();
            arr.add(v);
        }

        Collections.reverse(arr);
        for (int v : arr) {
            while (k - v >= 0) {
                k -= v;
                count++;
            }
        }

        System.out.println(count);
    }
}