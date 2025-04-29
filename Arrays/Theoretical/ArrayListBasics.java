package DSA.Arrays.Theoretical;
import java.util.Scanner;
import java.util.ArrayList;

public class ArrayListBasics {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        ArrayList<Integer> list = new ArrayList<>(3);   
        // 3 is the initial size which can be varied
        System.out.println(list);   // currently empty

        // add elements
        list.add(4);
        list.add(3);
        list.add(6);
        list.add(11);
        list.add(14);
        // add at a particular index
        list.add(5,100);
        System.out.println(list);

        // remove elements by giving their indices
        list.remove(3); //removes element at index 3
        System.out.println(list);

        // remove element by converting the desired element into object
        list.remove(Integer.valueOf(14));
        System.out.println(list);

        list.add(44);
        list.add(13);
        list.add(16);
        list.add(21);
        list.add(24);
        System.out.println(list);
        // get size of list
        System.out.println("Size of list: "+list.size());

        // get element at given indice
        System.out.println("Element at index 4: "+list.get(4));

        // returns boolean to check if element is present in list
        System.out.println("Does list contain 3: "+list.contains(3));
        System.out.println("Does list contain 99: "+list.contains(99));

        list.set(1,150);    // diff bw set and add is set can update value but add cannot
        System.out.println(list);
        System.out.println("Index of element 100: "+list.indexOf(100));
        
    }
}
