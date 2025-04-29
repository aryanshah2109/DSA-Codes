package DSA.Arrays.Theoretical;
import java.util.Scanner;
import java.util.Arrays;
public class PassToFunction{
    public static void change(int[] arr){
        arr[3] = 4;
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] arr = new int[6];
        System.out.println("Enter array elements: ");
        for(int i=0;i<arr.length;i++){
            arr[i] = sc.nextInt();
        }
        System.out.println(Arrays.toString(arr));
        change(arr);
        System.out.println(Arrays.toString(arr));
        sc.close();
    }
}











