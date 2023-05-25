import java.util.ArrayList;

public class validparanthesis {
    
}

class Solution {
    public boolean isValid(String s) {
        ArrayList<String> arr = new ArrayList<>();
        for (int i = 0; i < s.length(); ++i) {
            String t = s.substring(i,i+1);
            if (t.equals("(") || t.equals("{") || t.equals("[")) {
                arr.add(t);
            } else {
                if (arr.size()==0) return false;
                String popped = arr.remove(arr.size()-1);
                if (popped.equals("(") && !t.equals(")")) return false;
                else if (popped.equals("{") && !t.equals("}")) return false;
                else if (popped.equals("[") && !t.equals("]")) return false;
            }
        }
        return arr.size() == 0;
    }
}