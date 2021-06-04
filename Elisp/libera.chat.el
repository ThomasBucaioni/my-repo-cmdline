(defun start-irc (nick)
  (interactive "sTell me your nick please: ")
  (setq erc-track-shorten-start 8
        erc-kill-buffer-on-part t
        erc-auto-query 'bury
        erc-hide-list '("JOIN" "PART" "QUIT")
        erc-network-hide-list '(("irc.libera.chat" "JOIN" "PART" "QUIT"))
        erc-channel-hide-list '(("#emacs" "JOIN" "PART" "QUIT"))
        erc-rename-buffers t
        erc-autojoin-channels-alist '(("libera.chat" "#emacs"))
        erc-interpret-mirc-color t
        erc-modules '(autojoin button completion fill irccontrols list match menu move-to-prompt netsplit networks noncommands notifications readonly ring stamp track truncate))
  (erc-tls :server "irc.libera.chat"
           :port 6697
           :nick nick
           :full-name "emacs-user"))
;; echo "machine irc.libera.chat login <nick> password <password>" >> ~/.authinfo
