;; This buffer is for text that is not saved, and for Lisp evaluation.
;; To create a file, visit it with C-x C-f and enter text in its buffer.

(defun cheap-count-words ()
  (interactive)
  (save-excursion
    (let ((words 0))
      (goto-char (point-min))
      (while (forward-word)
	(setq words (1+ words)))
      (message (format "Words in Buffer: %s" words))
      words)))

(require 'ert)

(ert-deftest count-words-test ()
  (get-buffer-create "*test*")
  (with-current-buffer "*test*"
    (erase-buffer)
    (insert "Hello world")
    (should (= (cheap-count-words) 2))
    )
  ;;(kill-buffer "*test*")
  )

