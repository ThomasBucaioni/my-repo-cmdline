(setq inhibit-startup-message t)

(scroll-bar-mode -1)
(tool-bar-mode -1)
(tooltip-mode -1)
(set-fringe-mode 10)

(menu-bar-mode -1)

(setq visible-bell t)

(require 'cl-lib)

;; Adjust this font size
(defvar efs/default-font-size 180)
(defvar efs/default-variable-font-size 180)

;;(set-face-attribute 'default nil :font "DejaVu Sans Mono-10" :height 100)
(set-face-attribute 'default nil :font "Fira Code Retina" :height 100)
;;(set-face-attribute 'default nil :font "Fira Code" :height 100)

(keyboard-translate ?\C-a ?\C-x)

;; Initialize package sources
(require 'package)

(setq package-archives '(("melpa" . "https://melpa.org/packages/")
                         ("org" . "https://orgmode.org/elpa/")
                         ("elpa" . "https://elpa.gnu.org/packages/")))

(package-initialize)
(unless package-archive-contents
  (package-refresh-contents))

;; Initialize use-package on non-Linux platforms
(unless (package-installed-p 'use-package)
  (package-install 'use-package))

(require 'use-package)
(setq use-package-always-ensure t)

;; (add-to-list 'load-path "~/.elisp/")

;; (use-package ligature
;;   :load-path "path-to-ligature-repo"
;;   :config
;;   ;; Enable the "www" ligature in every possible major mode
;;   (ligature-set-ligatures 't '("www"))
;;   ;; Enable traditional ligature support in eww-mode, if the
;;   ;; `variable-pitch' face supports it
;;   (ligature-set-ligatures 'eww-mode '("ff" "fi" "ffi"))
;;   ;; Enable all Cascadia Code ligatures in programming modes
;;   (ligature-set-ligatures 'prog-mode '("|||>" "<|||" "<==>" "<!--" "####" "~~>" "***" "||=" "||>"
;;                                        ":::" "::=" "=:=" "===" "==>" "=!=" "=>>" "=<<" "=/=" "!=="
;;                                        "!!." ">=>" ">>=" ">>>" ">>-" ">->" "->>" "-->" "---" "-<<"
;;                                        "<~~" "<~>" "<*>" "<||" "<|>" "<$>" "<==" "<=>" "<=<" "<->"
;;                                        "<--" "<-<" "<<=" "<<-" "<<<" "<+>" "</>" "###" "#_(" "..<"
;;                                        "..." "+++" "/==" "///" "_|_" "www" "&&" "^=" "~~" "~@" "~="
;;                                        "~>" "~-" "**" "*>" "*/" "||" "|}" "|]" "|=" "|>" "|-" "{|"
;;                                        "[|" "]#" "::" ":=" ":>" ":<" "$>" "==" "=>" "!=" "!!" ">:"
;;                                        ">=" ">>" ">-" "-~" "-|" "->" "--" "-<" "<~" "<*" "<|" "<:"
;;                                        "<$" "<=" "<>" "<-" "<<" "<+" "</" "#{" "#[" "#:" "#=" "#!"
;;                                        "##" "#(" "#?" "#_" "%%" ".=" ".-" ".." ".?" "+>" "++" "?:"
;;                                        "?=" "?." "??" ";;" "/*" "/=" "/>" "//" "__" "~~" "(*" "*)"
;;                                        "\\\\" "://"))
;;   ;; Enables ligature checks globally in all buffers. You can also do it
;;   ;; per mode with `ligature-mode'.
;;   (global-ligature-mode t))

(use-package command-log-mode)
;;clm/toggle-command-log-buffer\
;;global-command-log-mode


(use-package ivy
  :diminish;; doesn't show in the mode-line : detail about modes, minor and major, ...
  :bind (("C-s" . swiper) ;; M-x counsel-find-file
         :map ivy-minibuffer-map
         ("TAB" . ivy-alt-done)
         ("C-s" . ivy-alt-done)
         ("C-t" . ivy-next-line)
         ("C-h" . ivy-previous-line)
         :map ivy-switch-buffer-map
         ("C-h" . ivy-previous-line)
         ("C-s" . ivy-done)
         ("C-d" . ivy-switch-buffer-kill)
         :map ivy-reverse-i-search-map
         ("C-h" . ivy-previous-line)
         ("C-d" . ivy-reverse-i-search-kill))
  :config
  (ivy-mode 1))

(use-package counsel
  :bind (; ("C-M-j" . 'switch-to-buffer) ;'counsel-ibuffer)
         ("C-x b" . 'counsel-switch-buffer)
         ("C-x C-f" . 'counsel-find-file)
         :map minibuffer-local-map
         ("C-r" . 'counsel-minibuffer-history))
  :custom
  (counsel-linux-app-format-function #'counsel-linux-app-format-function-name-only)
  :config
  (counsel-mode 1))

(use-package company
  :after lsp-mode
  :hook (prog-mode . company-mode)
  :bind (:map company-active-map
              ;;("<tab>" . company-complete-selection)
              ("<return>" . company-complete-selection))
  (:map lsp-mode-map
        ("<tab>" . company-indent-or-complete-common))
  :custom
  (company-minimum-prefix-length 1)
  (company-idle-delay 0.0)
  (global-company-mode t)
  )

;; (use-package company-lsp ; obsolete
;;   :after company
;;   :config
;;   (push 'company-lsp company-backends))

;;-----
;; Prescient
;;
(use-package ivy-prescient
  :after counsel
  :config
  (ivy-prescient-mode 1)
  (prescient-persist-mode 1))
(use-package company-prescient
  :after company
  :config
  (company-prescient-mode 1))

;;;;
;;; Make ESC quit prompts
;; (global-set-key (kbd "<escape>") 'keyboard-escape-quit)

(use-package all-the-icons) ;; then call M-x all-the-icons-install-fonts

(use-package doom-modeline
  :ensure t
  :init (doom-modeline-mode 1)
  :custom ((doom-modeline-height 15)))

;; remember cursor position, for emacs 25.1 or later
(save-place-mode 1)

;; open help buffer on the right
(setq split-height-threshold nil)
(setq split-width-threshold 0)
;; other spliting functions
;;(split-window-right)
;;(split-window-horizontally)
;;(split-window-vertically)

(column-number-mode)
(global-display-line-numbers-mode t)

;; Make frame transparency overridable
(defvar efs/frame-transparency '(90 . 90))

;; Set frame transparency
(set-frame-parameter (selected-frame) 'alpha efs/frame-transparency)
(add-to-list 'default-frame-alist `(alpha . ,efs/frame-transparency))
(set-frame-parameter (selected-frame) 'fullscreen 'maximized)
(add-to-list 'default-frame-alist '(fullscreen . maximized))

;; Disable line numbers for some modes
(dolist (mode '(org-mode-hook
                term-mode-hook
                shell-mode-hook
                treemacs-mode-hook
                eshell-mode-hook))
  (add-hook mode (lambda () (display-line-numbers-mode 0))))

(use-package rainbow-delimiters
  :hook (prog-mode . rainbow-delimiters-mode))

(use-package which-key
  :defer 0
  :diminish which-key-mode
  :config
  (which-key-mode)
  (setq which-key-idle-delay 1))

(use-package ivy-rich ; #2 t=20'
  :after ivy
  :init
  (ivy-rich-mode 1)) ; M-o ; M-h

(use-package helpful ; #2 t=36'
  :ensure t
  :commands (helpful-callable helpful-variable helpful-command helpful-key)
  :custom
  (counsel-describe-function-function #'helpful-callable)
  (counsel-describe-variable-function #'helpful-variable)
  :bind
  ([remap describe-function] . counsel-describe-function)
  ([remap describe-command] . helpful-command)
  ([remap describe-variable] . counsel-describe-variable)
  ([remap describe-key] . helpful-key))

;; Themes
;;(use-package doom-themes
;;  :init (load-theme 'doom-Iosvkem t))
;;  :init (load-theme 'doom-acario-dark t))
;; (use-package doom-themes
;;   :init (load-theme 'doom-palenight t))
;; Other themes
;;(load-theme 'tango-dark)
(load-theme 'wombat)
;;(load-theme 'dracula t)
;;(load-theme 'danneskjold t)
;; (use-package doom-themes
;;   :init (load-theme 'doom-dracula t))

;;;;-----
;;;; Keybindings
;;;
;; (global-set-key (kbd "C-M-j") 'counsel-switch-buffer)
;; (define-key emacs-lisp-mode-map (kbd "C-x M-t") 'counsel-load-theme)
;; trick M-: (global-unset-key (kbd "C-M-j"))

(defun indent-buffer ()
  "Indent the buffer."
  (interactive)
  (save-excursion
    (delete-trailing-whitespace)
    (indent-region (point-min) (point-max) nil)
    (untabify (point-min) (point-max))))
(global-set-key [f12] 'indent-buffer)

;;;;-----
;; Package general.el ; example
;; (use-package general)
;; (general-define-key
;;  "C-M-j" 'counsel-switch-buffer)

(use-package general
  :after evil
  :config
  (general-create-definer efs/leader-keys
    :keymaps '(normal insert visual emacs)
    ;; :prefix "SPC"
    :global-prefix "C-;") ; :global-prefix "C-SPC")


  (efs/leader-keys
    "h"  '(:ignore t :which-key "toggles")
    "hh" '(counsel-load-theme :which-key "choose theme")
    "fde" '(lambda () (interactive) (find-file (expand-file-name "~/.emacs.d/Emacs.org")))))

(use-package evil
  :init
  (setq evil-want-integration t)
  (setq evil-want-keybinding nil)
  (setq evil-want-C-u-scroll t)
  (setq evil-want-C-i-jump nil)
  :config
  (evil-mode 1)
  (define-key evil-insert-state-map (kbd "C-g") 'evil-normal-state)
  ;;(define-key evil-insert-state-map (kbd "C-h") 'evil-delete-backward-char-and-join)
  (global-set-key (kbd "C-?") 'help-command) ; former : undefined

  ;; Use visual line motions even outside of visual-line-mode buffers
  (evil-global-set-key 'motion "t" 'evil-next-visual-line)
  (evil-global-set-key 'motion "h" 'evil-previous-visual-line)

  (evil-set-initial-state 'messages-buffer-mode 'normal)
  (evil-set-initial-state 'dashboard-mode 'normal))

(defun my-evil-dvorak-customizations () ; from https://github.com/jbranso/evil-dvorak
  "My helpful evil-dvorak customizations."
  (interactive)
  ;;normal mode customizations
  (evil-define-key 'normal evil-dvorak-mode-map
    (kbd "l") 'recenter-top-bottom
    (kbd "Q") 'anzu-query-replace-regexp)

  ;;insert mode customizations
  (evil-define-key 'insert evil-dvorak-mode-map
    (kbd "C-h") 'evil-previous-line
    (kbd "C-t") 'evil-next-line
    (kbd "C-N") 'evil-backward-word-begin
    (kbd "C-S") 'evil-forward-word-end
    (kbd "C-d") 'delete-char
    (kbd "C-z") 'evil-normal-state)

  (evil-define-key 'visual evil-dvorak-mode-map
    (kbd "o") 'evil-backward-word-begin
    (kbd "e") 'evil-forward-word-begin))

(use-package evil-dvorak
  :ensure t
  :config
  (global-evil-dvorak-mode 1)
  (my-evil-dvorak-customizations))
;; h move the cursor one line up
;; t move the cursor one line down
;; n move the cursor one character to the left
;; s move the cursor one character to the right
;; k kill from point to the end of the line
;; K kill from point to the beginning of the line
;; j join the lower line to the end of this line
;; J join the current line the end of the previous line
;; C-h  insert a new line below point and switch to insert state
;; C-t  insert a new line above point and switch to insert state. The reader should note that this conflicts with the emacs binding of (transpose-chars), which I have personally rebound to (global-set-key (kbd "C-c t") 'transpose-chars)
(global-set-key (kbd "C-c t") 'transpose-chars)

(use-package evil-collection
  :after evil
  :config
  (evil-collection-init))

;;;; Display commands on another buffer
(use-package command-log-mode
  :commands command-log-mode)

(use-package hydra
  :defer t)

(defhydra hydra-text-scale (:timeout 4)
  "scale text"
  ("h" text-scale-increase "in")
  ("t" text-scale-decrease "out")
  ("f" nil "finished" :exit t))

(efs/leader-keys
  "hs" '(hydra-text-scale/body :which-key "scale text"))

;;;;-----
;;;; Projectile #4
;;;
(use-package projectile
  :diminish projectile-mode
  :config (projectile-mode)
  :custom ((projectile-completion-system 'ivy))
  :bind-keymap
  ("C-c p" . projectile-command-map)
  :init
  ;; NOTE: Set this to the folder where you keep your Git repos!
  (when (file-directory-p "~/github/my-repo")
    (setq projectile-project-search-path '("~/github/my-repo" "~/code/")))
  (setq projectile-switch-project-action #'projectile-dired))

(use-package counsel-projectile
  :after projectile
  :config (counsel-projectile-mode))

(use-package magit
  :commands magit-status ; not necessary: use-package does it
  :custom
  (magit-display-buffer-function #'magit-display-buffer-same-window-except-diff-v1))

;; (use-package evil-magit
;;   :after magit)

;; NOTE: Make sure to configure a GitHub token before using this package!
;; - https://magit.vc/manual/forge/Token-Creation.html#Token-Creation
;; - https://magit.vc/manual/ghub/Getting-Started.html#Getting-Started
;; (use-package forge
;;   :after magit)

;;;;-----
;;;; Org-mode
;;;
(defun efs/org-font-setup ()
  ;; Replace list hyphen with dot
  (font-lock-add-keywords 'org-mode
                          '(("^ *\\([-]\\) "
                             (0 (prog1 () (compose-region (match-beginning 1) (match-end 1) "•"))))))

  ;; Set faces for heading levels
  (dolist (face '((org-level-1 . 1.2)
                  (org-level-2 . 1.1)
                  (org-level-3 . 1.05)
                  (org-level-4 . 1.0)
                  (org-level-5 . 1.1)
                  (org-level-6 . 1.1)
                  (org-level-7 . 1.1)
                  (org-level-8 . 1.1)))
    (set-face-attribute (car face) nil :font "Cantarell" :weight 'regular :height (cdr face)))

  ;; Ensure that anything that should be fixed-pitch in Org files appears that way
  (set-face-attribute 'org-block nil    :foreground nil :inherit 'fixed-pitch)
  (set-face-attribute 'org-table nil    :inherit 'fixed-pitch)
  (set-face-attribute 'org-formula nil  :inherit 'fixed-pitch)
  (set-face-attribute 'org-code nil     :inherit '(shadow fixed-pitch))
  (set-face-attribute 'org-table nil    :inherit '(shadow fixed-pitch))
  (set-face-attribute 'org-verbatim nil :inherit '(shadow fixed-pitch))
  (set-face-attribute 'org-special-keyword nil :inherit '(font-lock-comment-face fixed-pitch))
  (set-face-attribute 'org-meta-line nil :inherit '(font-lock-comment-face fixed-pitch))
  (set-face-attribute 'org-checkbox nil  :inherit 'fixed-pitch)
  (set-face-attribute 'line-number nil :inherit 'fixed-pitch)
  (set-face-attribute 'line-number-current-line nil :inherit 'fixed-pitch))

(defun efs/org-mode-setup ()
  (org-indent-mode)
  (variable-pitch-mode 1)
  (visual-line-mode 1))

(use-package org
  :pin org
  :commands (org-capture org-agenda)
  :hook (org-mode . efs/org-mode-setup)
  :config
  (setq org-ellipsis " ▾") ;

  (setq org-agenda-start-with-log-mode t)
  (setq org-log-done 'time)
  (setq org-log-into-drawer t)

  (setq org-agenda-files
        '("~/Projects/Code/emacs-from-scratch/OrgFiles/Tasks.org"
          "~/Projects/Code/emacs-from-scratch/OrgFiles/Habits.org"
          "~/Projects/Code/emacs-from-scratch/OrgFiles/Birthdays.org")))

(use-package org-bullets
  :hook (org-mode . org-bullets-mode)
  :custom
  (org-bullets-bullet-list '("◉" "○" "●" "○" "●" "○" "●")))

(defun efs/org-mode-visual-fill ()
  (setq visual-fill-column-width 100
        visual-fill-column-center-text t)
  (visual-fill-column-mode 1))

(use-package visual-fill-column
  :hook (org-mode . efs/org-mode-visual-fill))

;; (use-package jupyter
;;   :commands (jupyter-run-server-repl
;;              jupyter-run-repl
;;              jupyter-server-list-kernels))

(org-babel-do-load-languages
 'org-babel-load-languages
 '((emacs-lisp . t)
   ;;(julia . t)
   (python . t)
   (ipython . t)
   ;; (jupyter . t) ; needs to be the last
   )
 )

;;;;
;;; Other configuration
(add-hook 'after-save-hook 'executable-make-buffer-file-executable-if-script-p) ; make file executable when starting with a shebang
(electric-pair-mode) ; make pair parentheses, quotes, double quotes, square brackets, bracketsa
(setq python-indent-guess-indent-offset t)
(setq python-indent-guess-indent-offset-verbose nil)


;;;;
;;; Lsp-mode
(use-package lsp-mode
  :init
  (setq lsp-keymap-prefix "C-c l")
  :hook (
         (python-mode . lsp)
         (lsp-mode . lsp-enable-which-key-integration)) ;; which-key integration
  :commands lsp)

(use-package lsp-ui :commands lsp-ui-mode)
;; (use-package lsp-ui ; to test
;;   :hook (lsp-mode . lsp-ui-mode)
;;   :custom
;;   (lsp-ui-doc-position 'bottom))
;; (setq lsp-ui-doc-enable t
;;       lsp-ui-peek-enable t
;;       lsp-ui-sideline-enable t
;;       lsp-ui-imenu-enable t
;;       lsp-ui-flycheck-enable t)

;;(use-package helm-lsp :commands helm-lsp-workspace-symbol)
(use-package lsp-ivy :commands lsp-ivy-workspace-symbol)
(use-package lsp-treemacs :commands lsp-treemacs-errors-list)

(use-package dap-mode ; to test
  :commands dap-debug
  :config
  (dap-mode 1)
  (dap-ui-mode 1) ; enables mouse hover support
  (dap-tooltip-mode 1) ; use tooltips for mouse hover ; if it is not enabled `dap-mode' will use the minibuffer.
  (tooltip-mode 1) ; displays floating panel with debug buttons
  (dap-ui-controls-mode 1)
  (require 'dap-python)
  (require 'dap-hydra)
  (require 'dap-gdb-lldb)
  (dap-gdb-lldb-setup)
  (general-define-key ; Bind `C-c l d` to `dap-hydra` for easy access
   :keymaps 'lsp-mode-map
   :prefix lsp-keymap-prefix
   "d" '(dap-hydra t :wk "debugger"))
  )

(use-package lsp-mode
  :hook (python-mode . lsp-deferred) ; cf. syscrafter
  :commands (lsp lsp-deferred)
  :custom
  (lsp-auto-guess-root nil) ; cf. Zaminski
  (lsp-prefer-flymake nil)
  ;;:bind (:map lsp-mode-map ("C-c C-f" . lsp-format-buffer))
  :hook ((python-mode) . lsp)
  )

;; flycheck syntax checker
(use-package flycheck
  :init (global-flycheck-mode))

(use-package virtualenvwrapper
  :config
  (venv-initialize-interactive-shells)
  (venv-initialize-eshell)
  )
(venv-workon "p3")
(setq lsp-python-executable-cmd "python3")

;;-----
;; Add keywords
;;-----
(font-lock-add-keywords 'fortran-mode
                        '(("%" . 'font-lock-keyword-face)
                          ("::" . 'font-lock-keyword-face)
                                        ;(":" . 'widget-documentation)
                          ("+\\|=\\|+\\|-\\|*\\|/\\|<\\|>" . 'escape-glyph)
                          ("," . 'widget-field)
                          ("(\\|)" . 'secondary-selection)))

(font-lock-add-keywords 'fortran-mode
                        '(("\\<\\(FIXME\\):" 1 'font-lock-warning-face prepend)))
;;                        ("\\<\\(and\\|or\\|not\\|%\\)\\>" . 'font-lock-keyword-face)))

(custom-set-variables
 ;; custom-set-variables was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 '(circe-default-nick "thomasb06")
 '(circe-default-realname "Thomas.B")
 '(circe-default-user "thomasb06")
 '(circe-use-cycle-completion t)
 '(column-number-mode t)
 '(delete-selection-mode 1)
 '(electric-pair-mode t)
 ;;'(global-linum-mode t)
 '(fortran-analyze-depth 0)
 '(fortran-line-length 132)
 '(kill-whole-line t)
 '(scroll-bar-mode nil)
 '(save-place t)
 '(show-paren-mode t)
 ;;'(smtpmail-smtp-server "smtp.univ-cotedazur.fr")
 ;;'(smtpmail-smtp-service 25)
 '(tool-bar-mode nil)
 '(tooltip-mode nil)
 )

(use-package lsp-ltex
  :ensure t
  :hook (text-mode . (lambda ()
                       (require 'lsp-ltex)
                       (lsp))))  ; or lsp-deferred

(defun my-save-and-compile-command ()
  (interactive)
  (save-buffer)
  (setq compile-command (concat "pdflatex -shell-escape " buffer-file-truename))
  (call-interactively 'compile)
  )
(global-set-key (kbd "C-x e") 'my-save-and-compile-command)

(setq compilation-scroll-output "follow")
(setq compilation-always-kill t)

;; .emacs-systemcrafter.el ends here
