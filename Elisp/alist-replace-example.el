;;---------------
;;-----
;;----------
;;-----
;; OK
;;-----
(setq e-addrs
      '(("robin" . "rl@sherwood.uk")
        ("marian" . "mf@sherwood.uk")))
;;-----
(message "%S" e-addrs)
;;-----
(defun alist-replace (alist key new-value)
  (message "In : %S" alist)
  (let ((sublist (assoc key alist)))
    (when sublist
      (message "sublist : %S" sublist)
      (setcdr sublist new-value)
      (message "sublist modified : %S" sublist))))
;;-----
(alist-replace e-addrs "robin" "johnl@exile.fr")
;;-----
(message "%S" e-addrs)
;;-----
;;----------
;;---------------
;;----------
;;-----
;; ?
;;-----
(let ((alist '((key . nil))))
  (setcdr (assoc 'key alist) 'value)
  alist)
;;-----
;;----------
;;-----
;;---------------
;;-----
;;----------
;;-----
;; Other technique
;;-----
(defun alist-replace (alist key new-value)
  (setcdr (assoc key alist) new-value))
;;-----
;;----------
;;-----
;;---------------
