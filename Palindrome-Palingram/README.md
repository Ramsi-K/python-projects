# Palindrome and Palingram Finder

This project focuses on identifying **palindromes** and **palingrams** from a given dictionary. It also explores optimization techniques and profiling to improve performance.

## Project Overview

### Palindromes

A **palindrome** is a word, phrase, or sequence that reads the same backward as forward (e.g., "radar"). The `palindromes.py` script implements a simple palindrome finder.

### Palingrams

A **palingram** is a pair of words that form a palindrome when combined (e.g., "straw" + "warts"). The `palingrams.py` script identifies palingrams from a dictionary, with subsequent scripts focusing on optimization and profiling.

---

## Files in the Project

1. **`load_dictionary.py`**: Loads and handles the dictionary file for word processing.
2. **`palindromes.py`**: Identifies palindromes from the dictionary.
3. **`palingrams.py`**: Searches for palingrams using a basic approach.
4. **`palingrams_optimized.py`**: Optimized version of palingram search using sets for faster performance.
5. **`palingrams_timed.py`**: Profiles and times the palingram search for performance evaluation.
6. **`cprofile_test.py`**: Uses `cProfile` to analyze performance bottlenecks in the palingram search.
7. **`dictionary_cleanup_practice.py`**: Cleans and verifies dictionary files to ensure data quality.

---

## Key Features

- **Palindrome Finder**:
  - Simple and efficient implementation to identify palindromes from a dictionary.

- **Palingram Finder**:
  - Identifies word pairs that form palindromes when combined.
  - Optimized version (`palingrams_optimized.py`) improves performance significantly using sets.

- **Performance Analysis**:
  - Uses `cProfile` and manual timing (`palingrams_timed.py`) to evaluate performance.
  - Demonstrates the performance advantage of sets over lists.

---

## Lessons Learned

1. **Optimization**:
   - Sets are faster than lists for membership checks, making them ideal for large datasets.
2. **Profiling**:
   - Tools like `cProfile` and manual timing are essential for identifying bottlenecks and improving code efficiency.
3. **Code Refactoring**:
   - Iterative improvements can significantly enhance both readability and performance.

---

This project demonstrates the value of efficient data structures and profiling in solving computational problems. It serves as a practical exercise in writing, optimizing, and analyzing Python code.
