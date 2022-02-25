""""
hashcode 2022
team Zlabiya
Algeria developers / ZeD_OnE and cr105ph1nx
"""

class hashcode:
    def __init__(self,cont,projects,name,namePro):
        """
        entrier of the hashcode test must be included in the script
        """
        self.completed = [] #possible done works
        self.cont = cont
        self.projects = projects
        self.name = name
        self.namePro = namePro
    def variables(self):
        """
        using local variables as a database
        :return:
        """
        self.projects
        """
        output: {
        'projectOne':{'day':7,'score':10,'bd':4,'rls':1,'req':[['c++','2']]}
        'projectTwo':{'day':7,'score':5,'bd':4,'rls':2,'req':[['c++','2'],['py','5']]}
        }
        """
        self.cont
        """
        output: {
        'anna':[[c++,2]]
        'bob':[['c++',2],['py',9]]
        }
        """
        self.namePro
        """
        output: ['projectOne','projectTwo']
        """
        self.name
        """
        output: ['inna','bob']
        """
        self.completed
        """
        Completed projects not needed to get checked again
        output: ['projectOne','projectTwo']
        """
    def worker(self,namePro):
        """
        solving the main problem
        :return status
        """
        check = True
        contName= 0
        required = list(self.projects[namePro]["req"])
        self.names = self.name.copy()
        Sname = ''
        for i in range(int(self.projects[namePro]["rls"])):
            for name in self.names:
                    m = 0
                    for j in self.cont[name]:
                        if len(required)!=0:
                            if j[0] in required[0][0]:
                                if int(j[1])>=int(required[0][1]):
                                    contName = contName+1               #c++:anna , html:bob
                                    Sname = Sname+name+" "
                                    self.projects[namePro]["inv"] = Sname
                                    if j[1]==int(required[0][1]):
                                        self.cont[name][m][1] = self.cont[name][m][1] + 1
                                    self.names.remove(name)
                                    required.remove(required[0])
                                    break
                        m = m + 1
            if contName==int(self.projects[namePro]["rls"]):
                check = True
            else: check = False
        return check
    def controlTheScript(self):
        """
        control the script and handle exceptions
        :return:
        """
        temp = []
        projects = self.namePro
        while(len(projects)>1):
            p = 0
            for x in projects:
                p= p +1
                if x not in self.completed:
                    status = self.worker(x) #if true then add to completed later
                    if status == True:
                        self.completed.append(x)
                        break
                    else:
                        pass
            if (len(self.namePro)==p or len(self.completed)==len(self.namePro)):
                break
        self.outputTheSolution()
    def outputTheSolution(self):
        """
        needed: self.completed / self.projects
        print out the solution
        :return:
        """
        file = open("submition.txt",'w+')
        file.write("")
        file.close()
        file = open("submition.txt",'a+')
        file.write(str(len(self.completed))+"\n")
        for project in self.completed:
            file.write(f"{project}\n{self.projects[project]['inv']}\n")
def main():
    """
    main function that control the script
    """
    contributors,projectsNbr = input().split(" ")
    contributors,projectsNbr = int(contributors),int(projectsNbr)
    contrByNamesAndSkills = {}
    projects = {}
    nameOfCont = []
    nameOfProjects = []
    for i in range(contributors):
       name,nbrOfSkills = input().split(" ")
       nbrOfSkills = int(nbrOfSkills)
       skills = []
       for _i_ in range(nbrOfSkills):
           skill= list(input().split(" "))
           skill[1] = int(skill[1])
           skills.append(skill)
       contrByNamesAndSkills[name]= skills
       nameOfCont.append(name)
    for i in range(projectsNbr):
        info = {}
        name,day,score,bestDay,roles = input().split(" ")
        info["day"] = day
        info["score"] = score
        info["bd"] = bestDay
        info["rls"] = roles
        skills = []
        for _i_ in range(int(roles)):
            skills.append(list(input().split(" ")))
        info["req"]=skills
        projects[name]= info
        nameOfProjects.append(name)
    hashcode(contrByNamesAndSkills,projects,nameOfCont,nameOfProjects).controlTheScript()
main()
