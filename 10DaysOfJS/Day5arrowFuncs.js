function modifyArray(nums) {
    // Use map to iterate through our array and the modulo so if divided by 2
    // and no reminder, we know it's even, and ternary so if true multiply by 2, 
    // if false mulitply by 3. Return our new array.
    let newArray = nums.map(n => n = (n%2==0) ? n*2: n*3);
    return newArray;
}
