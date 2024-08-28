# Anagram and Phrase Anagram Solver

This project explores solving single-word and multi-word phrase anagrams. It also includes a thematic Voldemort challenge, using cryptanalytical techniques to uncover the hidden name. Advanced techniques like digrams, trigrams, and CV mapping were employed to optimize the process.

## Project Overview

### Single-Word Anagrams

The project begins with the implementation of `anagrams.py`, a script to find all valid single-word anagrams for a given input using a dictionary.

### Phrase Anagrams

Building on the single-word solution, `phrase_anagrams.py` handles multi-word anagrams. The script allows users to:

- Generate partial anagrams.
- Validate whether generated words are meaningful.
- Select words interactively to form phrases.

Example: The input "Bill Bo" produces the phrase anagram "ill Bob".

### Voldemort Anagram Challenge

Using brute-force and cryptanalytical techniques, the Voldemort challenge solves a complex anagram using:

1. **CV Mapping**: Maps consonants and vowels for efficient filtering.
2. **Digrams and Trigrams**: Uses least-likely trigrams and digrams to refine the search space.
3. **Permutation-Based Search**: Brute-forces potential solutions and allows user input for leftover letters.

---

## Files in the Project

1. **`anagrams.py`**: Finds single-word anagrams for a given input.
2. **`phrase_anagrams.py`**: Finds multi-word phrase anagrams interactively.
3. **`voldemort_british.py`**: Implements the Voldemort brute-force solver with advanced filtering.
4. **`load_dictionary.py`**: Handles loading the dictionary file for word processing.
5. **`count_digrams_practice.py`**: Identifies digrams from the dictionary for filtering.
6. **`least-likely_trigrams.txt`**: Provides a list of least-likely trigrams for filtering improbable combinations.

---

## Key Features

1. **Interactive Anagram Solving**:
   - Allows users to form phrase anagrams interactively.
   - Offers real-time validation of meaningful words.

2. **Voldemort Anagram Challenge**:
   - Leverages cryptanalysis techniques to refine brute-force anagram solving.
   - Integrates digram and trigram filtering for better performance.

3. **Optimized Word Processing**:
   - Utilizes Python’s `itertools` and `collections` modules for efficiency.
   - Explores the performance impact of sets and lists for word lookups.

---

## Lessons Learned

1. **Cryptanalysis Applications**:
   - Techniques like CV mapping and n-grams are powerful tools for text analysis and filtering.

2. **Interactive Scripting**:
   - Designing user-interactive scripts improves usability and showcases dynamic problem-solving.

---

This project showcases advanced text analysis techniques and interactive scripting to solve challenging anagram problems. It demonstrates the value of optimization and the practical application of Python's standard library.
