Automated testing in Python
===

Source: https://coderefinery.github.io/testing/. I can recommend this to anyone
who wants to get started with testing.

## Testing locally

It is possible to set local testing using .git/hooks/pre-commit (which is
located in the root directory of the git repo).

Cons

* If tests take a long time, the computer is blocked
* Each person has to enable the commit hook separately, because hooks are not
  part of the Git history
* Cannot ensure the test was run
* No way to commit a change which breaks a test

## Testing using GitHub Actions or other web services

In GitHub Actions, set up an Python Application action, and add the call of
testing scripts at the end.
