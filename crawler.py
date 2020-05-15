import urllib.request as req
import bs4

URL = "https://www.indeed.co.in/python-jobs"
response = req.urlopen(URL)
htmlSourceCode = bs4.BeautifulSoup(response, "lxml")  # lxml is html parser
# print(htmlSourceCode)
jobsList = htmlSourceCode.find_all('div', 'jobsearch-SerpJobCard')
# print(job)
for job in jobsList:
    jobTitle = job.find('h2', 'title')
    print(jobTitle.text.strip())
    companyName = job.find('span', 'company')
    print(companyName.text.strip())
    jobLocation = job.find('div', 'location')
    print(jobLocation.text.strip())
    print("----------------------------------")
