# METHOD 1 | create a new dictionary for counting the occurances
#          | 1 - results array



def tournamentWinner(competitions, results):
  res_dict = {}
  for idx in range(len(competitions)):
    try:
      res_dict[competitions[idx][1 - results[idx]]] += 3
    except:
      res_dict[competitions[idx][1 - results[idx]]] = 3
  
  max_val = -1
  res_place = ""
  
  for key in res_dict:
    if(res_dict[key] > max_val):
      max_val = res_dict[key]
      res_place = key 
  
  return res_place

print (tournamentWinner([
    ["C#", "C#"],
    ["C#", "C#"],
    ["Python", "HTML"]
  ], [0,0,1]))