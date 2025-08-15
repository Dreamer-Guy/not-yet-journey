import java.beans.PropertyEditorSupport;
import java.util.*;
import java.util.stream.Collectors;

public class SlidingWindowProblems {

    //url: https://leetcode.com/problems/repeated-dna-sequences/submissions/1653795783/
    public List<String> findRepeatedDnaSequences(String s) {
        if(s.length()<=10){
            return List.of();
        }
        Map<String,Integer> map=new HashMap<>();
        Integer DNA_LENGTH=10;
        int n=s.length();
        String current=s.substring(0,DNA_LENGTH);
        map.put(current,1);
        for(int i=1;i<=n-DNA_LENGTH;++i){
//            current=s.substring(i,i+DNA_LENGTH);
            current=current.substring(1)+s.charAt(i+DNA_LENGTH-1);
            if(map.containsKey(current)){
                map.put(current,map.get(current)+1);
            }
            else{
                map.put(current,1);
            }
        }
        List<String> res=new ArrayList<>();
        for(String key:map.keySet()){
            if(map.get(key)>1){
                res.add(key);
            }
        }
        return res;
    }

    //url: https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/
    public int longestSubstring(String s, int k) {
        if(s==null || s.isEmpty() || s.length()<k){
            return 0;
        }
        int[]alphabet=new int[26];
        int n=s.length();
        for(int i=0;i<n;++i){
            int index=s.charAt(i)-'a';
            alphabet[index]+=1;
        }
        Boolean isValidString=true;
        for(int i=0;i<26;++i){
            if(alphabet[i]>0 && alphabet[i]<k){
                isValidString=false;
                break;
            }
        }
        if(isValidString){
            return n;
        }
        int res=0;
        int start=0;
        for(int i=0;i<n;++i){
            int count=alphabet[s.charAt(i)-'a'];
            if(count>0 && count<k){
                String currentString=s.substring(start,i);
                res=Math.max(res,longestSubstring(currentString,k));
                start=i+1;
            }
        }
        res=Math.max(res,longestSubstring(s.substring(start),k));
        return res;
    }

    //url: https://leetcode.com/problems/find-all-anagrams-in-a-string/
    private boolean isAnagrams(String s,int[] lettersP){
        int n=s.length();
        int[] lettersS=new int[26];
        for(int i=0;i<n;++i){
            lettersS[s.charAt(i)-'a']+=1;
        }
        for(int i=0;i<26;++i){
            if(lettersP[i]!=lettersS[i]){
                return false;
            }
        }
        return true;
    }
    public List<Integer> findAnagrams(String s, String p) {
        int n=s.length();
        int n1=p.length();
        int[] lettersP=new int[26];
        for(int i=0;i<n1;++i){
            int index=p.charAt(i)-'a';
            lettersP[index]+=1;
        }
        List<Integer>res=new ArrayList<>();
        for(int i=0;i<=n-n1;i+=1){
            String current=s.substring(i,i+n1);
            if(isAnagrams(current,lettersP)){
                res.add(i);
            }
        }
        return res;
    }

    //url: https://leetcode.com/problems/subarray-product-less-than-k/description/
    public int resolve(int[]nums,int index,int k){
        if(index>=nums.length){
            return 0;
        }
        int count=0;
        int product=1;
        for(int i=index;i<nums.length;++i){
            product*=nums[i];
            if(product>=k){
                break;
            }
            count+=1;
        }
        return count+resolve(nums,index+1,k);

    }
    public int numSubarrayProductLessThanK(int[] nums, int k) {
        return resolve(nums,0,k);
    }

    //url: https://leetcode.com/problems/find-k-closest-elements/description/
    public List<Integer> findClosestElements(int[] arr, int k, int x) {
        int n=arr.length;
        if(k>=n){
            return Arrays.stream(arr).boxed().toList();
        }
        if(x<=arr[0]){
            return Arrays.stream(Arrays.copyOfRange(arr,0,k)).boxed().toList();
        }
        if(x>=arr[n-1]){
            return Arrays.stream(Arrays.copyOfRange(arr,n-k,n)).boxed().toList();
        }
        int left=0;
        int right=0;
        for(int i=0;i<n;++i){
            if(arr[i]>x){
                left=i-1;
                right=i;
                break;
            }
            if(arr[i]==x){
                int distance_left=Math.abs(arr[i]-arr[i-1]);
                int distance_right=Math.abs(arr[i+1]-arr[i]);
                if(distance_left<=distance_right){
                    left=i-1;
                    right=i;
                }
                else {
                    left=i;
                    right=i+1;
                }
                break;
            }
        }
        int count=0;
        List<Integer> res=new ArrayList<>();
        while(count<k){
            if(left<0){
                res.add(arr[right]);
                right+=1;
                count+=1;
                continue;
            }
            if(right>n-1){
                res.add(arr[left]);
                left-=1;
                count+=1;
                continue;
            }
            int distance_left=Math.abs(x-arr[left]);
            int distance_right=Math.abs(x-arr[right]);
            if(distance_left<=distance_right){
                res.add(arr[left]);
                left-=1;
            }
            else {
                res.add(arr[right]);
                right+=1;
            }
            count++;
        }
        return res.stream().sorted().toList();
    }

    //url: https://leetcode.com/problems/longest-repeating-character-replacement/
    public int characterReplacement(String s, int k) {
        if(s.isEmpty()||s==null){
            return 0;
        }
        int n=s.length();
        if(k>=n){
            return n;
        }
        int max=0;
        int res=0;
        int l=0;
        int r=0;
        int[] countLetters=new int[26];
        for(;r<n;++r){
            countLetters[s.charAt(r)-'A']++;
            max=Arrays.stream(countLetters).max().getAsInt();
            int count=r-l+1-max;
            if(count<=k){
                res=Math.max(res,r-l+1);
            }
            else{
                countLetters[s.charAt(l)-'A']--;
                l++;
            }
        }
        return res;
    }

    //url: https://leetcode.com/problems/max-consecutive-ones-iii/description/
    public int longestOnes(int[] nums, int k) {
        int n=nums.length;
        int left=0;
        int right=0;
        int res=0;
        int[] counts=new int[2];
        for(;right<n;++right){
            counts[nums[right]]+=1;
            if(counts[0]<=k){
                res=Math.max(res,right-left+1);
            }
            else{
                counts[nums[left]]-=1;
                left+=1;
            }
        }
        return res;
    }
}

