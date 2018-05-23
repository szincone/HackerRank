/*
 * Rectangle function that return length, width,
 * perimeter, and area.
 */
function Rectangle(a, b) {
    // setting constants
    const length = a, width = b, perimeter = 2 * (a + b), area = a * b;
    // returning values needed to meet conditions
    return {length, width, perimeter, area};
}
