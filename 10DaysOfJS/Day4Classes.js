class Polygon {
    // Use the constructor to assign values to our perimeter total
    // this keyword assigns the parameter values to our new variable
    constructor(perimeterTotal){
        this.perimeterTotal = perimeterTotal;
    }
    // Use reduce to add up all of the elements in our array
    perimeter() {
       return this.perimeterTotal.reduce(function(a, b){return a + b});
    }
}
