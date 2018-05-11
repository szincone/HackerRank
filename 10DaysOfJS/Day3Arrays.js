/**
*   Return the second largest number in the array.
*   @param {Number[]} nums - An array of numbers.
*   @return {Number} The second largest number in the array.
**/
function getSecondLargest(nums) {
    // Makes a new array and Set() gets rid of duplicates
    var setNums = Array.from(new Set(nums)) 
    // Reverse sort our array for easy indexings
    var newNums = setNums.sort(function(a,b){return b-a});
    // Calling second largest number in array
    return newNums[1];
}
