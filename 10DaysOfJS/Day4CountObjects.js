/*
 * Return a count of the total number of objects 'o' satisfying o.x == o.y.
 * 
 * Parameter(s):
 * objects: an array of objects with integer properties 'x' and 'y'
 */
function getCount(objects) {
    // setting our counter variable
    var count = 0;
    // iterating through our objects array
    for (let i in objects){
        // while iterating, if x == y, count variable gets a +1
        if (objects[i].x == objects[i].y){
            count += 1;
        } 
    // returning the count of the number of x == y
    } return count;
    
}
