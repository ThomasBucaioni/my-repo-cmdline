Start with some list:

- one
- two
- three
- four

Define a counter variable:

M-: (defvar *i* 0) RET

Then select the list, and use:

M-x replace-regexp RET ^- → \,(incf *i*)) RET

To get:

1) one
2) two
3) three
4) four
