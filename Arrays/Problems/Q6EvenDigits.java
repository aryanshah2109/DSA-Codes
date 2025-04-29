// Leetcode 1295
package DSA.Arrays.Problems;
import java.util.Scanner;
public class Q6EvenDigits {
    public static int findDigits(int n){
        int count = 0;
        while(n>0){
            n = n/10;
            count+=1;
        }
        return count;
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter number of elements: ");
        int n = sc.nextInt();
        int[] arr = new int[n];
        System.out.println("Enter array elements: ");
        for (int i = 0; i < arr.length; i++) {
            arr[i] = sc.nextInt();
        }
        int evenDigits = 0;
        for(int x:arr){
            if(findDigits(x) % 2 == 0){
                evenDigits++;
            }
        }
        System.out.println("No of elements with even digits: "+evenDigits);
    }
}
