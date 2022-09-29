from MRE import Job
from locations import directory

input = directory('\WebsiteEjer5\input')



# A ---------------------------------------------
# outputUserPage = directory('\WebsiteEjer5\outputA\outputUserPage')
# outputFinal = directory('\WebsiteEjer5\outputA\outputFinal')

# def fmapUserPage(key, value, context):
#   id_user = key
#   id_page, time = value.split("\t")

#   context.write((id_user, id_page), time)

# def fredUserPage(key, values, context):
#   c = 0
#   for v in values:
#     c += int(v)
#   context.write(key, c)
  
# def fmapFinal(key, value, context):
#   id_user = key
#   id_page, time_acum = value.split("\t")
  
#   context.write(id_user, (id_page, time_acum))
  
# def fredFinal(key, values, context):
#   max_time = 0
#   max_page = ""
#   for v in values:
#     if(int(v[1]) > max_time):
#       max_time = int(v[1])
#       max_page = v[0]
  
#   context.write(key, (max_page, max_time))

# jobUserPage = Job(input, outputUserPage, fmapUserPage, fredUserPage)
# jobUserPage.setCombiner(fredUserPage)
# jobUserPage.waitForCompletion()

# jobFinal = Job(outputUserPage, outputFinal, fmapFinal, fredFinal)
# jobFinal.setCombiner(fredFinal)
# jobFinal.waitForCompletion()
# A ---------------------------------------------




# B ---------------------------------------------
# outputVisitedPages = directory('\WebsiteEjer5\outputB\outputVisitedPages')
# outputCountPagesByUser = directory('\WebsiteEjer5\outputB\outputCountPagesByUser')
# outputMaxUser = directory('\WebsiteEjer5\outputB\outputMaxUser')

# # Remove duplicated pages
# def fmapVisitedPages(key, value, context):
#   id_user = key
#   id_page, time = value.split("\t")

#   context.write((id_user, id_page), 1)

# def fredVisitedPages(key, values, context):
#   id_user, id_page = key
#   c = 0
#   # Puedo omitir directamente el for?
#   for v in values:
#     c += int(v)
#   context.write(id_user, id_page)
  

# # Count pages by user
# def fmapCountPagesByUser(key, value, context):
#   id_user = key
#   context.write(id_user, 1)
  
# def fredCountPagesByUser(key, values, context):
#   c = 0  
#   for v in values:
#     c += v
#   context.write(key, c) 

# # User than visited more pages
# def fmapMaxUser(key, value, context):
#   context.write(1, (key, value))
  
# def fcomMaxUser(key, values, context):
#   max_id_user = 0
#   max_quantity = 0
#   for v in values:
#     if (int(v[1]) > max_quantity):
#       max_id_user = v[0]
#       max_quantity = int(v[1])
#   context.write(1, (max_id_user, max_quantity))
  
# def fredMaxUser(key, values, context):
#   max_id_user = 0
#   max_quantity = 0
#   for v in values:
#     if (int(v[1]) > max_quantity):
#       max_id_user = v[0]
#       max_quantity = int(v[1])
#   context.write(max_id_user, max_quantity)
  

# # Jobs
# jobVisitedPages = Job(input, outputVisitedPages, fmapVisitedPages, fredVisitedPages)
# jobVisitedPages.waitForCompletion()


# jobCountPagesByUser = Job(outputVisitedPages, outputCountPagesByUser, fmapCountPagesByUser, fredCountPagesByUser)
# jobCountPagesByUser.setCombiner(fredCountPagesByUser)
# jobCountPagesByUser.waitForCompletion()


# jobMaxUser = Job(outputCountPagesByUser, outputMaxUser, fmapMaxUser, fredMaxUser)
# jobMaxUser.setCombiner(fcomMaxUser)
# jobMaxUser.waitForCompletion()
# B ---------------------------------------------




# B ---------------------------------------------
outputVisitedPages = directory('\WebsiteEjer5\outputB\outputVisitedPages')
outputCountPagesByUser = directory('\WebsiteEjer5\outputB\outputCountPagesByUser')
outputMaxUser = directory('\WebsiteEjer5\outputB\outputMaxUser')

# Remove duplicated pages
def fmapVisitedPages(key, value, context):
  id_user = key
  id_page, time = value.split("\t")

  context.write((id_user, id_page), 1)

def fredVisitedPages(key, values, context):
  id_user, id_page = key
  c = 0
  # Puedo omitir directamente el for?
  for v in values:
    c += int(v)
  context.write(id_user, id_page)
  

# Count pages by user
def fmapCountPagesByUser(key, value, context):
  id_user = key
  context.write(id_user, 1)
  
def fredCountPagesByUser(key, values, context):
  c = 0  
  for v in values:
    c += v
  context.write(key, c) 

# User than visited more pages
def fmapMaxUser(key, value, context):
  context.write(1, (key, value))
  
def fcomMaxUser(key, values, context):
  max_id_user = 0
  max_quantity = 0
  for v in values:
    if (int(v[1]) > max_quantity):
      max_id_user = v[0]
      max_quantity = int(v[1])
  context.write(1, (max_id_user, max_quantity))
  
def fredMaxUser(key, values, context):
  max_id_user = 0
  max_quantity = 0
  for v in values:
    if (int(v[1]) > max_quantity):
      max_id_user = v[0]
      max_quantity = int(v[1])
  context.write(max_id_user, max_quantity)
  

# Jobs
jobVisitedPages = Job(input, outputVisitedPages, fmapVisitedPages, fredVisitedPages)
jobVisitedPages.waitForCompletion()


jobCountPagesByUser = Job(outputVisitedPages, outputCountPagesByUser, fmapCountPagesByUser, fredCountPagesByUser)
jobCountPagesByUser.setCombiner(fredCountPagesByUser)
jobCountPagesByUser.waitForCompletion()


jobMaxUser = Job(outputCountPagesByUser, outputMaxUser, fmapMaxUser, fredMaxUser)
jobMaxUser.setCombiner(fcomMaxUser)
jobMaxUser.waitForCompletion()
# B ---------------------------------------------

