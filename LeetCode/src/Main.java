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

        int[]arr=new int[]{2,3,1,1,4};
        int k=3;

        String s="9801982396";
        var t=anonymousProblems.isAdditiveNumber(s);
        System.out.println(t);
    }
}