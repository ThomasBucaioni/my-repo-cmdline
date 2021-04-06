;;----------
;;----- Redefine keybindings
;;----------
;;(define-key key-translation-map (kbd "C-o") (kbd "C-s"))
(global-set-key (kbd "C-S-o") 'isearch-forward-symbol-at-point)
;; (kbd "C-o") ; former : 'open-line
(global-set-key (kbd "C-o") 'other-window) ; former : 'open-line
(global-set-key (kbd "C-?") 'help-command) ; former : undefined
(global-set-key (kbd "C-? /") 'describe-key) ; former : undefined
;;(define-key key-translation-map (kbd "C-h") (kbd "C-b"))
;; (kbd "C-h") ; former : 'help-command
;;(define-key key-translation-map (kbd "M-h") (kbd "M-b"))
;; (kbd "M-h") ; former : 'mark-paragraph
;; (kbd "C-M-h") ; former : 'mark-defun
;;(define-key key-translation-map (kbd "C-y") (kbd "C-t"))
;; (kbd "C-y") ; former : 'yank
;;(define-key key-translation-map (kbd "M-y") (kbd "M-t"))
;; (kbd "M-y") ; former : 'yank-pop
;;(define-key key-translation-map (kbd "C-'") (kbd "C-y"))
(global-set-key (kbd "C-,") 'kill-buffer)
;; (kbd "C-'") ; former : undefined
(global-set-key (kbd "M-,") 'next-buffer) ; former: xref-pop-marker-stack
;;(define-key key-translation-map (kbd "M-'") (kbd "M-y"))
;;(global-set-key (kbd "M-,") 'yank-pop)
;; (kbd "M-'") ; former : 'abbrev-prefix-mark
(global-set-key (kbd "C-\\") 'yank) ;; former : toggle-input-method
(global-set-key (kbd "C-|") 'yank-pop) ; former : undefined
;;(define-key key-translation-map (kbd "C-t") (kbd "C-p"))
;; (kbd "C-t") ; former : 'transpose-char
;;(define-key key-translation-map (kbd "M-t") (kbd "C-a"))
;; (kbd "M-t") ; former : 'transpose-word
;;(global-set-key (kbd "M-n") 'move-end-of-line) ; former : undefined
;;(define-key key-translation-map (kbd "C-s") (kbd "C-f"))
;; (kbd "C-s") ; former : 'isearch-forward
;;(define-key key-translation-map (kbd "M-s") (kbd "M-f"))
;;(define-key key-translation-map (kbd "M-_") (kbd "M-s"))
;; (kbd "C-M-s") ; former : isearch-forward-regexp
;; (kbd "M-s") ; former : prefix
;; (kbd "M-_") ; former : undefined
(global-set-key (kbd "C-;") 'kill-line) ; former : undefined
(setq kill-whole-line t)
(global-set-key (kbd "C-x f") 'find-file)
;; (kbd "C-x f") ; former : set-fill-column
;; (define-key key-translation-map (kbd "C-b") (kbd "C-x b")) ; not a good idea -> no more C-x C-b...
;; (kbd "C-b") ; former : backward-char
(global-set-key (kbd "C-'") 'save-buffer) ; former : undefined
(global-set-key (kbd "C-\"") 'switch-to-buffer) ; former : undefined
(global-set-key (kbd "C-=") 'kill-region) ; former : undefined
(global-set-key (kbd "C-+") 'kill-ring-save) ; former : undefined
;; (global-set-key (kbd "C-|") ') ; former : undefined
(define-key global-map (kbd "C-x g") 'magit-status)
(global-set-key (kbd "<S-f5>") 'toggle-truncate-lines)
;;-----  
(global-set-key (kbd "M-s =") 'my-yank-primary) ; former : undefined
(defun my-yank-primary ()
  "Primary paste with the keyboard"
  (interactive)
  (let ((primary (gui-get-primary-selection)))
    (push-mark)
    (insert-for-yank primary)))
;;(load "~/.emacs.d/lisp/datclip/datclip.el")

(defun switch-to-minibuffer ()
  "Switch to minibuffer window."
  (interactive)
  (if (active-minibuffer-window)
      (select-window (active-minibuffer-window))
    (error "Minibuffer is not active")))
(global-set-key "\C-co" 'switch-to-minibuffer) ;; Bind to `C-c o'

(defun scroll-a-few-lines-ahead ()
  "Scroll ahead a few lines."
  (interactive)
  (scroll-up 10))
(defun scroll-a-few-lines-behind ()
  "Scroll behind a few lines."
  (interactive)
  (scroll-down 10))
(global-set-key (kbd "<mouse-8>") 'scroll-a-few-lines-ahead) ; former : undefined
(global-set-key (kbd "<mouse-9>") 'scroll-a-few-lines-behind) ; former : undefined
(global-set-key (kbd "C-v") 'next-five-lines) ; former : 'scroll-up
(global-set-key (kbd "C-S-v") 'previous-five-lines) ; former M-v : 'scroll-down
(defun previous-five-lines ()
  "Scroll ahead one/five line(s)."
  (interactive)
  (previous-line 5))
(defun next-five-lines ()
  "Scroll behind one/five line(s)."
  (interactive)
  (next-line 5))
;;(global-set-key (kbd "C-M-t") 'beginning-of-buffer);'previous-five-lines) ; former : 'transpose-sexps
;;(global-set-key (kbd "C-M-n") 'end-of-buffer);'next-five-lines) ; former : 'forward-list
;;(global-set-key (kbd "C-M-h") 'move-beginning-of-line)
;;(global-set-key (kbd "C-M-s") 'move-end-of-line)
;;----------
;;----- End redefine keybindings
;;----------

;;----- older -----
(define-key key-translation-map (kbd "²") (kbd "\\" ))
;;(define-key key-translation-map (kbd "œ") (kbd "\\" ))
;;(define-key key-translation-map (kbd "<f8>") (kbd "• • • •"))
;;(global-set-key (kbd "M-S-<up>") (kbd "• • •")) ;; trois bullets
;;(global-set-key (kbd "M-{") (kbd "{} C-b"))
;; par defaut  : avec espace
;;(global-set-key (kbd "M-[") (kbd "[] C-b"))
;;(global-set-key (kbd "M-]") (kbd "() C-b"))
;;(global-set-key (kbd "M-]") (progn (kbd "()") (backward-char)))
;;(define-key key-translation-map (kbd "^ ") (kbd "^" )) ;; à revoir...

