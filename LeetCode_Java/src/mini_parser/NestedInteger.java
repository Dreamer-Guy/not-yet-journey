package mini_parser;


import java.util.List;

//url: https://leetcode.com/problems/mini-parser/submissions/1687923436/
public class NestedInteger {
    public NestedInteger(){

    }
    public NestedInteger(int value){

    }
    public boolean isInteger(){
        return true;
    }
    public Integer getInteger(){
        return 0;
    }
    public void setInteger(int value){

    }
    public void add(NestedInteger ni){

    }
    public List<NestedInteger> getList(){
        return List.of();
    }

    public NestedInteger deserialize(String s) {
        if(s==null || s.isEmpty()){
            return null;
        }
        if(Character.isDigit(s.charAt(0)) || s.charAt(0)=='-' || s.charAt(0)=='+'){
            return new NestedInteger(Integer.parseInt(s));
        }
        int n=s.length();
        NestedInteger parent=new NestedInteger();
        int flag=0;
        int start=1;
        for(int i=1;i<n-1;++i){
            if(s.charAt(i)=='['){
                flag+=1;
                continue;
            }
            if(s.charAt(i)==']'){
                flag-=1;
                continue;
            }
            if(s.charAt(i)==',' && flag==0){
                NestedInteger ele=deserialize(s.substring(start,i));
                if(ele!=null){
                    parent.add(ele);
                }
                start=i+1;
            }
        }
        NestedInteger lastEle=deserialize(s.substring(start,n-1));
        if(lastEle!=null){
            parent.add(lastEle);
        }
        return parent;
    }
}
