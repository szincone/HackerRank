/** Returns A, B, C, or D depending on criteria. */
function getLetter(s) {
    switch (true) {
    case ['a','e','i','o','u'].includes(s[0]):
        return "A";
        break;
    case ['b','c','d','f','g'].includes(s[0]):
        return "B";
        break;
    case ['h','j','k','l','m'].includes(s[0]):
        return "C";
        break;
    default:
        return "D";
    }
}
