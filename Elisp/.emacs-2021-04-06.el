(require 'package)
(add-to-list 'package-archives
             '("melpa-stable" . "http://stable.melpa.org/packages/") t)
;;----------
(package-initialize)
(package-install 'color-identifiers-mode)
(advice-add 'python-mode :before 'elpy-enable)

(setq desktop-path (list "~/"))
(desktop-save-mode 1)

;;(global-set-key (kbd "\C-a") ctl-x-map) ; 'Caps Lock - q' =  "\C-q"
(define-key key-translation-map (kbd "C-a") (kbd "C-x"))
(define-key key-translation-map (kbd "C-x") (kbd "C-a"))

(setq compilation-read-command nil)
(global-set-key "\C-x\C-m" 'compile)
(custom-set-variables
 ;; custom-set-variables was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 '(circe-default-nick "thomasb")
 '(circe-default-realname "Thomas.B")
 '(circe-default-user "thomasb")
 '(circe-use-cycle-completion t)
 '(column-number-mode t)
 '(delete-selection-mode 1)
 '(electric-pair-mode t)
 '(elpy-rpc-python-command "python3")
 '(fortran-analyze-depth 0)
 '(fortran-line-length 132)
 '(global-linum-mode t)
 '(icomplete-mode t)
 '(kill-whole-line t)
 '(package-selected-packages
   (quote
    (elpy gnuplot magit multiple-cursors idle-highlight-mode color-identifiers-mode auto-complete dracula-theme)))
 '(save-place t)
 '(scroll-bar-mode nil)
 '(send-mail-function (quote smtpmail-send-it))
 '(show-paren-mode t)
 '(smtpmail-smtp-server "smtp.univ-cotedazur.fr")
 '(smtpmail-smtp-service 25)
 '(tool-bar-mode nil)
 '(tooltip-mode nil))
(add-to-list 'load-path "~/.emacs.d/lisp/")
;;-----
(require 'wgrep)
;;-----
(require 'fill-column-indicator)
(setq fci-rule-width 1)
(setq fci-rule-color "orange")
(setq-default fill-column 132)
(add-hook 'fortran-mode-hook #'fci-mode)
(fci-mode)
(fci-mode)
(fci-mode)
;;-----
(require 'multiple-cursors)
(global-set-key (kbd "C-S-c C-S-c") 'mc/edit-lines)
(global-set-key (kbd "C->") 'mc/mark-next-like-this)
(global-set-key (kbd "C-<") 'mc/mark-previous-like-this)
(global-set-key (kbd "C-c C-<") 'mc/mark-all-like-this)

;;-----
(custom-set-faces
 ;; custom-set-faces was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 '(default ((t (:family "DejaVu Sans Mono" :foundry "PfEd" :slant normal :weight normal :height 83 :width normal)))))

;;-----
;;(find-file "~/myfile")
;;(revert-buffer "~/myfile")

;;----------
(setq compile-command (concat "pdflatex " buffer-file-truename)) ;; original: `(setq ... "make package install")'
;;-----
;; (global-set-key (kbd "C-x e") 'compile) ; compile without saving
;;-----
;; Compile with automatic saving, from https://www.masteringemacs.org/article/mastering-key-bindings-emacs
;;--
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
;;-----

(setq compilation-scroll-output "follow")
(setq compilation-always-kill t)

;;-----
;; Helper for compilation. Close the compilation window if
;; there was no error at all.
(defun compilation-exit-autoclose (status code msg)
  ;; If M-x compile exists with a 0
  (when (and (eq status 'exit) (zerop code))
    ;; then bury the *compilation* buffer, so that C-x b doesn't go there
    (bury-buffer)
    ;; and delete the *compilation* window
    (delete-window (get-buffer-window (get-buffer "*compilation*"))))
  ;; Always return the anticipated result of compilation-exit-message-function
  (cons msg code))
;; Specify my function (maybe I should have done a lambda function)
(setq compilation-exit-message-function 'compilation-exit-autoclose)
;;----------

;;-----
(defun indent-buffer ()
  (interactive)
  (save-excursion
    (delete-trailing-whitespace)
    (indent-region (point-min) (point-max) nil)
    (untabify (point-min) (point-max))))
(global-set-key [f12] 'indent-buffer)

;;----------------------------------------
;; Règle la taille du cadre (i.e. 'frame')
(add-to-list 'default-frame-alist '(fullscreen . maximized))
;;(setq default-frame-alist '((left . 0) (width . 65) (fullscreen . fullheight)))
;;----------------------------------------

(setq inhibit-startup-screen t)
(menu-bar-mode -1)

(load-theme 'dracula t)

(defun my-count-words-buffer () ; test Elisp
  (interactive)
  (let ((count 0))
    (goto-char (point-min))
    (while (< (point) (point-max))
      (forward-word 1)
      (setq count (1+ count)))
    (message "le buffer contient %d mots." count)))

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

;;-----
;; Replace regexps
;;-----
;; From https://www.emacswiki.org/emacs/QueryExchange
(defun query-exchange (string-1 string-2 &optional delimited start end)
  "Exchange string-1 and string-2 interactively.
The user is prompted at each instance like query-replace."
  (interactive
   (let ((common
          (query-replace-read-args
           (concat "Query replace"
                   (if current-prefix-arg " word" "")
                   " regexp"
                   (if (and transient-mark-mode mark-active) " in region" ""))
           t)))
     (list (nth 0 common) (nth 1 common) (nth 2 common)
           ;; These are done separately here
           ;; so that command-history will record these expressions
           ;; rather than the values they had this time.
           (if (and transient-mark-mode mark-active)
               (region-beginning))
           (if (and transient-mark-mode mark-active)
               (region-end)))))

  (perform-replace
   (concat "\\(" string-1 "\\)\\|" string-2)
   '(replace-eval-replacement replace-quote
                              (if (match-string 1) string-2 string-1))
   t t delimited nil nil start end))

;;----------
;;----- Redefine keybindings
;;----------
(global-set-key (kbd "C-S-o") 'isearch-forward-symbol-at-point)
;; (kbd "C-o") ; former : 'open-line
(global-set-key (kbd "C-o") 'other-window) ; former : 'open-line
(global-set-key (kbd "C-?") 'help-command) ; former : undefined
(global-set-key (kbd "C-? /") 'describe-key) ; former : undefined
(global-set-key (kbd "C-,") 'kill-buffer) ; former : undefined
;; (global-set-fkey (kbd "M-,") 'next-buffer) ; former: xref-pop-marker-stack
(global-set-key (kbd "C-\\") 'yank) ;; former : toggle-input-method
(global-set-key (kbd "C-|") 'yank-pop) ; former : undefined
(global-set-key (kbd "C-;") 'kill-line) ; former : undefined
(global-set-key (kbd "C-x f") 'find-file) ; former : set-fill-column
;; (global-set-key (kbd "C-b") 'switch-to-buffer) ; former : backward-char
(global-set-key (kbd "C-'") 'save-buffer) ; former : undefined
(global-set-key (kbd "C-\"") 'switch-to-buffer) ; former : undefined
(global-set-key (kbd "C-=") 'kill-region) ; former : undefined
(global-set-key (kbd "C-+") 'kill-ring-save) ; former : undefined
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
;;----------
;;----- End redefine keybindings
;;----------

;;----------
;;----- Check symlink files
;;----------
(defun read-only-if-symlink ()
  (if (file-symlink-p buffer-file-name)
      (progn
        (setq buffer-read-only t)
        (message "File is a symlink."))))
(add-hook 'find-file-hooks 'read-only-if-symlink)

;;----------
;;----- Insert time and date -----
;;----------
;;-----
;;----- Generic timestamps
;;-----
(add-hook 'before-save-hook 'time-stamp)
;;-----
;;----- C timestamps
;;-----
(add-hook 'c-mode-hook (lambda ()
                         (require 'time-stamp)
                         (set (make-local-variable 'time-stamp-pattern)
                              "8/\/\* Last modified:[ \t]+%3a %2d %3b %02H:%02M:%02S %Z %:y by %u\*\/")
                         (set (make-local-variable 'time-stamp-time-zone) "UTC")))
;;----------
;;----- end writestamps -----
;;----------

;;;;----------
;;;;----- IRC -----
;;;;----------
(add-to-list 'load-path "~/.emacs.d/lisp/circe/")
(require 'circe)
;;-
;; This defines the password variables below
;;(when (file-exists-p "~/.emacs.d/lisp/circe/.private.el")
;;  (load-file "~/.emacs.d/lisp/circe/.private.el"))
;;-----
;; Safer password management
(setq auth-sources '("~/.emacs.d/lisp/circe/.authinfo.gpg"))
;;-
(defun my-fetch-password (&rest params)
  (require 'auth-source)
  (let ((match (car (apply 'auth-source-search params))))
    (if match
        (let ((secret (plist-get match :secret)))
          (if (functionp secret)
              (funcall secret)
            secret))
      (error "Password not found for %S" params))))
;;-
(defun my-nickserv-password (server)
  (my-fetch-password :login "forcer" :machine "irc.freenode.net"))
;;-----
;; Network Configuration
(setq circe-network-options
      '(("Freenode"
         :tls t
         :nick "thomasb"
         :sasl-username "thomasb"
         :sasl-password my-nickserv-password
         :nickserv-password my-nickserv-password ; Join Channels requiring Identification
         :channels (:after-auth "#emacs-circe" "#emacs")
         :reduce-lurker-spam t
         )))
;; Hiding the Join/Part Spam
;; (setq circe-reduce-lurker-spam t)
;; Hiding Other Messages
;; (circe-set-display-handler "JOIN" (lambda (&rest ignored) nil))
;;-----
;; Tab Completion
(setq circe-use-cycle-completion t)
;;-----
;; Automatic Pasting
(require 'lui-autopaste) ; just in case it doesn't work, add to see: (enable-lui-track)
(add-hook 'circe-channel-mode-hook 'enable-lui-autopaste)
;;-----
;; Topic Diffs
(setq circe-format-server-topic "*** Topic change by {userhost}: {topic-diff}")
;;-----
;; Channel Name in the Prompt
(add-hook 'circe-chat-mode-hook 'my-circe-prompt)
(defun my-circe-prompt ()
  (lui-set-prompt
   (concat (propertize (concat (buffer-name) "-->")
                       'face 'circe-prompt-face)
           " ")))
;;-----
;; Aligning nick names and messages
(setq circe-format-say "{nick:-16s} {body}")
;;-----
;; Format (colors, ...)
(require 'circe-color-nicks)
(enable-circe-color-nicks)
(require 'lui-track)
(enable-lui-track)
(require 'lui-irc-colors)
(enable-lui-irc-colors)
(require 'lui-logging)
(enable-lui-logging)
;;-----
;; Quick IRC Command
(defun circe-network-connected-p (network)
  "Return non-nil if there's any Circe server-buffer whose
`circe-server-netwok' is NETWORK."
  (catch 'return
    (dolist (buffer (circe-server-buffers))
      (with-current-buffer buffer
        (if (string= network circe-server-network)
            (throw 'return t))))))
;;-
(defun circe-maybe-connect (network)
  "Connect to NETWORK, but ask user for confirmation if it's
already been connected to."
  (interactive "sNetwork: ")
  (if (or (not (circe-network-connected-p network))
          (y-or-n-p (format "Already connected to %s, reconnect?" network)))
      (circe network)))
;;-
(defun irc ()
  "Connect to IRC."
  (interactive)
  (circe-maybe-connect "Freenode"))
;;-
;;(circe "Freenode")
;;(circe "sarg" "23523" "IRCnet" muh-passwd)
;;(circe "localhost" "6668" "bitlbee"))
;;-----
;; Notifications

(setq tracking-ignored-buffers '("#emacs")) ; untrack the channel
(setq tracking-ignored-buffers '(("#emacs" circe-highlight-nick-face))) ; track the channel when nick mentionned

(eval-after-load 'circe
  '(progn
     (defadvice circe-command-SAY (after jjf-circe-unignore-target)
       (let ((ignored (tracking-ignored-p (current-buffer) nil)))
         (when ignored
           (setq tracking-ignored-buffers
                 (remove ignored tracking-ignored-buffers))
           (message "This buffer will now be tracked."))))
     (ad-activate 'circe-command-SAY)))

(defadvice tracking-shorten (around tracking-shorten-aggressively)
  (let ((shorten-join-function #'shorten-join-sans-tail))
    ad-do-it))
(ad-activate 'tracking-shorten)

(require 'notifications)
(require 's)

(defvar tom/chatnotification nil
  "ID of the last send desktop notification.")
(defvar tom/lastchatnotification 0
  "Time of the last send notification, seconds since epoch as float")
(defvar tom/lastbufferlist nil
  "The value of tracking-buffers when we last notified")
(defvar tom/chatnotifyintervall 90
  "Minimum delay between chat activity notifications in seconds")

(defun tom/replace-html-chars (text)
  "Replace < to &lt; and other chars in TEXT."
  (save-restriction
    (with-temp-buffer
      (insert text)
      (goto-char (point-min))
      (while (search-forward "&" nil t) (replace-match "&amp;" nil t))
      (goto-char (point-min))
      (while (search-forward "<" nil t) (replace-match "&lt;" nil t))
      (goto-char (point-min))
      (while (search-forward ">" nil t) (replace-match "&gt;" nil t))
      (buffer-string))))

(defadvice tracking-add-buffer (after tracking-desktop-notify activate)
  (let ((current-t (float-time))
        (current-bl (s-join "\n" tracking-buffers)))
    ;; min tom/chatnotifyintervall seconds since last delay?
    (if (and (not (eql current-bl "")) (not (eql current-bl tom/lastbufferlist))
             (> (- current-t tom/lastchatnotification) tom/chatnotifyintervall))
        (progn
          ;; delete alst notification id any
          (and tom/chatnotification (notifications-close-notification tom/chatnotification))
          ;; remember time and notify
          (setq  tom/lastchatnotification current-t
                 tom/lastbufferlist current-bl
                 tom/chatnotification (notifications-notify
                                       :title "Emacs Active Buffers"
                                       :body (tom/replace-html-chars current-bl)
                                       :timeout 750
                                       :desktop-entry "emacs24"
                                       :sound-name "message-new-entry"
                                       :transient))))))
;;-
;; Notifications from "https://github.com/eqyiel/circe-notifications"
;; (add-to-list 'load-path "~/.emacs.d/lisp/circe-notifications")
;; (autoload 'enable-circe-notifications "circe-notifications" nil t)
;;
;; (eval-after-load "circe-notifications"
;;   '(setq circe-notifications-watch-strings
;;          ;;      '("people" "you" "like" "to" "hear" "from")))
;;
;; (add-hook 'circe-server-connected-hook 'enable-circe-notifications)
;;-----
;; Circe line length
(setq circe-split-line-length 400) ; by default
(setq
 lui-time-stamp-position 'right-margin
 lui-fill-type nil)
;;-
(add-hook 'lui-mode-hook 'my-lui-setup)
(defun my-lui-setup ()
  (setq
   fringes-outside-margins t
   right-margin-width 7
   word-wrap t
   wrap-prefix "    "))
;;-----
;; Nick appears
(setq circe-format-self-say "<{nick}> {body}")
;;-----
;; Spellchecker
(setq lui-flyspell-p t
        lui-flyspell-alist '(("#hamburg" "german8")
                             (".*" "american")))
;;;;----------
;;;;----- end IRC -----
;;;;----------

;;;;----------
;;;;-----
;;; Sometimes, terminals send escape sequences not defined in their              
;;; terminfo/termcap definitions. The solution is to either fix those            
;;; definitions, which is a PITA, or to tell Emacs to understand them            
;;; better.                                                                      
;;;                                                                              
;;; In this piece of code, both entries in those lists are read using            
;;; the `kbd' macro. To add keys, you can use C-q <key> to enter the             
;;; escape sequence on the left, and use whatever key you want it to be          
;;; mapped to on the right. Running Emacs in X and using C-h k for that          
;;; key usually gives the "canonical" Emacs name.                                
;; (mapc (lambda (map)
;;         (define-key function-key-map
;;           (read-kbd-macro (car map))
;;           (read-kbd-macro (cadr map))))
;;       '(("^[[1;2A" "<S-up>")
;;         ("^[[1;2B" "<S-down>")
;;         ("^[[1;2C" "<S-right>")
;;         ("^[[1;2D" "<S-left>")

;;         ("^[[1;3A" "<M-up>")
;;         ("^[[1;3B" "<M-down>")
;;         ("^[[1;3C" "<M-right>")
;;         ("^[[1;3D" "<M-left>")

;;         ("^[[1;4A" "<M-S-up>")
;;         ("^[[1;4B" "<M-S-down>")
;;         ("^[[1;4C" "<M-S-right>")
;;         ("^[[1;4D" "<M-S-left>")

;;         ("^[[1;5A" "<C-up>")
;;         ("^[[1;5B" "<C-down>")
;;         ("^[[1;5C" "<C-right>")
;;         ("^[[1;5D" "<C-left>")

;;         ("^[[5~"   "<prior>")
;;         ("^[[6~"   "<next>")
;;         ("^[[5;5~" "<C-prior>")
;;         ("^[[6;5~" "<C-next>")

;;         ))


;;;;----------
;;;;----------
;; Dired mode
;;;;-----
(put 'dired-find-alternate-file 'disabled nil)


;;;;----------
;;;;----------
;; Set transparency of emacs
;;;;-----
 (defun transparency (value)
   "Sets the transparency of the frame window. 0=transparent/100=opaque"
   (interactive "nTransparency Value 0 - 100 opaque:")
   (set-frame-parameter (selected-frame) 'alpha value))


;;;;----------
;;;;----------
;; Make executable if Shebang
;;;;-----
(add-hook 'after-save-hook 'executable-make-buffer-file-executable-if-script-p)


;;;;----------
;;;;----------
;; Use the Python standard interpreter (default):
;;-----
;; (setq python-shell-interpreter "python3"
;;       python-shell-interpreter-args "-i")
;;-----
;; Use Jupyter console (recommended for interactive Python)
;;;;-----
(start-process-shell-command "myprocessvirtualenv" "mybuffervirtualenv" "virtualenv ~/code/jupyterenvironment")
(start-process-shell-command "myprocesssource" "mybuffersource" "source ~/code/jupyterenvironment/bin/activate")
(setq python-shell-interpreter "~/code/jupyterenvironment/bin/jupyter"
      python-shell-interpreter-args "console --simple-prompt"
      python-shell-prompt-detect-failure-warning nil)
;;(setq python-shell-completion-native-disabled-interpreters ("jupyter")) ; with-eval-after-load ; add-to-list
(with-eval-after-load 'python-shell-completion-native-disabled-interpreters "jupyter") ; with-eval-after-load ; add-to-list
;;-----
;; Use IPython:
;;-----
;; (setq python-shell-interpreter "ipython"
;;       python-shell-interpreter-args "-i --simple-prompt")
;; ;; Note that various issues with plotting have been reported when running IPython 5 in Emacs under Windows. We recommend using Jupyter console instead.
;; ;; If you have an older version of IPython and the above code does not work for you, you may also try:
;; (setenv "IPY_TEST_SIMPLE_PROMPT" "1")
;; (setq python-shell-interpreter "ipython"
;;       python-shell-interpreter-args "-i")


;;;;----------
;;;;----------
;; Emacs tricks
;;;;-----
;; M-g C-h : help to find a line a point
;; C-s M-p : search previous item
;; M-x ielm : execute elisp
;; M-p and M-n : in minibuffer, in ielm and in
;; C-r b l m : jump to bookmark, list the bookmarks, add a bookmark
;; C-l : scroll cursor to top, middle, or bottom position
;; M-r : move cursor to top, middle, or botom postion
;;;;----------
;;;;----------
