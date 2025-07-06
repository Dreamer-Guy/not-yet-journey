import java.util.*;

public class AnonymousProblems {
    //url: https://leetcode.com/problems/zigzag-conversion/description/
    public String convert(String s, int numRows) {
        if(numRows==1){
            return s;
        }
        Integer t=1;
        Boolean isDown=true;
        Map<Integer,String> map=new HashMap<>();
        for(int i=1;i<=numRows;++i){
            map.put(i,"");
        }
        int n=s.length();
        for(int i=0;i<n;++i){
            String oldString=map.get(t);
            String newString=oldString+s.charAt(i);
            map.put(t,newString);
            if(isDown){
                t++;
                if(t>numRows){
                    t-=2;
                    isDown=false;
                }
            }
            else {
                t--;
                if(t<1){
                    t+=2;
                    isDown=true;
                }
            }
        }
        String res="";
        for(Integer key:map.keySet()){
            res+=map.get(key);
        }
        return res;
    }

    //url: https://leetcode.com/problems/jump-game/description/
    public boolean canJump(int[] nums) {
        int max=nums[0];
        int n=nums.length;
        for(int i=1;i<n;++i){
            if(i<=max){
                max=Math.max(max,i+nums[i]);
            }
        }
        return max>=(n-1);
    }

    //url: https://leetcode.com/problems/jump-game-ii/
    public int jump(int[] nums) {
        int n=nums.length;
        int[] count=new int[n];
        for(int i=0;i<n;++i){
            count[i]=Integer.MAX_VALUE;
        }
        count[0]=0;
        for(int i=0;i<n;++i){
            int t=nums[i];
            for(int j=1;j<=t && i+j<=n-1;j++){
                count[i+j]=Math.min(count[i+j],count[i]+1);
            }
        }
        return count[n-1];
    }

    //url: https://leetcode.com/problems/remove-duplicate-letters/
    public String removeDuplicateLetters(String s) {
        int n=s.length();
        int[]lastIndex=new int[26];
        boolean[]seen=new boolean[26];
        for(int i=0;i<n;++i){
            lastIndex[s.charAt(i)-'a']=i;
        }
        Stack<Integer> st=new Stack<>();
        for(int i=0;i<n;++i){
            if(seen[s.charAt(i)-'a']){
                continue;
            }
            if(st.isEmpty()){
                seen[s.charAt(i)-'a']=true;
                st.push(s.charAt(i)-'a');
                continue;
            }
            while(!st.isEmpty() && lastIndex[st.peek()]>i && st.peek()>s.charAt(i)-'a'){
                seen[st.pop()]=false;
            }
            st.push(s.charAt(i)-'a');
            seen[s.charAt(i)-'a']=true;
        }
        StringBuilder stringBuilder=new StringBuilder();
        while(!st.isEmpty()){
            stringBuilder.append((char)('a'+st.pop()));
        }
        return stringBuilder.reverse().toString();
    }

    //url: https://leetcode.com/problems/bulls-and-cows/description/
    public String getHint(String secret, String guess) {
        int[] numsSec=new int[10];
        int[] numsGuess=new int[10];
        int bull=0;
        int n=secret.length();
        for(int i=0;i<n;++i){
            if(secret.charAt(i)==guess.charAt(i)){
                bull+=1;
            }
            numsSec[secret.charAt(i)-'0']+=1;
            numsGuess[guess.charAt(i)-'0']+=1;
        }
        int cow=0;
        for(int i=0;i<10;++i){
            cow+=(Math.min(numsSec[i],numsGuess[i]));
        }
        cow-=bull;
        return String.format("%dA%dB",bull,cow);
    }

    //url: https://leetcode.com/problems/longest-increasing-subsequence/description/
    public int lengthOfLIS(int[] nums) {
        List<Integer> l=new ArrayList<>();
        int n=nums.length;
        for(int i=0;i<n;++i){
            if(l.isEmpty() || nums[i]>l.getLast()){
                l.add(nums[i]);
                continue;
            }
            for(int j=0;j<l.size();++j){
                if(nums[i]<=l.get(j)){
                    l.set(j,nums[i]);
                    break;
                }
            }
        }
        return l.size();
    }

    private Boolean isPossibleToFormAdditive(String s,
                                             long first,long second,int start){
        if(start>=s.length()){
            return true;
        }
        String sum=String.valueOf(first+second);
        int n=sum.length();
        for(int i=0;i<n;++i){
            if(start+i>=s.length() || sum.charAt(i)!=s.charAt(start+i)){
                return false;
            }
        }
        return isPossibleToFormAdditive(s,second,Long.parseLong(sum),start+n);
    }
    //url: https://leetcode.com/problems/additive-number/
    public boolean isAdditiveNumber(String num) {
        int n=num.length();
        for(int i=1;i<=n/2;++i){
            for(int j=1;j<=n/2;++j){
                if(i+j>=n){
                    continue;
                }
                String firstString=num.substring(0,i);
                String secondString=num.substring(i,i+j);
                if((firstString.charAt(0)=='0' && firstString.length()>1)
                        || (secondString.charAt(0)=='0' && secondString.length()>1)){
                    continue;
                }
                Long first=Long.parseLong(firstString);
                Long second=Long.parseLong(secondString);
                int start=i+j;
                if(isPossibleToFormAdditive(num,first,second,start)){
                    return true;
                }
            }
        }
        return false;
    }
    
}
