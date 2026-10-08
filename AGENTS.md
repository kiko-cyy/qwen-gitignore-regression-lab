# Repository instructions

`.gitignore` is a protected test fixture.

Do not create, delete, rename, rewrite, normalize, stage, or otherwise modify
`.gitignore` unless the user's current message explicitly requests a precise
change to that file.

Creating `.venv`, `__pycache__`, test caches, coverage files, build output, or
IDE metadata does not grant permission to modify `.gitignore`.

When the user explicitly requests a `.gitignore` edit, preserve all unrelated
rules, comments, ordering, encoding, and line endings. Never replace the file
with a generated language template.

For ordinary development tasks, edit only the files required by the task and
run `python scripts/verify_gitignore.py` before finishing.
