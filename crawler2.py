import urllib.request as req
import bs4

startingPoint = 0
jobCounter = 0
jobs = []
while True:
    URL = f"https://www.indeed.co.in/jobs?q=python&start={startingPoint}"
    print(URL)
    response = req.urlopen(URL)
    htmlSourceCode = bs4.BeautifulSoup(response, "lxml")  # lxml is html parser
    # print(htmlSourceCode)
    jobsList = htmlSourceCode.find_all('div', 'jobsearch-SerpJobCard')
    # print(job)
    for job in jobsList:
        jobs.append(job)
        jobCounter += 1
        print(f"Job {jobCounter}")

        jobTitle = job.find('h2', 'title')
        print(jobTitle.text.strip())

        companyName = job.find('span', 'company')
        print(companyName.text.strip())

        jobLocation = job.find('div', 'location')
        jobLocation = jobLocation if jobLocation != None else job.find(
            'span', 'location')
        print(jobLocation.text.strip()) if jobLocation != None else print(
            "Location not specified / Only remote work available")

        salaryText = job.find('span', 'salaryText')
        print(salaryText.text.strip()) if salaryText != None else print(
            "Salary not specified")

        jobDetailsList = job.find('ul')
        jobDetails = jobDetailsList.find_all('li')
        print("Details:")
        for detail in jobDetails:
            print(" - ", detail.text.strip())

        print("----------------------------------")

    choice = input("Do you want to see more jobs(Y/N): ")
    if choice != 'y' and choice != 'Y' and choice != "yes":
        break
    startingPoint += 10

choice = input("Do you want to see details for some job(Y/N): ")
if choice == 'y' or choice == 'Y' or choice == 'yes':
    while True:
        jobNumber = int(
            input("Enter job number for which you want to see details: "))
        job = jobs[jobNumber - 1]
        # print(job)
        jobTitle = job.find('h2', 'title')
        jobLink = jobTitle.find('a')
        print(f"https://www.indeed.co.in{jobLink['href']}")
