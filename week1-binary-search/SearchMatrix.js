var searchMatrix = function (matrix, target) {
    if (matrix == null || matrix.length == 0) return false;
    const m = matrix.length;
    const n = matrix[0].length;
    let row = 0;
    while (row < m) {
        if (matrix[row][n - 1] > target) {
            let low = 0;
            let high = n -1;
            while (low <= high) {
                let mid = parseInt(low + (high - low) / 2);
                if (matrix[row][mid] < target) {
                    low = mid + 1;
                } else if (matrix[row][mid] > target) {
                    high = mid - 1;
                } else {
                    return true;
                }
            }
            return false;
        }else if(matrix[row][n - 1] == target){
            return true;
        } else {
            row++;
        }
    }
    return false;
};
// const matrix = [
//     [1, 3, 5, 7],
//     [10, 11, 16, 20],
//     [23, 30, 34, 50]
// ]; const target = 13;

// const matrix = [
//     [1]
// ]; const target = 1;

const matrix = [
    [1,3,5]
]; const target = 1;
console.log(searchMatrix(matrix,target));

