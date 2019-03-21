# Pre-commit hooks template example

This is a sample pre-commit hook that is built using [pre-commit hooks template](https://github.com/btomer/pre-commit-hooks-template).

The hook provided by this project is `verify_shebang`, which verifies that shell scripts you commit to git start with a [https://en.wikipedia.org/wiki/Shebang\_(Unix)](Shebang) (`#!`).

To use this pre-commit hook in your project, install the [pre-commit-hooks](https://pre-commit.com) framework, and then create a `.pre-commit-config.yaml` file your repository's root directory and add the following lines to it:

```yaml
repos:
  - repo: https://github.com/btomer/pre-commit-hook-verify-shebang
    rev: v1.0.0
    hooks:
      - id: verify_shebang
```
