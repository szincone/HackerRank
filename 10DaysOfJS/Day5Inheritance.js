/*
 *  Write code that adds an 'area' method to the Rectangle class' prototype
 */
Rectangle.prototype.area = function() {
  return this.h * this.w;
}
/*
 * Create a Square class that inherits from Rectangle and implement its class constructor
 */
class Square extends Rectangle {
    constructor(squareSides) {
        super(squareSides);
        // Hackerrank needs h and w specifically
        this.h = squareSides;
        this.w = squareSides;
    }
    
}// End Square class
