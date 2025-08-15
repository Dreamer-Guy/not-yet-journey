import java.util.Arrays;
import java.util.Collections;
import java.util.Map;

public class TwoPointersProblems {

    //url: https://leetcode.com/problems/longest-mountain-in-array/
    public int longestMountain(int[] arr) {
        int res=0;
        int n=arr.length;
        for(int i=1;i<n-1;++i){
            int l=i-1;
            int r=i+1;
            if(arr[l]>=arr[i] || arr[r]>=arr[i]){
                continue;
            }
            while(l>=0){
                if(arr[l]>=arr[l+1]){
                    break;
                }
                l--;
            }
            while(r<=n-1){
                if(arr[r]>=arr[r-1]){
                    break;
                }
                r++;
            }
            int len=r-l+1-2;
            if(len<3){
                len=0;
            }
            res= Math.max(res,len);
        }
        return res;
    }

    //url: https://leetcode.com/problems/string-compression/
    public int compress(char[] chars) {
        int n=chars.length;
        if(n==0){
            return 0;
        }
        int left=0;
        int right=0;
        int res_len=0;
        int index=0;
        while(left<=n-1){
            while(right<n && chars[right]==chars[left]){
                right+=1;
            }
            chars[index]=chars[left];
            index+=1;
            res_len+=1;
            int count=right-left+1-1;
            if(count>1){
                String countString=Integer.toString(count);
                res_len+=countString.length();
                for(int i=0;i<countString.length();++i){
                    chars[index]= countString.charAt(i);
                    index++;
                }
            }
            left=right;
        }
        return res_len;
    }


    private void reverse(int[]nums, int start,int e){
        while(start<e){
            int t=nums[start];
            nums[start]=nums[e];
            nums[e]=t;
            start++;
            e--;
        }
    }
    //url: https://leetcode.com/problems/rotate-array/description/
    public void rotate(int[] nums, int k) {
        int n=nums.length;
        k=k%n;
        if(n<=1){
            return;
        }
        reverse(nums,0,n-1);
        reverse(nums,0,k-1);
        reverse(nums,k,n-1);
    }
}
