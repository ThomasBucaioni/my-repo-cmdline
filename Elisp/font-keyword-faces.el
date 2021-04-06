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
