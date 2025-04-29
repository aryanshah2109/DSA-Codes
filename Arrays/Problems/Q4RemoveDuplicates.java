package DSA.Arrays.Problems;
import java.util.Scanner;
import java.util.Arrays;
import java.util.ArrayList;
public class Q4RemoveDuplicates {
    public static int[] removedDuplicates(int[] arr){
        int n = arr.length;
        int[] temp = new int[n];
        int j=0;
        for(int i=0;i<n-1;i++){
            if(arr[i]!=arr[i+1]){
                temp[j] = arr[i];
                j++;
            }
        }
        temp[j] = arr[n-1];
        j++;

        int[] result = new int[j];
        for(int i=0;i<j;i++){
            result[i] = temp[i];
        }
        return result;
        

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
        int[] removedDuplicates = removedDuplicates(arr);
        System.out.println("New array: "+Arrays.toString(removedDuplicates));
        sc.close();
    }
}
