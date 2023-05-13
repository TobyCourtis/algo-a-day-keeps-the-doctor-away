function kangaroo(x1, v1, x2, v2) {
    // Write your code here
    let pos1 = x1;
    let pos2 = x2;
    let keepJumping = true;

    while (keepJumping === true) {
        pos1 += v1;
        pos2 += v2;
        if (pos1 === pos2) return 'YES'
        if (pos1 > pos2 || v2 >= v1) return 'NO'
    }
}