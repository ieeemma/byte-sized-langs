fac {
  dup
  { dup 1 - fac * }
  { pop 1 }
  if
}

main {
  5 fac { result } =
  result print
}
