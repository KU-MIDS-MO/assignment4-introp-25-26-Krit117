import numpy as np
def mask_and_classify_scores(arr):
   if not isinstance(arr, np.ndarray):
      return None
   if arr.ndim != 2:
      return None
   if arr.shape[0] != arr.shape[1]:
      return None
   n= arr.shape[0]
   if n>4:
      return None
   arrcopy=arr.copy()
   arrcopy[arrcopy<0]= 0
   arrcopy[arrcopy>100]= 100
   levels= np.zeros_like(arrcopy, dtype=int)
   levels[arrcopy >= 70] = 2
   levels[arrcopy>= 40] = 1
   pass_score_per_row= np.zeros(n, dtype=int)
   for i in range(n):
       for j in range(n):
           if arrcopy[i,j]>= 50:
              pass_score_per_row[i] +=1
              return arrcopy,levels,pass_score_per_row
    