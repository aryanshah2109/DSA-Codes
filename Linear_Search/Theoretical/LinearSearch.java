package DSA.Linear_Search.Theoretical;
import java.util.Scanner;
import java.util.Arrays;

public class LinearSearch {
    public static int linearSearch(int[] arr,int element){
        if(arr.length == 0) return -2;
        for(int i=0;i<arr.length;i++) if(arr[i] == element) return i;
        return -1;
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter size of array: ");
        int n = sc.nextInt();
        int[] arr = new int[n];
        System.out.println("\nEnter array elements: ");
        for (int i = 0; i < arr.length; i++) {
            arr[i] = sc.nextInt();
        }
        System.out.println("\nEnter element to search: ");
        int element = sc.nextInt();
        int key = linearSearch(arr,element);
        if(key == -2) System.out.println("Empty array");
        else if(key == -1) System.out.println("Element not found");
        else System.out.println("Element " + element +" found at index "+key);
    }
}
