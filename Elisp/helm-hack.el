;; Bind helper functions to keys
(use-package helm-descbinds
  :ensure t
  :bind (("C-h b" . helm-descbinds)
         ("C-h h" . helm-descbinds)))

;; Counsel/Ivy/Swiper
;;
(use-package ivy
  :ensure t
  :load-path (lambda () (my-return-path-if-ok
                         "~/src/emacs/swiper.git")) ;; local hacking, can be ignored
  :commands ivy-mode
  :init (ivy-mode)
  :config
  (setq
    ivy-use-virtual-buffers t
    ivy-count-format "%d/%d "
    ivy-re-builders-alist
    '((ivy-switch-buffer . ivy--regex-plus)
      (t . ivy--regex-plus))))

(use-package ivy-hydra
  :after ivy
  :ensure t)

(use-package counsel
  :ensure t
  :commands counsel-mode
  :bind (:map counsel-mode-map
              ("M-x" . counsel-M-x)
              ("M-y" . counsel-yank-pop)
              ("C-x b" . counsel-switch-buffer)
              ("C-x m" . counsel-mark-ring)
              ("C-h ?" . counsel-search))
  :init (counsel-mode))

;; Traceback
;; C-h v lui-completion-function
;; C-h m ; minor and major modes activated
;; C-h v completion-at-point-functions
;; 
