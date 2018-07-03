function regexVar() {
    /*
     * Declare a RegExp object variable named 're'
     * It must match a string that starts and ends with the same vowel (i.e., {a, e, i, o, u})
     */
    // \1$ checks that the last character matches the first captured charcter
    let re =  /^([aeiou])[a-z]+\1$/ ;
    /*
     * Do not remove the return statement
     */
    return re;
}
