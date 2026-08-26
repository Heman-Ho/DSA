class Solution {
public:
    bool canReach(string s, int minJump, int maxJump) {
        int n = s.length();

        if (s[n-1] == '1') {
            return false;
        }

        std::vector<bool> dp(n, false);
        dp[0] = true;

        int reachable_in_window = 0;

        for (int i = 1; i < n; ++i){
            // Expand the window and add index that is exactly minjump steps behind 
            if ( i >= minJump && dp[i - minJump]) {
                reachable_in_window ++;
            }
            // shrink the window 
            if (i > maxJump && dp[i - maxJump - 1]) {
                reachable_in_window --;
            }
            // if there's a valid starting point in the window, then we can land here
            if (reachable_in_window > 0 && s[i] == '0'){
                dp[i] = true;
            }

        }

        return dp[n-1];
    }
};