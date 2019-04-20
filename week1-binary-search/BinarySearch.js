/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function (nums, target) {
    if (nums == null || nums.length == 0) return -1;
    let low = 0;
    let high = nums.length - 1;
    while (low <= high) {
        let mid = parseInt(low + (high - low) / 2);
        if (nums[mid] == target) {
            return mid;
        } else if (nums[mid] < target) {
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }
    return -1;

};
const nums = [-1, 0, 3, 5, 9, 12];
console.log(search(nums, 5));