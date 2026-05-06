// Question number: 9
// Level: easy
// Author: Naama Tzadok
// Date: Jan 23, 2025 00:46


class Solution {
    public boolean isPalindrome(int x) {
        if(x < 0){ 
            return false;
        }
        int y = x;
        int num = 0;
        int curent = 0;

        while(x != 0){
            curent = x%10;
            num = num*10 + curent;
            x = x/10;
        }
        if(num == y)
            return true;
        return false;
        
    }
}

// Time Complexity: O(log n)
// Space Complexity: O(1)