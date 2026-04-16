class Solution {
    public int lastStoneWeight(int[] stones) {
        // Max heap
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());
        
        // Add all stones
        for (int stone : stones) {
            maxHeap.add(stone);
        }
        
        // Smash until ≤ 1 stone remains
        while (maxHeap.size() > 1) {
            int y = maxHeap.poll(); // largest
            int x = maxHeap.poll(); // second largest
            
            if (y != x) {
                maxHeap.add(y - x);
            }
        }
        
        return maxHeap.isEmpty() ? 0 : maxHeap.poll();
    }
}