
/**
 * Definition for a binary tree node.
 */
function TreeNode(val) {
    this.val = val;
    this.left = this.right = null;
}

var isSymmetric = function (root) {
    if (!root) return true;
    return isMirror(root.left, root.right);

};

function isMirror(l, r) {
    var q1 = [l]; var q2 = [r];
    while (q1.length > 0 || q2.length > 0) {
        //dequeue
        var n1 = q1.shift(); var n2 = q2.shift();
        if (!n1 && !n2) {
            continue;
        }
        if (!n1 || !n2 || n1.val != n2.val) {
            return false;
        }
        q1.push(n1.left);
        q1.push(n1.right);
        q2.push(n2.right);
        q2.push(n2.left);
    }
    return true;
}