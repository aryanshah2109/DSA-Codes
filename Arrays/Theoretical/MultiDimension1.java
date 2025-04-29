package DSA.Arrays.Theoretical;
import java.util.Scanner;
public class MultiDimension1 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[][] arr = new int[4][4];

        int[][] arr2 = {{1,2,3},{4,5,6},{7,8,9}};

        System.out.println("Enter array elements: ");
        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < arr.length; j++) {
                arr[i][j] = sc.nextInt();
            }
        }

        System.out.println("Array elements: ");
        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < arr[0].length; j++) {
                System.out.print(arr[i][j]+" ");
            }
            System.out.println("");
        }
        sc.close();


        // the number of rows is mandatory to give
        // int[][] arr = new int[3][] is valid
        // int[][] arr = new int[][5] is invalid

    }
}
