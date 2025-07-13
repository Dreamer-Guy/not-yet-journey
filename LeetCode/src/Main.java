import classProblems.LRUCache;

import javax.swing.*;
import java.util.List;

public class Main {

    public static void main(String[] args) {
        StringProblems stringProblems=new StringProblems();
        SlidingWindowProblems slidingWindowProblems=new SlidingWindowProblems();
        TwoPointersProblems twoPointersProblems=new TwoPointersProblems();
        BinarySearch binarySearch=new BinarySearch();
        AnonymousProblems anonymousProblems=new AnonymousProblems();
        LRUCache lruCache=new LRUCache(2);

        int[]a=new int[]{0,1,2,5};
        int k=3;

        String[] strs = {"10", "0001", "111001", "1", "0"};
        int m=5;
        int n=3;
        var t= anonymousProblems.permute(a);
        System.out.println(t.size());
    }
}