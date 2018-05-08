/*
 * First prints all vowels of a strings.
 * Then prints all consonants. 
 */
function vowelsAndConsonants(s) {
    var vowels = ['a','e','i','o','u']
    var vowel_l = []
    var consts = []
    var s_list = []
    for (let x in s) {
        if (vowels.includes(s[x])) {
            vowel_l += s[x];
        } else {
            consts += s[x];
        }
    s_list = vowel_l + consts
    }
    for (let i in s_list) {
        let list = vowel_l + consts
        console.log(s_list[i])
    }
}
