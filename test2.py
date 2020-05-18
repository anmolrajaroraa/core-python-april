import urllib.request as req
import urllib.parse as parse
import bs4
jobcounter = 0
starting_point = 0
jobs = []
qInput = input("Job title, keywords, or company: ")
lInput = input("City or State: ")
while True:
    # URL = f"https://www.indeed.co.in/jobs?q=python&amp;start={starting_point}"
    URL = f"https://www.indeed.co.in/jobs?"
    URL = URL + parse.urlencode({
        'q': qInput,
        'l': lInput,
        'start': starting_point
    })
    print(URL)
    response = req.urlopen(URL)
    print(response)
    htmlsourcecode = bs4.BeautifulSoup(response, 'lxml')
    jobLists = htmlsourcecode.find_all('div', 'jobsearch-SerpJobCard')
    for job in jobLists:
        # jobs.append(job)
        jobPosting = {
            "title": "",
            "company_name": "",
            "location": "",
            "salary": "",
            "details": [],
            "posted": "",
            "link": ""
        }
        jobcounter += 1
        print(f"Job {jobcounter}")
        jobTitle = job.find('h2', 'title')
        jobLink = jobTitle.find('a')['href']
        # a = jobLink['href']
        jobLink = f"https://www.indeed.co.in{jobLink}"
        jobPosting['link'] = jobLink
        print(jobTitle.text.strip())
        jobPosting['title'] = jobTitle.text.strip()
        company_name = job.find('span', 'company')
        print(company_name.text.strip())
        jobPosting['company_name'] = company_name.text.strip()
        job_location = job.find('div', 'location')
        job_location = job_location if job_location != None else job.find(
            'span', 'location')
        if job_location != None:
            print(job_location.text.strip())
            jobPosting['location'] = job_location.text.strip()
        else:
            print("Location not specified /Remote work available")
            jobPosting['location'] = "Location not specified /Remote work available"
        salary_text = job.find('span', 'salaryText')
        if salary_text != None:
            print(salary_text.text.strip())
            jobPosting['salary'] = salary_text.text.strip()
        else:
            print('Salary not mentioned')
            jobPosting['salary'] = "Salary not mentioned"
        job_detail_list = job.find('ul')
        job_details = job.find_all('li')
        print("Details:")
        for detail in job_details:
            print("-", detail.text.strip())
            jobPosting['details'].append(detail.text.strip())
        job_date = job.find('span', 'date')
        print("Job was offered -", job_date.text.strip())
        jobPosting['posted'] = job_date.text.strip()
        # print(jobPosting)
        jobs.append(jobPosting)
        print("-----------------")
    choice = input("Do you want to see more jobs of same type(Y/N)?")
    if choice != 'y' and choice != 'Y' and choice != 'yes':
        break
    starting_point += 10

flag = True
choice = input("Do you want to see details for some job(Y/N)?")
if choice == 'y' or choice == 'Y' or choice == 'yes':
    while flag == True:
        job_number = int(
            input("Enter job no. for which you want to see details:"))
        job = jobs[job_number - 1]
        jobLink = job['link']
        response = req.urlopen(jobLink)
        sourceCode = bs4.BeautifulSoup(response, 'lxml')
        extraDetails = sourceCode.find_all(
            'span', 'jobsearch-JobMetadataHeader-iconLabel')
        for detail in extraDetails:
            print(detail.text.strip())
        a = input("Do you want to see details of more jobs? (y/n)")
        if a != 'y' and a != 'Y' and a != 'yes':
            flag = False

ch = input("Do you want to compare any two jobs (Y/N)?")
if ch == 'y' or ch == 'Y' or ch == 'yes':
    while True:
        print("Enter the Jobs number")
        job1 = int(input("Job 1:"))
        job2 = int(input("Job 2:"))
        if job1 <= len(jobs) and job2 <= len(jobs):
            break
        print("Please enter valid job number...")
    jobPosting1 = list(jobs[job1 - 1].values())
    # print(jobPosting1)
    jobPosting2 = list(jobs[job2 - 1].values())
    print("Job 1 --- Job 2".center(105))
    for i, j in zip(jobPosting1, jobPosting2):
        if type(i) == list:
            continue
        print(i.center(50), end='')
        print(" --- ", end='')
        print(j.center(50))
