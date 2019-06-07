/**
 * @param {number[]} nums
 * @return {number}
 */
var findMin = function (nums) {
    if (nums == null || nums.length == 0) return null;
    if (nums.length == 1) return nums[0];
    let low = 0;
    let high = nums.length - 1;
    while (low + 1 < high) {
        let mid = parseInt(low + (high - low) / 2);
        if(nums[mid] > nums[high]){ 
            low = mid; //right part 
        }else{ 
            high = mid;//left part
        } 
    }
    return nums[low] < nums[high] ? nums[low] : nums[high];
};

//in the worst case, it is O(n)
var findMin1 = function(nums) {
    var target = nums[nums.length-1];
    for(var i = 0; i< nums.length; i++){
        if(nums[i]<=target){
            return nums[i];
        }
    }
};
const nums = [4,5,6,7,0,1,2];
//const nums = [2, 1];
//const nums = [3,1,2];
//const nums = [5,1,2,3,4];
//const nums = [3,4,5,1,2];
//const nums = [2,3,4,5,1];
console.log(findMin(nums));