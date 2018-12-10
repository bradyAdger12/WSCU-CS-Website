import java.util.*;

public class Main {
    public static void main(String[] args) {

        //declare and initialize ArrayList
        ArrayList<Integer> arr = new ArrayList<Integer>();

        //appends to the end of the array
        arr.add(5);
        arr.add(3);
        arr.add(7);

        System.out.println("Before clear: " + arr.size());

        //clear array
        arr.clear();

        System.out.println("After clear: " + arr.size());

    }
}
