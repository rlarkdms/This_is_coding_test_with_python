def re_function(i):
  if i ==100:
    return 
  print("%d번쨰 반복입니다." %i)
  re_function(i+1)

re_function(1)