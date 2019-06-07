var searchMatrix = function (matrix, target) {
    if (matrix == null || matrix.length == 0) return false;

    const m = matrix.length;
    const n = matrix[0].length;
    let low = 0;
    let high = m * n - 1;

    while (low <= high) {
        let mid = parseInt(low + (high - low) / 2);
        let r = parseInt(mid / n);
        let c = parseInt(mid % n);
        if(matrix[r][c]<target){
            low = mid+1;
        }else if(matrix[r][c]>target){
            high = mid -1;
        }else{
            return true;
        }
    }
    return false;
}

const matrix = [
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 50]
]; const target = 13;

// const matrix = [
//     [1]
// ]; const target = 1;

// const matrix = [
//     [1,3,5]
// ]; const target = 1;
console.log(searchMatrix(matrix,target));