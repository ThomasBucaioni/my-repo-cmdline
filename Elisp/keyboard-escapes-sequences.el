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
