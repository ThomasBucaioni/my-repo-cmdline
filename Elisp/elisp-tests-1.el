;; This buffer is for text that is not saved, and for Lisp evaluation.
;; To create a file, visit it with C-x C-f and enter text in its buffer.
(setq myl '(1 2 3 4))
(dolist (element myl)
  (when (= (mod element 2) 0)
    ;;(print element)
    (message (number-to-string element))))

(let (some-var)
  (when (null some-var)
    (message "var is null")))

some-var
myl

(let ((some-var) (other-var 1))
  (if (null some-var)
      (progn
	(message "Variable is null")
	(message "Other message - null case"))
    (message "Variable not null")
    (message "Other message - non null case")
    ))

(defun sum-evens (some-list)
  (let ((sum 0))
    (dolist (element some-list)
      (when (= (mod element 2) 0)
	(setq sum (+ sum element))
	(message "sum = %d ; element = %d" sum element)))
    sum))

(sum-evens myl)

(setq electric-pair-mode t)

(require 'ert)

(ert-deftest sum-evens-test ()
  (should (= (sum-evens '(1 3 5)) 0))
  (should (= (sum-evens '(1 2 3)) 2))
  (should (= (sum-evens '()) 0))
  )

