
(= and (macro (x y)
  (list (quote if) x y 0)))

(= t? (lambda (a b) (== (type a) b)))

(= pair? (lambda (x) (t? x (quote list))))

(= index (lambda (i xs)
    (if (== i 0)
        (car xs)
        (index (- i 1) (cdr xs)))))

(= tagged? (lambda (x tag)
    (and (pair? x) (== (car x) tag))))

(= sum? (lambda (x) (tagged? x (quote +))))

(= prod? (lambda (x) (tagged? x (quote *))))

(= sum (lambda (x y)
    (if (== x 0)
        y
    (if (== y 0)
        x
        (list (quote +) x y)))))

(= prod (lambda (x y)
    (if (== x 0)
        0
    (if (== x 1)
        y
    (if (== y 0)
        0
    (if (== y 1)
        x
        (list (quote *) x y)))))))

(= lhs (lambda (x) (index 1 x)))

(= rhs (lambda (x) (index 2 x)))

(= derive (lambda (exp var)
    (if (t? exp (quote int))
        0
    (if (t? exp (quote str))
        (if (== exp var) 1 0)
    (if (sum? exp)
        (sum (derive (lhs exp) var)
            (derive (rhs exp) var))
    (if (prod? exp)
        (sum (prod
                (lhs exp)
                (derive (rhs exp) var))
            (prod
                (derive (lhs exp) var)
                (rhs exp)))

    (do
        (print (quote unknown-expr-type))
        (print exp)
        (exit 1))))))))

(= exp (quote
    (+ (* y y) (* x y))))

(print (derive exp (quote y)))
