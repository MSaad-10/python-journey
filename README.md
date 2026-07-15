
# 🐍 python-journey

A personal learning repository of small Python examples, exercises, and notes arranged by chapter. This repository is designed as a hands‑on reference for learning Python concepts step‑by‑step.

---

## 📚 At-a-glance index (click to jump)

Below is the project hierarchy. Click any file to jump to a detailed description further down this document.


# Repository Structure

📁 **python-journey/**
  - 📁 **[Ch_01](#ch_01)**
      - 📄 [Ch_01/calc.py](#file-ch_01-calc-py)
      - 📄 [Ch_01/escape_sequences.py](#file-ch_01-escape_sequences-py)
      - 📄 [Ch_01/Ex_01.py](#file-ch_01-Ex_01-py)
      - 📄 [Ch_01/print_func.py](#file-ch_01-print_func-py)
      - 📄 [Ch_01/raw_string.py](#file-ch_01-raw_string-py)
      - 📄 [Ch_01/regex.py](#file-ch_01-regex-py)
      - 📄 [Ch_01/variable.py](#file-ch_01-variable-py)
  - 📁 **[Ch_02](#ch_02)**
      - 📄 [Ch_02/Ex_01.py](#file-ch_02-Ex_01-py)
      - 📄 [Ch_02/Ex_02.py](#file-ch_02-Ex_02-py)
      - 📄 [Ch_02/Ex_03.py](#file-ch_02-Ex_03-py)
      - 📄 [Ch_02/Ex_04.py](#file-ch_02-Ex_04-py)
      - 📄 [Ch_02/Ex_05.py](#file-ch_02-Ex_05-py)
      - 📄 [Ch_02/input_function.py](#file-ch_02-input_function-py)
      - 📄 [Ch_02/str_alignment.py](#file-ch_02-str_alignment-py)
      - 📄 [Ch_02/str_concatenation.py](#file-ch_02-str_concatenation-py)
      - 📄 [Ch_02/str_formatting.py](#file-ch_02-str_formatting-py)
      - 📄 [Ch_02/str_immutability.py](#file-ch_02-str_immutability-py)
      - 📄 [Ch_02/str_indexing.py](#file-ch_02-str_indexing-py)
      - 📄 [Ch_02/str_methods.py](#file-ch_02-str_methods-py)
      - 📄 [Ch_02/str_slicing.py](#file-ch_02-str_slicing-py)
      - 📄 [Ch_02/type_casting.py](#file-ch_02-type_casting-py)
  - 📁 **[Ch_03](#ch_03)**
      - 📄 [Ch_03/empty_or_not.py](#file-ch_03-empty_or_not-py)
      - 📄 [Ch_03/Ex_01.py](#file-ch_03-Ex_01-py)
      - 📄 [Ch_03/Ex_02.py](#file-ch_03-Ex_02-py)
      - 📄 [Ch_03/Ex_03.py](#file-ch_03-Ex_03-py)
      - 📄 [Ch_03/Ex_04.py](#file-ch_03-Ex_04-py)
      - 📄 [Ch_03/Ex_05.py](#file-ch_03-Ex_05-py)
      - 📄 [Ch_03/for_loop.py](#file-ch_03-for_loop-py)
      - 📄 [Ch_03/if_elif_else.py](#file-ch_03-if_elif_else-py)
      - 📄 [Ch_03/if_else.py](#file-ch_03-if_else-py)
      - 📄 [Ch_03/logical_operators.py](#file-ch_03-logical_operators-py)
      - 📄 [Ch_03/membership_operators.py](#file-ch_03-membership_operators-py)
      - 📄 [Ch_03/pass_statement.py](#file-ch_03-pass_statement-py)
      - 📄 [Ch_03/while_loop.py](#file-ch_03-while_loop-py)
  - 📁 **[Ch_04](#ch_04)**
      - 📄 [Ch_04/Ex_01.py](#file-ch_04-Ex_01-py)
      - 📄 [Ch_04/Ex_02.py](#file-ch_04-Ex_02-py)
      - 📄 [Ch_04/Ex_03.py](#file-ch_04-Ex_03-py)
      - 📄 [Ch_04/fibonacci_sequence.py](#file-ch_04-fibonacci_sequence-py)
      - 📄 [Ch_04/functions_basics.py](#file-ch_04-functions_basics-py)
      - 📄 [Ch_04/return_multiple_values.py](#file-ch_04-return_multiple_values-py)
  - 📁 **[Ch_05](#ch_05)**
      - 📄 [Ch_05/Ex_01.py](#file-ch_05-Ex_01-py)
      - 📄 [Ch_05/Ex_02.py](#file-ch_05-Ex_02-py)
      - 📄 [Ch_05/Ex_03.py](#file-ch_05-Ex_03-py)
      - 📄 [Ch_05/Ex_04.py](#file-ch_05-Ex_04-py)
      - 📄 [Ch_05/Ex_05.py](#file-ch_05-Ex_05-py)
      - 📄 [Ch_05/Ex_06.py](#file-ch_05-Ex_06-py)
      - 📄 [Ch_05/Ex_07.py](#file-ch_05-Ex_07-py)
      - 📄 [Ch_05/list_addition_methods.py](#file-ch_05-list_addition_methods-py)
      - 📄 [Ch_05/list_advanced_concepts.py](#file-ch_05-list_advanced_concepts-py)
      - 📄 [Ch_05/list_basics.py](#file-ch_05-list_basics-py)
      - 📄 [Ch_05/list_comparison.py](#file-ch_05-list_comparison-py)
      - 📄 [Ch_05/list_methods.py](#file-ch_05-list_methods-py)
      - 📄 [Ch_05/list_removal_methods.py](#file-ch_05-list_removal_methods-py)
      - 📄 [Ch_05/min_max_functions.py](#file-ch_05-min_max_functions-py)
      - 📄 [Ch_05/split_and_join.py](#file-ch_05-split_and_join-py)
  - 📁 **[Ch_06](#ch_06)**
      - 📄 [Ch_06/tuple_basics.py](#file-ch_06-tuple_basics-py)
      - 📄 [Ch_06/tuple_methods.py](#file-ch_06-tuple_methods-py)
  - 📁 **[Ch_07](#ch_07)**
      - 📄 [Ch_07/dictionary_basics.py](#file-ch_07-dictionary_basics-py)
      - 📄 [Ch_07/dictionary_iteration.py](#file-ch_07-dictionary_iteration-py)
      - 📄 [Ch_07/dictionary_methods.py](#file-ch_07-dictionary_methods-py)
      - 📄 [Ch_07/dictionary_removal_methods.py](#file-ch_07-dictionary_removal_methods-py)
      - 📄 [Ch_07/Ex_01.py](#file-ch_07-Ex_01-py)
      - 📄 [Ch_07/Ex_02.py](#file-ch_07-Ex_02-py)
      - 📄 [Ch_07/Ex_03.py](#file-ch_07-Ex_03-py)
  - 📁 **[Ch_08](#ch_08)**
      - 📄 [Ch_08/frozenset_basics.py](#file-ch_08-frozenset_basics-py)
      - 📄 [Ch_08/set_basics.py](#file-ch_08-set_basics-py)
      - 📄 [Ch_08/set_comprehension.py](#file-ch_08-set_comprehension-py)
      - 📄 [Ch_08/set_methods.py](#file-ch_08-set_methods-py)
      - 📄 [Ch_08/set_operators.py](#file-ch_08-set_operators-py)
  - 📁 **[Ch_09](#ch_09)**
      - 📄 [Ch_09/Ex_01.py](#file-ch_09-Ex_01-py)
      - 📄 [Ch_09/Ex_02.py](#file-ch_09-Ex_02-py)
      - 📄 [Ch_09/Ex_03.py](#file-ch_09-Ex_03-py)
      - 📄 [Ch_09/Ex_04.py](#file-ch_09-Ex_04-py)
      - 📄 [Ch_09/list_comprehension.py](#file-ch_09-list_comprehension-py)
  - 📁 [Ch_10](#ch_10)
      - 📄 [Ch_10/dictionary_comprehension.py](#file-ch_10-dictionary_comprehension-py)
  - 📁 **[Ch_11](#ch_11)**
      - 📄 [Ch_11/args_positional_arguments.py](#file-ch_11-args_positional_arguments-py)
      - 📄 [Ch_11/Ex_01.py](#file-ch_11-Ex_01-py)
      - 📄 [Ch_11/Ex_02.py](#file-ch_11-Ex_02-py)
      - 📄 [Ch_11/kwargs_keyword_arguments.py](#file-ch_11-kwargs_keyword_arguments-py)
  - 📁 **[Ch_12](#ch_12)**
      - 📄 [Ch_12/lambda_basics.py](#file-ch_12-lambda_basics-py)
  - 📁 **[Ch_13](#ch_13)**
      - 📄 [Ch_13/advance_min_max.py](#file-ch_13-advance_min_max-py)
      - 📄 [Ch_13/any_all_basics.py](#file-ch_13-any_all_basics-py)
      - 📄 [Ch_13/docstrings_and_help.py](#file-ch_13-docstrings_and_help-py)
      - 📄 [Ch_13/enumerate_basics.py](#file-ch_13-enumerate_basics-py)
      - 📄 [Ch_13/Ex_01.py](#file-ch_13-Ex_01-py)
      - 📄 [Ch_13/Ex_02.py](#file-ch_13-Ex_02-py)
      - 📄 [Ch_13/Ex_03.py](#file-ch_13-Ex_03-py)
      - 📄 [Ch_13/Ex_04.py](#file-ch_13-Ex_04-py)
      - 📄 [Ch_13/filter_function_basics.py](#file-ch_13-filter_function_basics-py)
      - 📄 [Ch_13/iterables_vs_iterators.py](#file-ch_13-iterables_vs_iterators-py)
      - 📄 [Ch_13/map_function_basics.py](#file-ch_13-map_function_basics-py)
      - 📄 [Ch_13/sort_vs_sorted.py](#file-ch_13-sort_vs_sorted-py)
      - 📄 [Ch_13/zip_function_basics.py](#file-ch_13-zip_function_basics-py)
  - 📁 **[Ch_14](#ch_14)**
      - 📄 [Ch_14/decorators_basics.py](#file-ch_14-decorators_basics-py)
      - 📄 [Ch_14/Ex_01.py](#file-ch_14-Ex_01-py)
      - 📄 [Ch_14/Ex_02.py](#file-ch_14-Ex_02-py)
      - 📄 [Ch_14/first_class_functions_and_closures.py](#file-ch_14-first_class_functions_and_closures-py)
      - 📄 [Ch_14/function_as_argument.py](#file-ch_14-function_as_argument-py)
      - 📄 [Ch_14/function_returning_function.py](#file-ch_14-function_returning_function-py)

---

## 🔎 How this README is organized

- The index above links into per-file sections below.
- Each file section contains: **purpose**, **key concepts**, **example usage**, and **notes**.
- Use your `Python 3` interpreter to run examples locally.

---

## 📚 Chapters (detailed)


<a id="ch_01"></a>
### 📘 Chapter 01 — Basics: strings, raw text, and printing


|                                 **Files**                                |                      **Key Concepts**                                          |
|--------------------------------------------------------------------------|--------------------------------------------------------------------------------| 
| <a id="file-ch_01-calc-py"></a>**Ch_01/calc.py**                         | arithmetic examples and simple calculations.                                   |
| <a id="file-ch_01-emoji_char-py"></a> **Ch_01/emoji_char.py**            | working with emoji and Unicode characters.                                     |
| <a id="file-ch_01-escape_sequences-py"></a>**Ch_01/escape_sequences.py** | demonstrates newline `\n`, tab `\t`, and other escape sequences.               |
| <a id="file-ch_01-Ex_01-py"></a>**Ch_01/Ex_01.py**                       | reinforces `print()` usage and string literals.                                |
| <a id="file-ch_01-print_func-py"></a>**Ch_01/print_func.py**             | examples of the `print()` function and its parameters (`sep`, `end`, `file`).  |
| <a id="file-ch_01-raw_string-py"></a>**Ch_01/raw_string.py**             | demonstrates raw strings `r"..."` and when to use them (regex, paths).         |
| <a id="file-ch_01-regex-py"></a>**Ch_01/regex.py**                       | basic regular expression examples using `re` module.                           |
| <a id="file-ch_01-variable-py"></a>**Ch_01/variable.py**                 | variable assignment, types, and introspection (`type()`).                      |                    


<a id="ch_02"></a>
### 📘 Chapter 02 — Strings and formatting

<a id="file-ch_02-Ex_01-py"></a>
#### Ch_02/Ex_01.py
- **Purpose:** exercise reinforcing string basics.

<a id="file-ch_02-Ex_02-py"></a>
#### Ch_02/Ex_02.py
- **Purpose:** second exercise — practice formatting or concatenation.

<a id="file-ch_02-Ex_03-py"></a>
#### Ch_02/Ex_03.py
- **Purpose:** exercise focused on indexing or slicing strings.

<a id="file-ch_02-Ex_04-py"></a>
#### Ch_02/Ex_04.py
- **Purpose:** exercises for alignment/formatting edge cases.

<a id="file-ch_02-Ex_05-py"></a>
#### Ch_02/Ex_05.py
- **Purpose:** further string practice; check contents for specifics.

<a id="file-ch_02-input_function-py"></a>
#### Ch_02/input_function.py
- **Purpose:** demonstrates `input()` behavior and basic input parsing.
- **Key concepts:** user input, casting types, prompting.

<a id="file-ch_02-str_alignment-py"></a>
#### Ch_02/str_alignment.py
- **Purpose:** string alignment using `.ljust()`, `.rjust()`, `.center()` and format specs.

<a id="file-ch_02-str_concatenation-py"></a>
#### Ch_02/str_concatenation.py
- **Purpose:** concatenating strings with `+`, `join()`, and f-strings.

<a id="file-ch_02-str_formatting-py"></a>
#### Ch_02/str_formatting.py
- **Purpose:** examples of `.format()` and f-strings for interpolation.

<a id="file-ch_02-str_immutability-py"></a>
#### Ch_02/str_immutability.py
- **Purpose:** shows that strings are immutable and how to create modified copies.

<a id="file-ch_02-str_indexing-py"></a>
#### Ch_02/str_indexing.py
- **Purpose:** indexing into strings with positive and negative indices.

<a id="file-ch_02-str_methods-py"></a>
#### Ch_02/str_methods.py
- **Purpose:** common string methods (`lower`, `upper`, `strip`, `split`, etc.).

<a id="file-ch_02-str_slicing-py"></a>
#### Ch_02/str_slicing.py
- **Purpose:** slicing syntax `s[start:stop:step]` and examples.

<a id="file-ch_02-type_casting-py"></a>
#### Ch_02/type_casting.py
- **Purpose:** converting between types: `int()`, `float()`, `str()`, etc.

<a id="ch_03"></a>
### 📘 Chapter 03 — Control flow: loops and conditionals

<a id="file-ch_03-empty_or_not-py"></a>
#### Ch_03/empty_or_not.py
- **Purpose:** checking emptiness for containers and truthiness.

<a id="file-ch_03-Ex_01-py"></a>
#### Ch_03/Ex_01.py
- **Purpose:** exercise on conditional logic.

<a id="file-ch_03-Ex_02-py"></a>
#### Ch_03/Ex_02.py
- **Purpose:** conditional/loop practice.

<a id="file-ch_03-Ex_03-py"></a>
#### Ch_03/Ex_03.py
- **Purpose:** further control flow exercises.

<a id="file-ch_03-Ex_04-py"></a>
#### Ch_03/Ex_04.py
- **Purpose:** practice with loops and conditions.

<a id="file-ch_03-Ex_05-py"></a>
#### Ch_03/Ex_05.py
- **Purpose:** additional exercises; inspect for details.

<a id="file-ch_03-for_loop-py"></a>
#### Ch_03/for_loop.py
- **Purpose:** `for` loop examples, iterating lists/ranges/strings.

<a id="file-ch_03-if_elif_else-py"></a>
#### Ch_03/if_elif_else.py
- **Purpose:** multi-branch conditional examples.

<a id="file-ch_03-if_else-py"></a>
#### Ch_03/if_else.py
- **Purpose:** simple `if/else` examples and pattern usage.

<a id="file-ch_03-logical_operators-py"></a>
#### Ch_03/logical_operators.py
- **Purpose:** `and`, `or`, `not` semantics and short-circuit examples.

<a id="file-ch_03-membership_operators-py"></a>
#### Ch_03/membership_operators.py
- **Purpose:** `in` and `not in` usage with sequences and sets.

<a id="file-ch_03-pass_statement-py"></a>
#### Ch_03/pass_statement.py
- **Purpose:** shows `pass` as a placeholder in control flow.

<a id="file-ch_03-while_loop-py"></a>
#### Ch_03/while_loop.py
- **Purpose:** `while` loop examples and loop control (`break`, `continue`).

<a id="ch_04"></a>
### 📘 Chapter 04 — Functions

<a id="file-ch_04-Ex_01-py"></a>
#### Ch_04/Ex_01.py
- **Purpose:** function definition exercises.

<a id="file-ch_04-Ex_02-py"></a>
#### Ch_04/Ex_02.py
- **Purpose:** function practice and parameter handling.

<a id="file-ch_04-Ex_03-py"></a>
#### Ch_04/Ex_03.py
- **Purpose:** more exercises on functions.

<a id="file-ch_04-fibonacci_sequence-py"></a>
#### Ch_04/fibonacci_sequence.py
- **Purpose:** implement Fibonacci sequence examples (iterative/recursive).
- **Key concepts:** recursion, loops, performance considerations.

<a id="file-ch_04-functions_basics-py"></a>
#### Ch_04/functions_basics.py
- **Purpose:** function signatures, defaults, and return values.

<a id="file-ch_04-return_multiple_values-py"></a>
#### Ch_04/return_multiple_values.py
- **Purpose:** returning tuples / multiple values and tuple unpacking.

<a id="ch_05"></a>
### 📘 Chapter 05 — Lists and sequence operations

<a id="file-ch_05-Ex_01-py"></a>
#### Ch_05/Ex_01.py
- **Purpose:** list basics exercise.

<a id="file-ch_05-Ex_02-py"></a>
#### Ch_05/Ex_02.py
- **Purpose:** list methods practice.

<a id="file-ch_05-Ex_03-py"></a>
#### Ch_05/Ex_03.py
- **Purpose:** list comprehension or iteration practice.

<a id="file-ch_05-Ex_04-py"></a>
#### Ch_05/Ex_04.py
- **Purpose:** exercises for list removal/manipulation.

<a id="file-ch_05-Ex_05-py"></a>
#### Ch_05/Ex_05.py
- **Purpose:** additional list practice.

<a id="file-ch_05-Ex_06-py"></a>
#### Ch_05/Ex_06.py
- **Purpose:** more list-method exercises.

<a id="file-ch_05-Ex_07-py"></a>
#### Ch_05/Ex_07.py
- **Purpose:** extended list practice.

<a id="file-ch_05-list_addition_methods-py"></a>
#### Ch_05/list_addition_methods.py
- **Purpose:** `append`, `extend`, `insert` and related methods examples.

<a id="file-ch_05-list_advanced_concepts-py"></a>
#### Ch_05/list_advanced_concepts.py
- **Purpose:** slicing, aliasing vs copying, list performance notes.

<a id="file-ch_05-list_basics-py"></a>
#### Ch_05/list_basics.py
- **Purpose:** constructing lists, indexing, and iteration.

<a id="file-ch_05-list_comparison-py"></a>
#### Ch_05/list_comparison.py
- **Purpose:** comparing lists, equality vs identity.

<a id="file-ch_05-list_methods-py"></a>
#### Ch_05/list_methods.py
- **Purpose:** overview of common list methods (sort, reverse, count, etc.).

<a id="file-ch_05-list_removal_methods-py"></a>
#### Ch_05/list_removal_methods.py
- **Purpose:** `pop`, `remove`, `del` usage and examples.

<a id="file-ch_05-min_max_functions-py"></a>
#### Ch_05/min_max_functions.py
- **Purpose:** using `min()`, `max()`, `sum()` and custom key functions.

<a id="file-ch_05-split_and_join-py"></a>
#### Ch_05/split_and_join.py
- **Purpose:** `str.split()` and `'sep'.join()` usage with lists.

<a id="ch_06"></a>
### 📘 Chapter 06 — Tuples

<a id="file-ch_06-tuple_basics-py"></a>
#### Ch_06/tuple_basics.py
- **Purpose:** immutable sequence behavior and tuple usage.

<a id="file-ch_06-tuple_methods-py"></a>
#### Ch_06/tuple_methods.py
- **Purpose:** methods available to tuples (`count`, `index`) and common patterns.

<a id="ch_07"></a>
### 📘 Chapter 07 — Dictionaries

<a id="file-ch_07-dictionary_basics-py"></a>
#### Ch_07/dictionary_basics.py
- **Purpose:** creating and accessing dictionaries; key/value semantics.

<a id="file-ch_07-dictionary_iteration-py"></a>
#### Ch_07/dictionary_iteration.py
- **Purpose:** iterating keys, values, and items; safe lookup with `get()`.

<a id="file-ch_07-dictionary_methods-py"></a>
#### Ch_07/dictionary_methods.py
- **Purpose:** `update`, `setdefault`, `pop`, and other utility methods.

<a id="file-ch_07-dictionary_removal_methods-py"></a>
#### Ch_07/dictionary_removal_methods.py
- **Purpose:** examples showing removal patterns and `del` vs `pop()`.

<a id="file-ch_07-Ex_01-py"></a>
#### Ch_07/Ex_01.py
- **Purpose:** dictionary exercise 1.

<a id="file-ch_07-Ex_02-py"></a>
#### Ch_07/Ex_02.py
- **Purpose:** dictionary exercise 2.

<a id="file-ch_07-Ex_03-py"></a>
#### Ch_07/Ex_03.py
- **Purpose:** dictionary exercise 3.

<a id="ch_08"></a>
### 📘 Chapter 08 — Sets and frozensets

<a id="file-ch_08-frozenset_basics-py"></a>
#### Ch_08/frozenset_basics.py
- **Purpose:** demonstrate `frozenset` behavior (immutable set).

<a id="file-ch_08-set_basics-py"></a>
#### Ch_08/set_basics.py
- **Purpose:** set creation, uniqueness, and basic operations.

<a id="file-ch_08-set_comprehension-py"></a>
#### Ch_08/set_comprehension.py
- **Purpose:** create sets using comprehension syntax.

<a id="file-ch_08-set_methods-py"></a>
#### Ch_08/set_methods.py
- **Purpose:** methods such as `add`, `remove`, `discard`, and `pop`.

<a id="file-ch_08-set_operators-py"></a>
#### Ch_08/set_operators.py
- **Purpose:** union, intersection, difference, symmetric difference examples.

<a id="ch_09"></a>
### 📘 Chapter 09 — Comprehensions

<a id="file-ch_09-Ex_01-py"></a>
#### Ch_09/Ex_01.py
- **Purpose:** comprehension exercises.

<a id="file-ch_09-Ex_02-py"></a>
#### Ch_09/Ex_02.py
- **Purpose:** comprehension practice with filtering.

<a id="file-ch_09-Ex_03-py"></a>
#### Ch_09/Ex_03.py
- **Purpose:** nested comprehension examples.

<a id="file-ch_09-Ex_04-py"></a>
#### Ch_09/Ex_04.py
- **Purpose:** more comprehension tasks.

<a id="file-ch_09-list_comprehension-py"></a>
#### Ch_09/list_comprehension.py
- **Purpose:** detailed examples of list comprehensions and idiomatic patterns.

<a id="ch_10"></a>
### 📘 Chapter 10 — Dictionary comprehensions

<a id="file-ch_10-dictionary_comprehension-py"></a>
#### Ch_10/dictionary_comprehension.py
- **Purpose:** examples building dicts with comprehensions and conditions.

<a id="ch_11"></a>
### 📘 Chapter 11 — Function arguments

<a id="file-ch_11-args_positional_arguments-py"></a>
#### Ch_11/args_positional_arguments.py
- **Purpose:** positional arguments, `*args` usage.

<a id="file-ch_11-Ex_01-py"></a>
#### Ch_11/Ex_01.py
- **Purpose:** exercise on argument passing.

<a id="file-ch_11-Ex_02-py"></a>
#### Ch_11/Ex_02.py
- **Purpose:** more argument-related practice.

<a id="file-ch_11-kwargs_keyword_arguments-py"></a>
#### Ch_11/kwargs_keyword_arguments.py
- **Purpose:** keyword arguments, `**kwargs`, and named-only patterns.

<a id="ch_12"></a>
### 📘 Chapter 12 — Lambdas and anonymous functions

<a id="file-ch_12-lambda_basics-py"></a>
#### Ch_12/lambda_basics.py
- **Purpose:** anonymous functions with `lambda`, usage with `map`/`filter`.

<a id="ch_13"></a>
### 📘 Chapter 13 — Utilities and functional tools

<a id="file-ch_13-advance_min_max-py"></a>
#### Ch_13/advance_min_max.py
- **Purpose:** advanced usage of `min`/`max` with `key` functions.

<a id="file-ch_13-any_all_basics-py"></a>
#### Ch_13/any_all_basics.py
- **Purpose:** `any()` and `all()` patterns for predicate checks.

<a id="file-ch_13-docstrings_and_help-py"></a>
#### Ch_13/docstrings_and_help.py
- **Purpose:** writing docstrings and using `help()`/`__doc__`.

<a id="file-ch_13-enumerate_basics-py"></a>
#### Ch_13/enumerate_basics.py
- **Purpose:** using `enumerate()` to get index/value pairs in loops.

<a id="file-ch_13-Ex_01-py"></a>
#### Ch_13/Ex_01.py
- **Purpose:** exercise in utilities.

<a id="file-ch_13-Ex_02-py"></a>
#### Ch_13/Ex_02.py
- **Purpose:** exercise in functional patterns.

<a id="file-ch_13-Ex_03-py"></a>
#### Ch_13/Ex_03.py
- **Purpose:** practice tasks.

<a id="file-ch_13-Ex_04-py"></a>
#### Ch_13/Ex_04.py
- **Purpose:** additional exercises.

<a id="file-ch_13-filter_function_basics-py"></a>
#### Ch_13/filter_function_basics.py
- **Purpose:** examples of `filter()` and predicate functions.

<a id="file-ch_13-iterables_vs_iterators-py"></a>
#### Ch_13/iterables_vs_iterators.py
- **Purpose:** clarify the differences between iterables and iterators.

<a id="file-ch_13-map_function_basics-py"></a>
#### Ch_13/map_function_basics.py
- **Purpose:** `map()` examples and alternatives with comprehensions.

<a id="file-ch_13-sort_vs_sorted-py"></a>
#### Ch_13/sort_vs_sorted.py
- **Purpose:** in-place `list.sort()` vs built-in `sorted()` and `key` usage.

<a id="file-ch_13-zip_function_basics-py"></a>
#### Ch_13/zip_function_basics.py
- **Purpose:** `zip()` to combine iterables and common idioms.

<a id="ch_14"></a>
### 📘 Chapter 14 — Higher-order functions and decorators

<a id="file-ch_14-decorators_basics-py"></a>
#### Ch_14/decorators_basics.py
- **Purpose:** basic decorator patterns, `@decorator` syntax example.

<a id="file-ch_14-Ex_01-py"></a>
#### Ch_14/Ex_01.py
- **Purpose:** decorator exercise.

<a id="file-ch_14-Ex_02-py"></a>
#### Ch_14/Ex_02.py
- **Purpose:** further decorator practice.

<a id="file-ch_14-first_class_functions_and_closures-py"></a>
#### Ch_14/first_class_functions_and_closures.py
- **Purpose:** first-class functions, closures, and lexical scoping examples.

<a id="file-ch_14-function_as_argument-py"></a>
#### Ch_14/function_as_argument.py
- **Purpose:** passing functions as arguments and callback patterns.

<a id="file-ch_14-function_returning_function-py"></a>
#### Ch_14/function_returning_function.py
- **Purpose:** functions that create and return other functions.

---

## 🚀 Quick start

1. Ensure you have `Python 3.8+` installed.
2. Run any example directly with:

```bash
python Ch_01/print_func.py
```

---

## 🌱 About This Repository

This repository serves as my structured collection of Python notes, examples, and practice exercises.

It is intended to:
- Strengthen my Python fundamentals
- Document concepts in an organized way
- Track my learning progress
- Provide a quick reference for future projects

As I continue learning, new chapters and examples will be added to reflect my growth as a Python developer.

<p align="center">Happy Learning! 🐍</p>
<p align="center">
⭐ If you found this repository helpful, consider giving it a star :)
</p>