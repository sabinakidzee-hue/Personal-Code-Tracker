// Write the recursive code of the following problems
//  Sum of n numbers;

public class assignment_2 {

    public static int sumOfNNumbers(int n) {
        if (n <= 0) {
            return 0;
        }
        return n + sumOfNNumbers(n - 1);
    }

    public static void main(String[] args) {
        int n = 5; 
        System.out.println("Sum of first " + n + " numbers is: " + sumOfNNumbers(n));
    }

    //  factorial of a number
    public static int factorial(int n) {
        if (n == 0) {
            return 1;
        }
        return n * factorial(n - 1);
    }
    //  Generating nth Fibonacci number
    public static int fibonacci(int n) {
        if (n <= 1) {
            return n;
        }
        return fibonacci(n - 1) + fibonacci(n - 2);
    }
    //  Linear search
    public static int linearSearch(int[] arr, int target, int index) {
        if (index >= arr.length) {
            return -1; // Target not found
        }
        if (arr[index] == target) {
            return index; // Target found
        }
        return linearSearch(arr, target, index + 1);
    }
    //  Binary search
    public static int binarySearch(int[] arr, int target, int left, int right) {
        if (left > right) {
            return -1; // Target not found
        }
        int mid = left + (right - left) / 2;
        if (arr[mid] == target) {
            return mid; // Target found
        }
        if (arr[mid] > target) {
            return binarySearch(arr, target, left, mid - 1);
        } else {
            return binarySearch(arr, target, mid + 1, right);
        } 
    }
}
