;;-----
;; Highlightings
;;-----
(load "~/.emacs.d/highlight-chars")
;;-----
;; keybindings
(global-set-key (kbd "<f8>")
                'hc-toggle-highlight-trailing-whitespace)
(setq hc-other-chars '("{:0123456789"))
(defun my-highlight-command ()
  (interactive)
  (hc-toggle-highlight-other-chars '(:foreground "red" :background "green"))
  )
(global-set-key (kbd "<f9>")
                'my-highlight-command)

;;;(global-set-key (kbd "<f9>")
;;;                (lambda ()
;;;                  (interactive)
;;;                  (hc-toggle-highlight-other-chars
;;;                    '(:foreground "red" :background "green"))))

;;;(while (search-forward-regexp REGEXP nil t)
;;;  (let* ((beg  (match-beginning 0))
;;;         (xx   (make-overlay beg (point))))
;;;    (overlay-put xx 'face '(:background "grey20"))
;;;    (read-char "Options:... ")
;;;    (remove-overlays beg (point))))

                                        ;(rot13 "zvpxrl@znfgrevatrznpf.bet")

(global-set-key (kbd "<f7>")
                (lambda ()
                  (interactive)
                  (highlight-regexp "func")))
(global-set-key (kbd "<f6>")
                (lambda ()
                  (interactive)
                  (unhighlight-regexp "func")))

(defun my/toggle-highlight ()
  (interactive)
  (let ((pattern ".*(.*).*=.*(.*).*\\|if\\|do"))
    (if (assoc pattern hi-lock-interactive-patterns) ; assoc or alist-get
        (unhighlight-regexp pattern)
      (highlight-regexp pattern))))
(global-set-key (kbd "<f5>") #'my/toggle-highlight)

