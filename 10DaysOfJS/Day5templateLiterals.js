function sides(literals, ...expressions) {
    // spread operator distriubtes values to our area and perimeter variables
    const [a,p] = expressions;
    // find the square root using the algorithim listeted above and return
    var root = Math.sqrt((p**2)-(16*a));
    return ([(p - root)/4, (p + root)/4]);
}
