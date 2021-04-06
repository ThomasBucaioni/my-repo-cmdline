;;----------
;;----- limited-save-excursion
;;----------
(defmacro limited-save-excursion (&rest subexprs)
  "Like save-expression, but only restores point."
  `(let ((orig-point (point-marker)))
     (unwind-protect
         (progn ,@subexprs)
       (goto-char orig-point))))
;;-----
(defmacro limited-save-excursion-v2 (&rest subexprs)
  "Like save-expression, but only restores point."
  (let ((orig-point (make-symbol "orig-point")))
    `(let ((,orig-point (point-marker)))
       (unwind-protect
           (progn ,@subexprs)
         (goto-char ,orig-point)))))
;;-----
(defun my-func-test-limited-save-excursion ()
  "Tests macro limited-save-excursion."
  (interactive)
  (setq line-start 0)
  (message "printf: line-start is %S " line-start)
  (setq line-start (limited-save-excursion
                    (beginning-of-line)
                    (point)))
  (message "printf: line-start is %S " line-start))
;;-----
(macroexpand (limited-save-excursion
              (beginning-of-line)
              (point)))
;;----------
;;----- end limited-save-excursion
;;----------
