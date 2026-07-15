
# 🐍 python-journey

A personal learning repository of small Python examples, exercises, and notes arranged by chapter. This repository is designed as a hands‑on reference for learning Python concepts step‑by‑step.

---

## 📚 At-a-glance index (click to jump)

Below is the project hierarchy. Click any file to jump to a detailed description further down this document.


# Repository Structure

📁 **python-journey/**
  - 📁 **[Ch_01/](#ch_01)**
      - 📄 [calc.py](#file-ch_01-calc-py)
      - 📄 [escape_sequences.py](#file-ch_01-escape_sequences-py)
      - 📄 [Ex_01.py](#file-ch_01-Ex_01-py)
      - 📄 [print_func.py](#file-ch_01-print_func-py)
      - 📄 [raw_string.py](#file-ch_01-raw_string-py)
      - 📄 [regex.py](#file-ch_01-regex-py)
      - 📄 [variable.py](#file-ch_01-variable-py)
  - 📁 **[Ch_02/](#ch_02)**
      - 📄 [Ex_01.py](#file-ch_02-Ex_01-py)
      - 📄 [Ex_02.py](#file-ch_02-Ex_02-py)
      - 📄 [Ex_03.py](#file-ch_02-Ex_03-py)
      - 📄 [Ex_04.py](#file-ch_02-Ex_04-py)
      - 📄 [Ex_05.py](#file-ch_02-Ex_05-py)
      - 📄 [input_function.py](#file-ch_02-input_function-py)
      - 📄 [str_alignment.py](#file-ch_02-str_alignment-py)
      - 📄 [str_concatenation.py](#file-ch_02-str_concatenation-py)
      - 📄 [str_formatting.py](#file-ch_02-str_formatting-py)
      - 📄 [str_immutability.py](#file-ch_02-str_immutability-py)
      - 📄 [str_indexing.py](#file-ch_02-str_indexing-py)
      - 📄 [str_methods.py](#file-ch_02-str_methods-py)
      - 📄 [str_slicing.py](#file-ch_02-str_slicing-py)
      - 📄 [type_casting.py](#file-ch_02-type_casting-py)
  - 📁 **[Ch_03/](#ch_03)**
      - 📄 [empty_or_not.py](#file-ch_03-empty_or_not-py)
      - 📄 [Ex_01.py](#file-ch_03-Ex_01-py)
      - 📄 [Ex_02.py](#file-ch_03-Ex_02-py)
      - 📄 [Ex_03.py](#file-ch_03-Ex_03-py)
      - 📄 [Ex_04.py](#file-ch_03-Ex_04-py)
      - 📄 [Ex_05.py](#file-ch_03-Ex_05-py)
      - 📄 [for_loop.py](#file-ch_03-for_loop-py)
      - 📄 [if_elif_else.py](#file-ch_03-if_elif_else-py)
      - 📄 [if_else.py](#file-ch_03-if_else-py)
      - 📄 [logical_operators.py](#file-ch_03-logical_operators-py)
      - 📄 [membership_operators.py](#file-ch_03-membership_operators-py)
      - 📄 [pass_statement.py](#file-ch_03-pass_statement-py)
      - 📄 [while_loop.py](#file-ch_03-while_loop-py)
  - 📁 **[Ch_04/](#ch_04)**
      - 📄 [Ex_01.py](#file-ch_04-Ex_01-py)
      - 📄 [Ex_02.py](#file-ch_04-Ex_02-py)
      - 📄 [Ex_03.py](#file-ch_04-Ex_03-py)
      - 📄 [fibonacci_sequence.py](#file-ch_04-fibonacci_sequence-py)
      - 📄 [functions_basics.py](#file-ch_04-functions_basics-py)
      - 📄 [return_multiple_values.py](#file-ch_04-return_multiple_values-py)
  - 📁 **[Ch_05/](#ch_05)**
      - 📄 [Ex_01.py](#file-ch_05-Ex_01-py)
      - 📄 [Ex_02.py](#file-ch_05-Ex_02-py)
      - 📄 [Ex_03.py](#file-ch_05-Ex_03-py)
      - 📄 [Ex_04.py](#file-ch_05-Ex_04-py)
      - 📄 [Ex_05.py](#file-ch_05-Ex_05-py)
      - 📄 [Ex_06.py](#file-ch_05-Ex_06-py)
      - 📄 [Ex_07.py](#file-ch_05-Ex_07-py)
      - 📄 [list_addition_methods.py](#file-ch_05-list_addition_methods-py)
      - 📄 [list_advanced_concepts.py](#file-ch_05-list_advanced_concepts-py)
      - 📄 [list_basics.py](#file-ch_05-list_basics-py)
      - 📄 [list_comparison.py](#file-ch_05-list_comparison-py)
      - 📄 [list_methods.py](#file-ch_05-list_methods-py)
      - 📄 [list_removal_methods.py](#file-ch_05-list_removal_methods-py)
      - 📄 [min_max_functions.py](#file-ch_05-min_max_functions-py)
      - 📄 [split_and_join.py](#file-ch_05-split_and_join-py)
  - 📁 **[Ch_06/](#ch_06)**
      - 📄 [tuple_basics.py](#file-ch_06-tuple_basics-py)
      - 📄 [tuple_methods.py](#file-ch_06-tuple_methods-py)
  - 📁 **[Ch_07/](#ch_07)**
      - 📄 [dictionary_basics.py](#file-ch_07-dictionary_basics-py)
      - 📄 [dictionary_iteration.py](#file-ch_07-dictionary_iteration-py)
      - 📄 [dictionary_methods.py](#file-ch_07-dictionary_methods-py)
      - 📄 [dictionary_removal_methods.py](#file-ch_07-dictionary_removal_methods-py)
      - 📄 [Ex_01.py](#file-ch_07-Ex_01-py)
      - 📄 [Ex_02.py](#file-ch_07-Ex_02-py)
      - 📄 [Ex_03.py](#file-ch_07-Ex_03-py)
  - 📁 **[Ch_08](#ch_08)/**
      - 📄 [frozenset_basics.py](#file-ch_08-frozenset_basics-py)
      - 📄 [set_basics.py](#file-ch_08-set_basics-py)
      - 📄 [set_comprehension.py](#file-ch_08-set_comprehension-py)
      - 📄 [set_methods.py](#file-ch_08-set_methods-py)
      - 📄 [set_operators.py](#file-ch_08-set_operators-py)
  - 📁 **[Ch_09](#ch_09)/**
      - 📄 [Ex_01.py](#file-ch_09-Ex_01-py)
      - 📄 [Ex_02.py](#file-ch_09-Ex_02-py)
      - 📄 [Ex_03.py](#file-ch_09-Ex_03-py)
      - 📄 [Ex_04.py](#file-ch_09-Ex_04-py)
      - 📄 [list_comprehension.py](#file-ch_09-list_comprehension-py)
  - 📁 **[Ch_10](#ch_10)/**
      - 📄 [dictionary_comprehension.py](#file-ch_10-dictionary_comprehension-py)
  - 📁 **[Ch_11](#ch_11)/**
      - 📄 [args_positional_arguments.py](#file-ch_11-args_positional_arguments-py)
      - 📄 [Ex_01.py](#file-ch_11-Ex_01-py)
      - 📄 [Ex_02.py](#file-ch_11-Ex_02-py)
      - 📄 [kwargs_keyword_arguments.py](#file-ch_11-kwargs_keyword_arguments-py)
  - 📁 **[Ch_12](#ch_12)/**
      - 📄 [lambda_basics.py](#file-ch_12-lambda_basics-py)
  - 📁 **[Ch_13](#ch_13)/**
      - 📄 [advance_min_max.py](#file-ch_13-advance_min_max-py)
      - 📄 [any_all_basics.py](#file-ch_13-any_all_basics-py)
      - 📄 [docstrings_and_help.py](#file-ch_13-docstrings_and_help-py)
      - 📄 [enumerate_basics.py](#file-ch_13-enumerate_basics-py)
      - 📄 [Ex_01.py](#file-ch_13-Ex_01-py)
      - 📄 [Ex_02.py](#file-ch_13-Ex_02-py)
      - 📄 [Ex_03.py](#file-ch_13-Ex_03-py)
      - 📄 [Ex_04.py](#file-ch_13-Ex_04-py)
      - 📄 [filter_function_basics.py](#file-ch_13-filter_function_basics-py)
      - 📄 [iterables_vs_iterators.py](#file-ch_13-iterables_vs_iterators-py)
      - 📄 [map_function_basics.py](#file-ch_13-map_function_basics-py)
      - 📄 [sort_vs_sorted.py](#file-ch_13-sort_vs_sorted-py)
      - 📄 [zip_function_basics.py](#file-ch_13-zip_function_basics-py)
  - 📁 **[Ch_14](#ch_14)/**
      - 📄 [decorators_basics.py](#file-ch_14-decorators_basics-py)
      - 📄 [Ex_01.py](#file-ch_14-Ex_01-py)
      - 📄 [Ex_02.py](#file-ch_14-Ex_02-py)
      - 📄 [first_class_functions_and_closures.py](#file-ch_14-first_class_functions_and_closures-py)
      - 📄 [function_as_argument.py](#file-ch_14-function_as_argument-py)
      - 📄 [function_returning_function.py](#file-ch_14-function_returning_function-py)

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


|                                 **Files**                                   |                      **Key Concepts**                                        |
|-----------------------------------------------------------------------------|------------------------------------------------------------------------------| 
| <a id="file-ch_02-Ex_01-py"></a>**Ch_02/Ex_01.py**                          | first exercise — reinforcing string basics.                                  |
| <a id="file-ch_02-Ex_02-py"></a>**Ch_02/Ex_02.py**                          | second exercise — practice formatting or concatenation.                      |
| <a id="file-ch_02-Ex_03-py"></a>**Ch_02/Ex_03.py**                          | third exercise — focused on indexing or slicing strings.                     |
| <a id="file-ch_02-Ex_04-py"></a>**Ch_02/Ex_04.py**                          | fourth exercise — alignment/formatting edge cases.                           |
| <a id="file-ch_02-Ex_05-py"></a>**Ch_02/Ex_05.py**                          | fifth exercise — further string practice; check contents for specifics.      |
| <a id="file-ch_02-input_function-py"></a>**Ch_02/input_function.py**        | demonstrates `input()` behavior and basic input parsing.                     |
| <a id="file-ch_02-str_alignment-py"></a>**Ch_02/str_alignment.py**          | string alignment using `.ljust()`, `.rjust()`, `.center()` and format specs. |
| <a id="file-ch_02-str_concatenation-py"></a>**Ch_02/str_concatenation.py**  | concatenating strings with `+`, `join()`, and f-strings.                     |                    
| <a id="file-ch_02-str_formatting-py"></a>**Ch_02/str_formatting.py**        | examples of `.format()` and f-strings for interpolation.                     | 
| <a id="file-ch_02-str_immutability-py"></a>**Ch_02/str_immutability.py**    | shows that strings are immutable and how to create modified copies.          |
| <a id="file-ch_02-str_indexing-py"></a>**Ch_02/str_indexing.py**            | indexing into strings with positive and negative indices.                    |
| <a id="file-ch_02-str_methods-py"></a>**Ch_02/str_methods.py**              | common string methods (`lower`, `upper`, `strip`, `split`, etc.).            |
| <a id="file-ch_02-str_slicing-py"></a>**Ch_02/str_slicing.py**              | slicing syntax `s[start:stop:step]` and examples.                            |
| <a id="file-ch_02-type_casting-py"></a>**Ch_02/type_casting.py**            | converting between types: `int()`, `float()`, `str()`, etc.                  |



<a id="ch_03"></a>
### 📘 Chapter 03 — Control flow: loops and conditionals


|                                 **Files**                                        |                      **Key Concepts**                         |
|----------------------------------------------------------------------------------|---------------------------------------------------------------| 
| <a id="file-ch_03-empty_or_not-py"></a>**Ch_03/empty_or_not.py**                 | checking emptiness for containers and truthiness.             |
| <a id="file-ch_03-Ex_01-py"></a>**Ch_03/Ex_01.py**                               | first exercise — conditional logic.                           |
| <a id="file-ch_03-Ex_02-py"></a>**Ch_03/Ex_02.py**                               | second exercise — conditional/loop practice.                  |
| <a id="file-ch_03-Ex_03-py"></a>**Ch_03/Ex_03.py**                               | third exercise — further control flow exercises.              |
| <a id="file-ch_03-Ex_04-py"></a>**Ch_03/Ex_04.py**                               | fourth exercise — practice with loops and conditions.         |
| <a id="file-ch_03-Ex_05-py"></a>**Ch_03/Ex_05.py**                               | fifth exercise — additional exercises; inspect for details.   |
| <a id="file-ch_03-for_loop-py"></a>**Ch_03/for_loop.py**                         | `for` loop examples, iterating lists/ranges/strings.          |
| <a id="file-ch_03-if_elif_else-py"></a>**Ch_03/if_elif_else.py**                 | multi-branch conditional examples.                            |                    
| <a id="file-ch_03-if_else-py"></a>**Ch_03/if_else.py**                           | simple `if/else` examples and pattern usage.                  |   
| <a id="file-ch_03-logical_operators-py"></a>**Ch_03/logical_operators.py**       | `and`, `or`, `not` semantics and short-circuit examples.      |
| <a id="file-ch_03-membership_operators-py"></a>**Ch_03/membership_operators.py** | `in` and `not in` usage with sequences and sets.              |
| <a id="file-ch_03-pass_statement-py"></a>**Ch_03/pass_statement.py**             | shows `pass` as a placeholder in control flow.                |
| <a id="file-ch_03-while_loop-py"></a>**Ch_03/while_loop.py**                     | `while` loop examples and loop control (`break`, `continue`). |



<a id="ch_04"></a>
### 📘 Chapter 04 — Functions

|                                 **Files**                                            |                      **Key Concepts**                        |
|------------------------------------------------------------------------------------- |--------------------------------------------------------------| 
| <a id="file-ch_04-Ex_01-py"></a>**Ch_04/Ex_01.py**                                   | first exercise — function definition examples.               |
| <a id="file-ch_04-Ex_02-py"></a>**Ch_04/Ex_02.py**                                   | second exercise — function practice and parameter handling.  |
| <a id="file-ch_04-Ex_03-py"></a>**Ch_04/Ex_03.py**                                   | third exercise — more exercises on functions.                |
| <a id="file-ch_04-fibonacci_sequence-py"></a>**Ch_04/fibonacci_sequence.py**         | implement Fibonacci sequence examples (iterative/recursive). |
| <a id="file-ch_04-functions_basics-py"></a>**Ch_04/functions_basics.py**             | function signatures, defaults, and return values.            |
| <a id="file-ch_04-return_multiple_values-py"></a>**Ch_04/return_multiple_values.py** | returning tuples / multiple values and tuple unpacking.      |



<a id="ch_05"></a>
### 📘 Chapter 05 — Lists and sequence operations


|                                 **Files**                                            |                      **Key Concepts**                         |
|------------------------------------------------------------------------------------- |---------------------------------------------------------------| 
| <a id="file-ch_05-Ex_01-py"></a>**Ch_05/Ex_01.py**                                   | first exercise — list basics practice.                        |
| <a id="file-ch_05-Ex_02-py"></a>**Ch_05/Ex_02.py**                                   | second exercise — list methods practice.                      |
| <a id="file-ch_05-Ex_03-py"></a>**Ch_05/Ex_03.py**                                   | third exercise — list comprehension or iteration practice.    |
| <a id="file-ch_05-Ex_04-py"></a>**Ch_05/Ex_04.py**                                   | exercises for list removal/manipulation.                      |
| <a id="file-ch_05-Ex_05-py"></a>**Ch_05/Ex_05.py**                                   | additional list practice.                                     |
| <a id="file-ch_05-Ex_06-py"></a>**Ch_05/Ex_06.py**                                   | more list-method exercises.                                   |
| <a id="file-ch_05-Ex_07-py"></a>**Ch_05/Ex_07.py**                                   | extended list practice.                                       |
| <a id="file-ch_05-list_addition_methods-py"></a>**Ch_05/list_addition_methods.py**   |  `append`, `extend`, `insert` and related methods examples.   |
| <a id="file-ch_05-list_advanced_concepts-py"></a>**Ch_05/list_advanced_concepts.py** | slicing, aliasing vs copying, list performance notes.         |
| <a id="file-ch_05-list_basics-py"></a>**Ch_05/list_basics.py**                       | constructing lists, indexing, and iteration.                  |
| <a id="file-ch_05-list_comparison-py"></a>**Ch_05/list_comparison.py**               | comparing lists, equality vs identity.                        |
| <a id="file-ch_05-list_methods-py"></a>**Ch_05/list_methods.py**                     | overview of common list methods (sort, reverse, count, etc.). |
| <a id="file-ch_05-list_removal_methods-py"></a>**Ch_05/list_removal_methods.py**     | `pop`, `remove`, `del` usage and examples.                    |
| <a id="file-ch_05-min_max_functions-py"></a>**Ch_05/min_max_functions.py**           | `min()`, `max()`, `sum()` and custom key functions.           |
| <a id="file-ch_05-split_and_join-py"></a>**Ch_05/split_and_join.py**                 | `str.split()` and `'sep'.join()` usage with lists.            |



<a id="ch_06"></a>
### 📘 Chapter 06 — Tuples


|                                 **Files**                          |                      **Key Concepts**                               |
|--------------------------------------------------------------------|---------------------------------------------------------------------| 
| <a id="file-ch_06-tuple_basics-py"></a>**Ch_06/tuple_basics.py**   | immutable sequence behavior and tuple usage.                        |
| <a id="file-ch_06-tuple_methods-py"></a>**Ch_06/tuple_methods.py** | methods available to tuples (`count`, `index`) and common patterns. |



<a id="ch_07"></a>
### 📘 Chapter 07 — Dictionaries



|                                 **Files**                                                    |                      **Key Concepts**                        |
|----------------------------------------------------------------------------------------------|--------------------------------------------------------------| 
| <a id="file-ch_07-dictionary_basics-py"></a>**Ch_07/dictionary_basics.py**                   | creating and accessing dictionaries; key/value semantics.    |
| <a id="file-ch_07-dictionary_iteration-py"></a>**Ch_07/dictionary_iteration.py**             | iterating keys, values, and items; safe lookup with `get()`. |
| <a id="file-ch_07-dictionary_methods-py"></a>**Ch_07/dictionary_methods.py**                 | `update`, `setdefault`, `pop`, and other utility methods.    |
| <a id="file-ch_07-dictionary_removal_methods-py"></a>**Ch_07/dictionary_removal_methods.py** | examples showing removal patterns and `del` vs `pop()`.      |
| <a id="file-ch_07-Ex_01-py"></a>**Ch_07/Ex_01.py**                                           | first exercise.                                              |
| <a id="file-ch_07-Ex_02-py"></a>**Ch_07/Ex_02.py**                                           | second exercise.                                             |
| <a id="file-ch_07-Ex_03-py"></a>**Ch_07/Ex_03.py**                                           | third exercise.                                              |



<a id="ch_08"></a>
### 📘 Chapter 08 — Sets and frozensets



|                                 **Files**                                  |                      **Key Concepts**                           |
|----------------------------------------------------------------------------|-----------------------------------------------------------------| 
| <a id="file-ch_08-frozenset_basics-py"></a>**Ch_08/frozenset_basics.py**   | demonstrate `frozenset` behavior (immutable set).               |
| <a id="file-ch_08-set_basics-py"></a>**Ch_08/set_basics.py**               | set creation, uniqueness, and basic operations.                 |
| <a id="file-ch_08-set_comprehension-py"></a>**Ch_08/set_comprehension.py** | create sets using comprehension syntax.                         |
| <a id="file-ch_08-set_methods-py"></a>**Ch_08/set_methods.py**             | methods such as `add`, `remove`, `discard`, and `pop`.          |
| <a id="file-ch_08-set_operators-py"></a>**Ch_08/set_operators.py**         | union, intersection, difference, symmetric difference examples. |


<a id="ch_09"></a>
### 📘 Chapter 09 — Comprehensions



|                                 **Files**                                    |                      **Key Concepts**                            |
|------------------------------------------------------------------------------|------------------------------------------------------------------| 
| <a id="file-ch_09-Ex_01-py"></a>**Ch_09/Ex_01.py**                           | first exercise — comprehension exercises.                        |
| <a id="file-ch_09-Ex_02-py"></a>**Ch_09/Ex_02.py**                           | second exercise — comprehension practice with filtering.         |
| <a id="file-ch_09-Ex_03-py"></a>**Ch_09/Ex_03.py**                           | third exercise — nested comprehension examples.                  |
| <a id="file-ch_09-Ex_04-py"></a>**Ch_09/Ex_04.py**                           | fourth exercise — more comprehension tasks.                      |
| <a id="file-ch_09-list_comprehension-py"></a>**Ch_09/list_comprehension.py** | detailed examples of list comprehensions and idiomatic patterns. |




<a id="ch_10"></a>
### 📘 Chapter 10 — Dictionary comprehensions



|                                 **Files**                                                |                      **Key Concepts**                       |
|------------------------------------------------------------------------------------------|-------------------------------------------------------------| 
| <a id="file-ch_10-dictionary_comprehension-py"></a>**Ch_10/dictionary_comprehension.py** | examples building dicts with comprehensions and conditions. |                        



<a id="ch_11"></a>
### 📘 Chapter 11 — Function arguments


|                                 **Files**                                                  |                      **Key Concepts**                   |
|--------------------------------------------------------------------------------------------|---------------------------------------------------------| 
| <a id="file-ch_11-args_positional_arguments-py"></a>**Ch_11/args_positional_arguments.py** | positional arguments, `*args` usage.                    |
| <a id="file-ch_11-Ex_01-py"></a>**Ch_11/Ex_01.py**                                         | first exercise — exercise on argument passing.          |
| <a id="file-ch_11-Ex_02-py"></a>**Ch_11/Ex_02.py**                                         | second exercise — more argument-related practice.       |
| <a id="file-ch_11-kwargs_keyword_arguments-py"></a>**Ch_11/kwargs_keyword_arguments.py**   | keyword arguments, `**kwargs`, and named-only patterns. |




<a id="ch_12"></a>
### 📘 Chapter 12 — Lambdas and anonymous functions



|                                 **Files**                          |                      **Key Concepts**                         |
|--------------------------------------------------------------------|---------------------------------------------------------------| 
| <a id="file-ch_12-lambda_basics-py"></a>**Ch_12/lambda_basics.py** | anonymous functions with `lambda`, usage with `map`/`filter`. |                        


<a id="ch_13"></a>
### 📘 Chapter 13 — Utilities and functional tools



|                                 **Files**                                            |                      **Key Concepts**                          |
|--------------------------------------------------------------------------------------|----------------------------------------------------------------| 
| <a id="file-ch_13-advance_min_max-py"></a>**Ch_13/advance_min_max.py**               | advanced usage of `min`/`max` with `key` functions.            |
| <a id="file-ch_13-any_all_basics-py"></a>**Ch_13/any_all_basics.py**                 | `any()` and `all()` patterns for predicate checks.             |
| <a id="file-ch_13-docstrings_and_help-py"></a>**Ch_13/docstrings_and_help.py**       | writing docstrings and using `help()`/`__doc__`.               |
| <a id="file-ch_13-enumerate_basics-py"></a>**Ch_13/enumerate_basics.py**             | using `enumerate()` to get index/value pairs in loops.         |
| <a id="file-ch_13-Ex_01-py"></a>**Ch_13/Ex_01.py**                                   | first exercise — utilities practice.                           |
| <a id="file-ch_13-Ex_02-py"></a>**Ch_13/Ex_02.py**                                   | second exercise — functional patterns.                         |
| <a id="file-ch_13-Ex_03-py"></a>**Ch_13/Ex_03.py**                                   | third exercise — practice tasks.                               |
| <a id="file-ch_13-Ex_04-py"></a>**Ch_13/Ex_04.py**                                   | fourth exercise — additional exercises.                        |
| <a id="file-ch_13-filter_function_basics-py"></a>**Ch_13/filter_function_basics.py** | examples of `filter()` and predicate functions.                |
| <a id="file-ch_13-iterables_vs_iterators-py"></a>**Ch_13/iterables_vs_iterators.py** | clarify the differences between iterables and iterators.       |
| <a id="file-ch_13-map_function_basics-py"></a>**Ch_13/map_function_basics.py**       | `map()` examples and alternatives with comprehensions.         |
| <a id="file-ch_13-sort_vs_sorted-py"></a>**Ch_13/sort_vs_sorted.py**                 | in-place `list.sort()` vs built-in `sorted()` and `key` usage. |
| <a id="file-ch_13-zip_function_basics-py"></a>**Ch_13/zip_function_basics.py**       | `zip()` to combine iterables and common idioms.                |




<a id="ch_14"></a>
### 📘 Chapter 14 — Higher-order functions and decorators



|                                 **Files**                                                                    |                      **Key Concepts**                          |
|--------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------| 
| <a id="file-ch_14-decorators_basics-py"></a>**Ch_14/decorators_basics.py**                                   | basic decorator patterns, `@decorator` syntax example.         |
| <a id="file-ch_14-Ex_01-py"></a>**Ch_14/Ex_01.py**                                                           | first exercise — decorator basics.                             |
| <a id="file-ch_14-Ex_02-py"></a>**Ch_14/Ex_02.py**                                                           | second exercise — further decorator practice.                  |
| <a id="file-ch_14-first_class_functions_and_closures-py"></a>**Ch_14/first_class_functions_and_closures.py** | first-class functions, closures, and lexical scoping examples. |
| <a id="file-ch_14-function_as_argument-py"></a>**Ch_14/function_as_argument.py**                             | passing functions as arguments and callback patterns.          |
| <a id="file-ch_14-function_returning_function-py"></a>**Ch_14/function_returning_function.py**               | functions that create and return other functions.              |


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