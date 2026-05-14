# 📘 Assignment: Debug Quest: Testing and Bug Fixes

## 🎯 Objective

Practice real-world software engineering skills by writing tests, identifying bugs, and fixing a small Python arcade simulation.

## 📝 Tasks

### 🛠️	Write Tests for the Arcade Engine

#### Description
You are given a mini game engine with several hidden logic bugs. Start by writing tests that capture the expected behavior of each function before changing the implementation.

#### Requirements
Completed program should:

- Create a test file named `test_starter_code.py` using Python's built-in `unittest` module
- Add tests for `calculate_score()`, `update_lives()`, and `get_rank()`
- Include at least one edge-case test (for example, score exactly on a rank boundary)
- Run your tests and confirm that at least 3 tests fail before fixes are applied


### 🛠️	Fix Bugs and Add a Fun Feature

#### Description
After tests expose the issues, fix the broken logic in the starter code. Then add one new feature that makes the game more interesting.

#### Requirements
Completed program should:

- Fix `calculate_score()` so penalties reduce score and the result never goes below 0
- Fix `update_lives()` so taking a hit decreases lives and lives never go below 0
- Fix `get_rank()` so higher scores map to stronger ranks correctly
- Add one new feature (for example: bonus points for a perfect combo, or a new rank tier)
- Ensure all tests pass after your fixes