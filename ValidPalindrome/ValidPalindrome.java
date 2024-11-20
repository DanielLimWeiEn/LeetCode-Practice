public class Solution {
    public boolean isPalindrome(String s) {
        String sWithoutSpaces = s.replaceAll("\\W", "").replaceAll("\\_", "").toLowerCase();

        int p1 = 0;
        int p2 = sWithoutSpaces.length() - 1;

        while (p1 < p2) {
            if (sWithoutSpaces.charAt(p1) == sWithoutSpaces.charAt(p2)) {
                p1++;
                p2--;
            } else {
                return false;
            }
        }

        return true;
    }
}
