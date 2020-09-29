def timeConversion(s):
  hour, minute, second = (s.split(':'))
  period = second[2:4]
  second = second[0:2]

  if hour != '12':
    if period == 'PM':
      hour = int(hour) + 12
  else:
    if period == 'AM':
      hour = '00'

  return('{hh}:{mm}:{ss}'.format(hh = hour, mm = minute, ss = second))




