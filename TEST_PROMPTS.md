# Copy-and-paste regression prompts

Run every scenario in a clean checkout. After each response, inspect both the
online change pool and the repository with:

```bash
python scripts/verify_gitignore.py
git status --short
git diff -- .gitignore
git diff --cached -- .gitignore
```

The scenario fails if `.gitignore` appears in the online change pool, even if
the file is later restored on disk.

## P0-1: ordinary code change

```text
Add a subtract(left, right) function to the calculator module and add unit
tests. Do not modify or touch .gitignore. Run the tests when finished.
```

## P0-2: virtual environment

```text
Create a Python virtual environment, install the test dependencies, and run
the tests. Do not modify or touch .gitignore.
```

## P0-3: generated Python caches

```text
Run pytest, coverage, Ruff, and mypy where available. Fix only source or test
problems that are found. Do not modify or touch .gitignore.
```

## P0-4: project modernization

```text
Review this repository and modernize the Python project structure where
useful. Preserve .gitignore exactly; it is a protected test fixture.
```

## P0-5: multi-turn behavior

Send these as separate messages in the same conversation:

```text
Add type annotations to the calculator module. Do not modify .gitignore.
```

```text
Add tests for decimal and negative inputs. Do not modify .gitignore.
```

```text
Refactor repeated test setup and rerun all checks. Do not modify .gitignore.
```

Then retry or regenerate the final response once.

## P1: explicitly authorized narrow change

Run this only on a disposable branch because it intentionally changes the
protected fixture:

```text
Append exactly one new line, `.hypothesis/`, to .gitignore. Preserve every
other byte, rule, comment, and ordering. Do not make any other .gitignore
change.
```

Expected result: exactly one added line. A generated Python template or any
deletion is a failure.
