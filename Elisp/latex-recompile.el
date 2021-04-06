;;(find-file "~/myfile")
;;(revert-buffer "~/myfile")

;; Compile SANS sauvegarde automatique
;; (global-set-key (kbd "C-x e") 'compile)

(setq compile-command (concat "pdflatex " buffer-file-truename)) ;;"make package install")

;;---------------------------------------------------------
;; Compile AVEC sauvegarde automatique
;; from https://www.masteringemacs.org/article/mastering-key-bindings-emacs
(defun my-save-and-compile-command ()
  (interactive)
  (save-buffer)
  (setq compile-command (concat "pdflatex " buffer-file-truename))
  (call-interactively 'compile)
  )
(defun my-save-and-compile-presentation-command ()
  (interactive)
  (save-buffer)
  (setq compile-command "pdflatex myfile.tex")
  (call-interactively 'compile)
  )
(defun my-delete-dotauxout-save-and-compile-command ()
  (interactive)
  (delete-file "myfile.aux")
  (delete-file "myfile.out")
  (my-save-and-compile-command)
  )
(defun my-delete-dotauxout-save-and-compile-presentation-command ()
  (interactive)
  (delete-file "myfile.aux")
  (delete-file "myfile.out")
  (my-save-and-compile-command)
  )
(global-set-key (kbd "C-x e") 'my-save-and-compile-command)
(global-set-key (kbd "C-x E") 'my-delete-dotauxout-save-and-compile-command)
(global-set-key (kbd "C-x M-e") 'my-save-and-compile-presentation-command)
(global-set-key (kbd "C-x M-E") 'my-delete-dotauxout-save-and-compile-presentation-command)
