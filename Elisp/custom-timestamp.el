;;----------
;;----- Insert time and date -----
;;----------
;;-----
;;----- Generic timestamps
;;-----
(add-hook 'before-save-hook 'time-stamp)
;;-----
;;(require 'timestamp)
;;-----
;;(add-hook 'write-file-functions (lambda (&rest _) (other-update-writestamps writestamp-prefix-enr)))
;;(add-hook 'after-change-functions (lambda (&rest _) (other-update-writestamps writestamp-prefix-mod)))
;;-----
;;----- Fortran timestamps
;;-----
;;(defun my-fortran-time-stamp ()
;;  (set (make-local-variable 'time-stamp-pattern)
;;       "-8/<p>Last modified:[ \t]+%3a %3b %02H:%02M:%02S %Z %:y by %u</p>")
;; (set (make-local-variable 'time-stamp-time-zone) "UTC"))
;;(add-hook 'fortran-mode-hook 'my-fortran-time-stamp)
;;-----
;; (add-hook 'fortran-mode-hook (lambda ()
;;                                (require 'time-stamp) ; not needed
;;                                (set (make-local-variable 'time-stamp-pattern)
;;                                     "-8/!Last modified:[ \t]+%3a %2d %3b %02H:%02M:%02S %Z %:y by %u")
;;                                (set (make-local-variable 'time-stamp-time-zone) "UTC")))
;; (require 'time-stamp)
;; (defun my-fortran-time-stamp ()
;;   (set (make-local-variable 'time-stamp-pattern)
;;        "-8/!     ! Last modified:[ \t]+%3a %3b %02H:%02M:%02S %Z %:y by %u")
;;   (set (make-local-variable 'time-stamp-time-zone) "UTC"))
;; (add-hook 'fortran-mode-hook 'my-fortran-time-stamp)
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
