public class BinarySearch {
    private Boolean isPossibleToSplit(int[]nums,int k,int maximum){
        int n=nums.length;
        int index=0;
        for(int i=0;i<k-1;++i){
            int sum=0;
            while(sum+nums[index]<=maximum){
                sum+=nums[index];
                index++;
                if(index>n-1){
                    return true;
                }
            }
        }
        int sum=0;
        for(int i=index;i<n;++i){
            sum+=nums[i];
        }
        return sum <= maximum;
    }
    //url: https://leetcode.com/problems/split-array-largest-sum/description/
    //key: the answer lie between max element and sum of array
    public int splitArray(int[] nums, int k) {
        int start=0;
        int end=0;
        for(int num:nums){
            start=Math.max(start,num);
            end+=num;
        }
        int total=end;
        while(start<end){
            int m=(start+end)/2;
            if(isPossibleToSplit(nums,k,m)){
                end=m;
                continue;
            }
            start=m+1;
        }
        return start;
    }


    private Long power(Long a,Long b){
        Long cur=1L;
        for(Long i=1L;i<=b;++i){
            cur=cur*a;
        }
        return cur;
    }
    private Boolean isAGoodBase(Long n,Long base){
        Long sum=1L;
        Long exponent=1L;
        while(sum<n){
            sum+=power(base,exponent);
            exponent+=1;
            if(sum.equals(n)){
                return true;
            }
        }
        return false;
    }
    //url: https://leetcode.com/problems/smallest-good-base/
    public String smallestGoodBase(String n) {
        Long start=1L;
        Long end=Long.parseLong(n);
        Long num=Long.parseLong(n);
        while(start<end){
            Long m=(start+end)/2;
            if(isAGoodBase(num,m)){
                end=m;
                continue;
            }
            start=m+1;
        }
        return String.valueOf(start);
    }

}
