function getMaxLessThanK(n, k) {
    // if k or k minus 1 is greater than n, we use our ternary
    // to return k minus 2, else we return k minus 1
    return ((k | (k - 1)) > n) ? (k - 2) : (k - 1);
}
