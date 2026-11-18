class Solution {
public:
    int maxSubArray(vector<int>& nums){
        int currMax {};
        int max = nums[0];
        for (const auto num: nums){
            if (currMax < 0){
                currMax = 0;
            }
            currMax += num;
            max = std::max(max, currMax);
            }
        return max;
        } 
};