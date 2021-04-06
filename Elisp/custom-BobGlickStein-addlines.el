;;----------
;;----- Add lines at the top of the buffer -----
;;----------
;;(defun previous-line--next-line-at-end (&optional arg try-vscroll)
;;  "Insert an empty line when moving up from the top line."
;;  (if (and next-line-add-newlines (= arg 1)
;;       (save-excursion (beginning-of-line) (bobp)))
;;(message "printf: bobp is %S " (bobp))
;;(if (bobp)
;;    (progn
;;(message "printf: %S %S %S " arg try-vscroll (bobp))
;; (beginning-of-line)
;;(newline))
;;  (when (bobp)
;;    (beginning-of-line)
;;    (newline))
;;(message "printf: doesn't pass through the function and bobp is %S " (bobp))))
;;  )
;;(advice-add 'previous-line :before #'previous-line--next-line-at-end)
;;----------
;;----- Ent add lines at the top of the buffer -----
;;----------

