;;----------
;;---- Minor mode refill-mode
;;----------
;;(require 'refillmode) ; in the .emacs file
;;----------
;;----- End minor mode refill-mode
;;----------

;;----------
;;---- Minor mode refill-mode (in ~/.emacs.d/lisp/refillmode.el)
;;----------
(defvar refill-mode nil
  "Mode variable for refill minor mode.")
(make-variable-buffer-local 'refill-mode)
;;-----
(defun refill-mode (&optional arg)
  "Refill minor mode."
  (interactive "P")
  (setq refill-mode
        (if (null arg)
            (not refill-mode)
          (> (prefix-numeric-value arg) 0)))
  ;;  (make-local-hook 'after-change-functions)
  (if refill-mode
    ;;(add-hook 'after-change-functions 'my-hook-debug nil t)
    (add-hook 'after-change-functions 'refill nil t)
    (remove-hook 'after-change-functions 'refill t)))
;;-----
(defun refill (start end len)
  "After a text change, refill the current paragraph."
  ;;  (interactive)
  (message "start: %S" start)
  (message "end  : %S" end)
  (message "len  : %S" len)
  (save-excursion
    (progn 
      (setq left-1 (progn
		     (goto-char start)
		     (beginning-of-line 0)
		     (point)))
      (setq left-2 (progn
		     (goto-char start)
		     (backward-paragraph 1)
		     (point)))))
  (message "point: %S" (point))
  (message "left-1: %S" left-1)
  (message "left-2: %S" left-2)
  (let ((left (if (or (zerop len)
                      (not (before-2nd-word-p start)))
		  ;;(save-excursion (beginning-of-line))
		  ;;start
		  (max left-1 left-2)
		(max left-1 left-2))))
    (if (or (and (zerop len)
                 (same-line-p start end)
                 (short-line-p end))
            (and (eq (char-syntax (preceding-char))
                     ?\ )
                 (looking-at "\\s *$")))
        nil
      (save-excursion
        (fill-region left end nil nil t)))))
;;-----
(defun before-2nd-word-p (pos)
  "Does POS lie before the second word on the line?"
  (save-excursion
    (goto-char pos)
    (beginning-of-line)
    (skip-syntax-forward "^ "); (concat "^ " (char-to-string (char-syntax ?\n))))
    (skip-syntax-forward " ")
    (< pos (point))))
;;-----
(defun same-line-p (start end)
  "Are START and END on the same line?"
  (save-excursion
    (goto-char start)
    (end-of-line)
    (<= end (point))))
;;-----
(defun short-line-p (pos)
  "Does line containing POS stay within 'fill-column'?"
  (save-excursion
    (goto-char pos)
    (end-of-line)
    (<= (current-column) fill-column)))
;;-----
(if (not (assq 'refill-mode minor-mode-alist))
    (setq minor-mode-alist
          (cons '(refill-mode " Refill")
                minor-mode-alist)))
;;-----
(defun my-hook-debug (&rest args)
  (message "HOOK: %S" args))
;;(add-hook 'after-change-functions 'my-hook-debug nil t)
(provide 'refillmode)
;;----------
;;----- End minor mode refill-mode
;;----------
;; (global-set-key (kbd "some key") (lambda () (interactive) (message "fill column: %s" fill-column)))

