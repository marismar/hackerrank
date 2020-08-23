def gradingStudents(grades):
  for i in range(0,len(grades)):
    if (grades[i] >= 38) and ((int(grades[i]/5) + 1) * 5 <= grades[i] + 2):
        grades[i] = (int(grades[i]/5) + 1) * 5
          
  return grades