Automated testing in Python
===

Source: https://coderefinery.github.io/testing/

## Testing locally

It is possible to set local testing using .git/hooks/pre-commit (which is
located in the root directory of the git repo).

Cons

* If tests take a long time, the computer is blocked
* Each person has to enable the commit hook separately, because hooks are not
  part of the Git history
* Cannot ensure the test was run
* No way to commit a change which breaks a test
