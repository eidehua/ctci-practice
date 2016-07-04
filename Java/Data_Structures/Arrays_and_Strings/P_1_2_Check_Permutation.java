package Arrays_and_Strings;
import java.util.Hashtable;
// Things to keep in mind I forgot about:
    // for these permutations, do we care about case sensitivity? And what about whitespaces? Do not make hasty assumptions!

// Given two strings, write a method to decide if one is a permutation of the other
// Check if they are same length
public class P_1_2_Check_Permutation{

    public static void main(String[] args) {
        String a = "olehll";
        String b = "helllo";
        String c = "balrry";
        String d = "helll0";
        boolean result = false;
        result = checkPermutation(a,b);
        assert  result;
        result = checkPermutation(b, c);
        assert !result;
        result = checkPermutation(b,d);
        assert !result;
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

        System.out.println(counts);
        return true;
    }


// Runtime: O(n) loop through first string + O(n) loop through second string + O(n) verify hash table = O(n)
// Space complexity: O(n) extra space for the hash table
    // note of contention: is it really O(n) extra space for each hash table? There are only a limited number of characters (usually good assumption)
    // although in such the case, method 2 provides a much cleaner implementation

// Method 2: 
    // REMEMBER, REMEMBER!! Strings are made up of chars, and usually we don't deal with an INFINITE number of chars!!!
    // EG if the character set is just ASCII, then to keep track of counts like I did with the hashtable, we only need an array of size 128!
    // Solution from book:
    public static boolean permutation(String a, String b) {
        if (a.length() != b.length()) {
            return false;
        }

        int[] letters = new int[128]; // char set assumption

        char[] a_array = a.toCharArray();
        for(char c : a_array) { // count the number of each char in a
            letters[c]++;
        }

        for(int i = 0; i < b.length(); i++){
            int c = (int)  b.charAt(i);
            letters[c]--;
            if(letters[c]<0){
                return false;
            }
        }
        return true;
    }
    // Why does this work? We make very good use of the fact the strings are of the same size
    // So, if they are not permutations of each other this means: the second string has a letter the first does not have accounted for
    // which will force letters[c] to go below 0
    // and since the strings are of the same size, there will never be a case of "left over" aka slots of letters[c] that are above 0

    // Runtime: O(n)
    // Space complexity: O(1). Just needed an array of size 128, that's a constant size!

}