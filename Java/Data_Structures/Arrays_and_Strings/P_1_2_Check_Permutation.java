package Arrays_and_Strings;// Given two strings, write a method to decide if one is a permutation of the other
// Check if they are same length


import java.util.Hashtable;

public class P_1_2_Check_Permutation{

    public static void main(String[] args) {
        String a = "olehl";
        String b = "hello";
        String c = "barry";
        boolean result = false;
        result = checkPermutation(a,b);
        assert  result == true;
        result = checkPermutation(b, c);
        assert result == false;
    }

// Method 1: Hash Table
// Loop through the first string, and store all character counts into a hash map
// Make sure the second string matches the same counts

    public static boolean checkPermutation(String A, String B) {
        Hashtable<Character, Integer> counts = new Hashtable<Character, Integer>();
        if (A.length() != B.length()) {
            return false;
        }

        for (int i = 0; i < A.length(); i ++) {
            Character currChar = A.charAt(i);
            Integer currCount = counts.get(A.charAt(i));
            if (currCount == null) {
                counts.put(currChar, 1);
            }
            //currCount++;
            else {
                counts.put(currChar, ++currCount);
                System.out.println(currChar + " " + counts.get(currChar));
            }
        }

        for (int i = 0; i < B.length(); i ++) {
            Character currChar = B.charAt(i);
            Integer currCount = counts.get(B.charAt(i));
            if (currCount == null) {
                return false; // found a character in B that is not in A
            }
            if (currCount == 0) {
                return false; // B has a character more times than A
            }
            counts.put(currChar, --currCount);
        }
        // since A and B are the same size, passing the above two if checks means A and b are the same

        return true;
    }


// Runtime: O(n) loop through first string + O(n) loop through second string + O(n) verify hash table = O(n)
// Space complexity: O(n) extra space for the hash table

// Method 2: 


}