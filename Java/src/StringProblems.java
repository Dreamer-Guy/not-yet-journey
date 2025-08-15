public class StringProblems {

    public int myAtoi(String s) {
//        url: https://leetcode.com/problems/string-to-integer-atoi/?envType=problem-list-v2&envId=string

        Boolean startNum=false;
        Boolean isPositive=true;
        s=s.trim();
        StringBuilder res= new StringBuilder();
        if(s.isEmpty()|| !Character.isDigit(s.charAt(0)) && s.charAt(0)!='-' && s.charAt(0)!='+'){
            return 0;
        }
        for(int i=0;i<s.length();++i){
            Character c=s.charAt(i);
            if(Character.isDigit(c)){
                startNum=true;
            }
            if(c.equals('-') && !startNum){
                isPositive=false;
            }
            if((c.equals('-') || c.equals('+')) && !startNum ){
                startNum=true;
                continue;
            }
            if(startNum && !Character.isDigit(c)){
                break;
            }
            res.append(s.charAt(i));
        }
        if(res.isEmpty()){
            return 0;
        }
        if(!isPositive){
            res.insert(0,'-');
        }
        int finalAnws=0;
        try{
            finalAnws=Integer.parseInt(res.toString());
        }
        catch (Exception e){
            if(isPositive){
                finalAnws=Integer.MAX_VALUE;
            }
            else {
                finalAnws=Integer.MIN_VALUE;
            }
        }
        return finalAnws;
    }

    public int lengthOfLongestSubstring(String s) {
        //url: https://leetcode.com/problems/longest-substring-without-repeating-characters/?envType=problem-list-v2&envId=string

        if(s.isEmpty()){
            return 0;
        }
        int size=s.length();
        int maxLength=-1;
        String current="";
        for(int j=0;j<size;++j){
            current="";
            for(int i=j;i<size;++i){
                char c=s.charAt(i);
                if(current.contains(""+c)){
                    if(current.length()>maxLength){
                        maxLength=current.length();
                    }
                    break;
                }
                current+=c;
            }
            if(current.length()>maxLength){
                maxLength=current.length();
            }
        }
        return maxLength;
    }
}
