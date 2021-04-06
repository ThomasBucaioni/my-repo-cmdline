;;----------
;;----- dernière modification le : lun. 24 août 2020 14:36:29 CEST -----
;;----- dernier enregistrement le : lun. 24 août 2020 14:36:29 CEST -----
;;----------
(defvar insert-time-format "%X"
  "*Format for \\[insert-time] (c.f. 'format-time-string').")
(defvar insert-date-format "%x"
  "*Format for \\[insert-date] (c.f. 'format-time-string').")
(defun insert-time ()
  "Insert the current time according to insert-time-format."
  (interactive "*")
  (insert (format-time-string insert-time-format
			      (current-time))))
(defun insert-date ()
  "Insert the current date according to insert-date-format."
  (interactive "*")
  (insert (format-time-string insert-date-format
			      (current-time))))
(defvar writestamp-format "%c"
  "*Format for writestamps (c.f. 'format-time-string').")
(defvar writestamp-prefix-mod "----- dernière modification le : "
  "*Format for writestamps (c.f. 'format-time-string').")
(defvar writestamp-prefix-enr "----- dernier enregistrement le : "
  "*Unique string identifying start of writestamp.")
(defvar writestamp-suffix " -----"
  "*String that terminates a writestamp.")
(defvar last-change-time nil
  "Time of last buffer modification.")
(make-variable-buffer-local 'last-change-time)
(defvar file-has-been-recorded nil
  "Boolean to indicate if the file has been recorded.")
(make-variable-buffer-local 'file-has-been-recorded)
(defun update-writestamps ()
  "Find writestamps and replace them with the current time."
  ;;(interactive "*")
  (message "printf: update-writestamp is executed")
  (save-excursion
    (save-restriction
      (save-match-data
	(widen)
	(goto-char (point-min))
	(setq my-stamps '(writestamp-prefix-mod writestamp-prefix-enr))
	;;(message "printf: my-stamps is %S " my-stamps)
	(while my-stamps
	  (setq my-stamps-tmp (symbol-value (pop my-stamps)))
	  ;;(message "printf: my-stamps-tmp is %S " my-stamps-tmp)
	  (if (string= my-stamps-tmp writestamp-prefix-enr)
	      (setq local-time-string (current-time))
	    (setq local-time-string last-change-time))
	  ;;(message "printf: local-time-string is %S " local-time-string)
	  (goto-char (point-min))
	  (while (re-search-forward (concat "^[;!%].*" (regexp-quote my-stamps-tmp)) nil t)
	    ;;(message "printf: init string found = %S" my-stamps-tmp)
	    (let ((start (point)))
	      (when (re-search-forward (concat (regexp-quote writestamp-suffix) ; if
					       "$")
				       nil t);(save-excursion (end-of-line) (point)) t)
		;;		(progn
		(delete-region start (match-beginning 0)) ; or: (- (point) 2))
		(goto-char start)
		(insert (format-time-string writestamp-format ;insert-time-format ;writestamp-format
					    local-time-string)))
	      ;;(setq my-stamps (cdr my-stamps))
	      ))))))
  nil)
(defun remember-change-time (&rest unused)
  "Store the current time in 'last-change-time'."
  (setq last-change-time (current-time))
  ;;(message "printf: file has been changed, last-change-time is %S" last-change-time)
  )
;;-----
;;(add-hook 'write-file-functions 'update-writestamps)
;;(add-hook 'after-change-functions 'remember-change-time)
;;-----
;;----- tests writestamps -----
;;-----
(defun other-update-writestamps (writestamp-prefix &rest unused)
  "Find writestamps and replace them with the current time."
  (save-excursion
    (save-restriction
      (save-match-data
	(widen)
	(goto-char (point-min))
	(while (re-search-forward (concat "^[;!%].*" (regexp-quote writestamp-prefix)) nil t)
	  (let ((start (point)))
	    (when (re-search-forward (concat (regexp-quote writestamp-suffix)
					     "$")
				     nil t)
	      (delete-region start (match-beginning 0))
	      (goto-char start)
	      (insert (format-time-string writestamp-format
					  (current-time)))))))))
nil)
;;----------
;;(make-local-variable 'after-change-functions) (setq after-change-functions (cons 'remember-change-time after-change-functions))
;;(add-to-list 'after-change-functions 'remember-change-time)
;;----------
(defun update-writestamps-old (writestamp-prefix)
  "Find writestamps and replace them with the current time."
  (save-excursion
    (save-restriction
      (save-match-data
	(widen)
	(goto-char (point-min))
	(while (re-search-forward (concat "^[;!].*" (regexp-quote writestamp-prefix)) nil t)
	  (let ((start (point)))
	    (when (re-search-forward (concat (regexp-quote writestamp-suffix)
					     "$")
				     nil t)
	      (delete-region start (match-beginning 0))
	      (goto-char start)
	      (insert (format-time-string writestamp-format
					  (current-time)))))))))
  nil)
;;----------
;;(add-hook 'write-file-functions (lambda (&rest _) (other-update-writestamps writestamp-prefix-enr)))
;;(add-hook 'after-change-functions (lambda (&rest _) (other-update-writestamps writestamp-prefix-mod)))
;;----------
(provide 'timestamp)
;;----------
;;----- dernière modification le : lun. 24 août 2020 14:36:29 CEST -----
;;----- dernier enregistrement le : lun. 24 août 2020 14:36:29 CEST -----
;;----------

