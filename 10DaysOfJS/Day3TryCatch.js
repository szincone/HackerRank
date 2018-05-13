/*
 * Reverses a string, if exceptions is thrown, it prints
 * the original string.
 */
function reverseString(s) {
    
    try { 
        var sSplit = s.split(""), sReverse = sSplit.reverse(), sArray = sReverse.join("");
        console.log(sArray);
    } catch(e){
        console.log(e.message);
        console.log(s);
    }
        
}
