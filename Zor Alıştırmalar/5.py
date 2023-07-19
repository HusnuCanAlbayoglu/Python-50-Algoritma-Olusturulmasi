def nearest_vowel (letter):
    alphabet="abcdefghijklmnopqrstuvwxyz"
    vowels_index=[alphabet.index(i) for i in "aeiou"]
    nearest=[abs(alphabet.index(letter)-i)for i in vowels_index]
    return "aeiou"[nearest.index(min(nearest))]

nearest_vowel("i")