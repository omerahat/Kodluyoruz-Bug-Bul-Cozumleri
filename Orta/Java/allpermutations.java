import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;

public class allpermutations {
    public static void main(String[] args) {
        findAllPermutations("aabb");
    }

    public static void findAllPermutations(String str){
        // Initialization
        
        String[] arr = str.split("");
        int[] iarr = new int[arr.length];
        ArrayList<int[]> allCombinations = allCombinations(iarr);
        ArrayList<String> res = new ArrayList<>();
        // for (int[] array : allCombinations) {
        //     printarr(array);
        // }
        // System.out.println(allCombinations.size());

        // Real Logic

        for (int[] combination : allCombinations) {
            String current = "";
            for (int i = 0; i < combination.length; ++i) {
                current += arr[combination[i]];
            }
            if (!res.contains(current)) res.add(current);
        }

        System.out.println(res);
    }
    public static ArrayList<int[]> allCombinations(int[] iarr) {
        ArrayList<int[]> res = new ArrayList<>();
        Arrays.fill(iarr, 0);
        while (!isAllFilled(iarr)) {
            int j = iarr.length - 1;
            ++iarr[j];
            while (j >= 0 && iarr[j] == iarr.length) {
                iarr[j] = 0;
                if (j - 1 >= 0) {
                    ++iarr[j - 1];
                }
                --j;
            }
            if (isValid(iarr)) res.add(iarr.clone());
        }
        return res;
    }
    public static boolean isAllFilled(int[] arr) {
        for (int i = 0; i < arr.length; ++i) {
            if (arr[i] != arr.length - 1) return false;
        }
        return true;
    }
    public static boolean isValid(int[] arr) {
        HashMap<Integer, Integer> frequency = new HashMap<>();
        
        for (int i = 0; i < arr.length; ++i) {
            frequency.putIfAbsent(arr[i],0);
            frequency.put(arr[i], frequency.get(arr[i]) + 1);
        }

        return frequency.keySet().size() == arr.length;
    }
    // *** HELPER FUNCTION ***
    public static void printarr(int[] arr) {
        for (int i = 0; i < arr.length; ++i) {
            System.out.print(arr[i] + (i-1 == arr.length ? "" : ", "));
        }
        System.out.println();
    }
}