;;----------
;;----- Unscroll ---
;;----------
;;(defadvice scroll-up (before remember-for-unscroll
;;                           activate compile)
;;  "Remember where we started from, for 'unscroll'."
;;  (if (not (eq last-command 'scroll-up))
;;      (setq unscroll-to (point))))
;;-----
(defvar unscroll-to (make-marker)
  "Text position for next call to 'unscroll'.")
(defvar unscroll-window-start (make-marker)
  "Window start for next call to 'unscroll'.")
(defvar unscroll-hscroll nil
  "Window start for next call to 'unscroll'.")
(put 'scroll-one-line-ahead 'unscrollable t)
(put 'scroll-one-line-behind 'unscrollable t)
(put 'end-of-buffer 'unscrollable t)
(put 'beginning-of-buffer 'unscrollable t)
;;-----
;;(defun my-unscroll-function (&optional my_argument) ;(activate compile)
;;"Remember where we started from, for 'unscroll'."
;;(interactive)
;;(message "printf - last command: %S " last-command)
;;(message "printf - point before: %S " (point))
;;(message "printf - unscroll-to before: %S " unscroll-to)
;;(if (not (eq last-command 'scroll-one-line-ahead));unless (eq last-command 'scroll-up)
;;(message "printf - get: %S " (get last-command 'unscrollable))
;;(unless (get last-command 'unscrollable)
;;(progn
;;(message "printf - if last command: %S " last-command)
;;(set-marker unscroll-to (point))
;;(set-marker unscroll-window-start (window-start))
;;(setq unscroll-hscroll (window-hscroll))
;;(message "printf - else last command: %S " last-command))
;;(message "printf - point after: %S " (point))
;;(message "printf - unscroll-to after: %S " unscroll-to))
;;(message "printf - unscroll-window-start= %S " unscroll-window-start))
;;))
;;-----
(defun my-unscroll-function (&optional my_argument) ;(activate compile)
  "Remember where we started from, for 'unscroll'."
  (interactive)
  (unless (and (symbolp last-command)
               (get last-command 'unscrollable))
    (set-marker unscroll-to (point))
    (set-marker unscroll-window-start (window-start))
    (setq unscroll-hscroll (window-hscroll))))
;;-----
(advice-add 'scroll-up :before #'my-unscroll-function)
(advice-add 'scroll-down :before #'my-unscroll-function)
(advice-add 'beginning-of-buffer :before #'my-unscroll-function)
(advice-add 'end-of-buffer :before #'my-unscroll-function)
(defun unscroll ()
  "Jump to location specified by 'unscroll-to'."
  (interactive)
  (goto-char unscroll-to)
  (set-window-start nil unscroll-window-start)
  (set-window-hscroll nil unscroll-hscroll))
;;----------
;;----- Unscroll ---
;;----------

