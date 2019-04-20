var searchRange = function(nums, target) {
    let low = 0;
    let high = nums.length -1;
    
    while(low +1 < high){
        let mid = low+(high-low)/2;
        if(nums[mid]< target){
            low = mid;
        }else{
            high = mid;
        }
    }
    return [low,high];
    
};
const nums = [5,7,7,8,8,10];
const target = 8 ;
console.log(searchRange(nums, target));
