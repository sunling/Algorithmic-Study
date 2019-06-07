var findPeakElement = function (nums) {
    if (nums.length == 1) {
        return 0;
    }
    let low = 0;
    let high = nums.length - 1;
    while (low + 1 < high) {
        let mid = parseInt(low + (high - low) / 2);
        //peak
        if (nums[mid] > nums[mid - 1] && nums[mid] > nums[mid + 1]) {
            return mid;
        }
        //increasing
        if (nums[mid] > nums[mid - 1] && nums[mid] < nums[mid + 1]) {
            low = mid;
        }
        //decreasing
        if (nums[mid] < nums[mid - 1] && nums[mid] > nums[mid + 1]) {
            high = mid;
        }
        //increasing
        if (nums[mid-1] > nums[mid] && nums[mid] < nums[mid + 1]) {
            low = mid;
        }
    }
    return nums[high] < nums[low] ? low : high;
};

//const nums = [1, 2, 3, 1];
//const nums = [1,2,1,3,5,6,4];
const nums = [1];
console.log(findPeakElement(nums));