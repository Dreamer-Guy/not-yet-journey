package classProblems;

import java.security.spec.PKCS8EncodedKeySpec;
import java.util.HashMap;
import java.util.Map;

//url: https://leetcode.com/problems/lru-cache/description/
public class LRUCache {
    public class Node{
        private Integer key;
        private Integer value;
        private Node previous;
        private Node next;

        public Node(Integer key,Integer val,Node pre,Node n){
            this.key=key;
            value=val;
            previous=pre;
            next=n;
        }
        public void setValue(Integer value){
            this.value=value;
        }
        public void setPrevious(Node n){
            previous=n;
        }
        public void setNext(Node n){
            next=n;
        }

        public void setKey(Integer key){
            this.key=key;
        }
        public Integer getKey(){
            return key;
        }
        public Integer getValue(){
            return value;
        }
        public Node getPrevious(){
            return previous;
        }
        public Node getNext(){
            return next;
        }
    }

    private Map<Integer,Node> map;
    private Node head;
    private Node tail;
    private final Integer capacity;

    private void updateTail(Node n){
        if(n==tail){
            return;
        }
        if(n==head){
            Node ne=n.getNext();
            ne.setPrevious(null);
            head=ne;

            n.setNext(null);
            n.setPrevious(tail);
            tail.setNext(n);
            tail=n;
            return;
        }
        Node pre=n.getPrevious();
        Node ne=n.getNext();
        pre.setNext(ne);
        ne.setPrevious(pre);
        n.setPrevious(tail);
        n.setNext(null);
        tail.setNext(n);
        tail=n;
    }
    public LRUCache(int capacity) {
        this.capacity=capacity;
        map=new HashMap<>();
        head=null;
        tail=null;
    }

    public int get(int key) {
        if(!map.containsKey(key)){
            return -1;
        }
        Node n=map.get(key);
        updateTail(n);
        return n.getValue();
    }

    public void put(int key, int value) {
        if(map.containsKey(key)){
            map.get(key).setValue(value);
            updateTail(map.get(key));
            return;
        }
        if(head==null){
            Node n=new Node(key,value,null,null);
            head=n;
            tail=n;
            map.put(key,n);
            return;
        }
        Node n=new Node(key,value,tail,null);
        tail.setNext(n);
        tail=n;
        map.put(key,n);
        if(map.size()>capacity){
            Node newHead=head.getNext();
            newHead.setPrevious(null);
            map.remove(head.getKey());
            head=newHead;
        }
    }
}
