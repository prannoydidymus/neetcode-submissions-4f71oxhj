class Solution {
    public boolean isHappy(int n) {
while(n>9){
    int sum = 0;
    while(n >0){
        sum += Math.pow(n%10,2);
        n /= 10;
    }
    n = sum;
}
if(n == 1 || n == 7){
    return true;
}
else{
    return false;
}
}
}
