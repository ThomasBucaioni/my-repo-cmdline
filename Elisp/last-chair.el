(defun last-chair (n)
  (setf a (make-array '(4 3)))
  (dotimes (i 4)
    (dotimes (j 3)
      (setf (aref a i j) (list i 'x j '= (* i j)))))
  (dotimes (i 4)
    (dotimes (j 3)
                                        ;(print n)))
      (print (aref a i j))))

  (print a)

  (defvar b (make-array (list n)))

  (print n)

  (dotimes (i n)
    (progn
      (setf (aref b i) (* i 0))
      (print (aref b i))))
  ;;(write a)
  ;;(write 9)
  (dotimes (i n)
    (dotimes (j n)
      (setf (aref b i j) (list i 'x j '= (* i j)))))
  )

;;(last-chair 10)

(defun last-chair-rec (n)
  (defvar b (make-array (list n)))
  (dotimes (i n)
    (progn
      (setf (aref b i) (* i 0))
      (print (aref b i))))
  (if (= (mod n 2) 1)
      (+ (last-chair-rec (n)))
    (last-chair-rec (n)))
  )


