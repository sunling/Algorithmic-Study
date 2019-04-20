var searchRange = function(nums, target) {
    const first = findFirst(nums,target);
    const last = findLast(nums,target);
    return [first,last];
    
};
function findFirst(nums, target){
    let low = 0;
    let high = nums.length -1; 
    while(low +1 < high){
        let mid = parseInt(low+(high-low)/2);
        if(nums[mid]< target){
            low = mid+1;
        }else{
            high = mid;
        } 
    }
    if(nums[low]==target){
        return low;
    } 
    if(nums[high]==target){
        return high;
    } 
    return -1; 
}

function findLast(nums, target){
    let low = 0;
    let high = nums.length -1; 
    while(low +1 < high){
        let mid = parseInt(low+(high-low)/2);
        if(nums[mid]<= target){
            low = mid;
        }else{
            high = mid-1;
        } 
    } 
    if(nums[high]==target){
        return high;
    } 
    if(nums[low]==target){
        return low;
    } 
    return -1; 
}

const nums = [5,7,7,8,8,10];
const target = 8 ;
console.log(searchRange(nums, target));
