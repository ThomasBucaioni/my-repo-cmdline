;;-----
;; test
;;-----
(global-set-key (kbd "M-s =") 'my-yank-primary)
(defun my-yank-primary ()
  "Primary paste with the keyboard"
  (run-hooks 'mouse-leave-buffer-hook)
  (when select-active-regions
    (let (select-active-regions)
      (deactivate-mark)))
  (let ((primary (gui-get-primary-selection)))
    (push-mark)
    (insert-for-yank primary)))
;;-----
;; final
;;-----  
(global-set-key (kbd "M-s =") 'my-yank-primary) ; former : undefined
(defun my-yank-primary ()
  "Primary paste with the keyboard"
  (interactive)
  (let ((primary (gui-get-primary-selection)))
    (push-mark)
    (insert-for-yank primary)))
