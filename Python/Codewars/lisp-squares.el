(defun is-square? (n)
  (progn
    (if (>= n 0)
    (setq m (sqrt n))
    (setq m 0))
    (setq m (floor m))
    (setq o (* m m))
    (write n)
    (princ " ")
    (write o)
    (if (= n o))))

