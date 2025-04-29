package DSA.Arrays.Problems;
import java.util.Scanner;
import java.util.Arrays;
public class Q3CheckIfSorted {
    public static boolean checkSorted(int[] arr){
        int n = arr.length;
        for(int i=1;i<n;i++){
            if(arr[i-1]>arr[i]) return false;
        }
        return true;
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter number of elements: ");
        int n = sc.nextInt();
        int[] arr = new int[n];
        System.out.println("Enter array elements: ");
        for(int i=0;i<n;i++){
            arr[i] = sc.nextInt();
        }
        if(checkSorted(arr)) System.out.println("Array is sorted");
        else  System.out.println("Array is unsorted");
        sc.close();
    }
}
