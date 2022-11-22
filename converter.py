import os

os.add_dll_directory(r"C:/Program Files/GTK3-Runtime Win64/bin")
from md2pdf.core import md2pdf
from git import Repo

localrepo = os.path.join(os.getcwd(),'')
destination = 'main'


""" def clone_repo():
    if os.path.exists(localrepo):
        repo = Repo(localrepo)
        origin = repo.remotes.origin
        origin.pull(destination)
    else:
        Repo.clone_from("https://github.com/geromedw/python.git",localrepo, branch=destination) """

def comandpush(repo):
    
    repo.git.add(update=True)
    repo=Repo(localrepo)
    origin = repo.remotes.origin
    origin.push()
    repo.git.commit("-m", "updating files")
    print("succesfully updated")


directory = 'input'

pdffilelist = []
mdfilelist = []
# iterate over files in
# that directory
for filename in os.listdir(directory):
    mdfile = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(mdfile):
        print(mdfile)
        mdfilelist.append(mdfile)
        pdfname = mdfile.replace("input","output",1)
        pdfname = pdfname[0:-2] + "pdf"
        print(pdfname)

        md2pdf(pdfname,
              md_content=None,
              md_file_path=mdfile,
              css_file_path="input.css",
              base_url=None)
       
        pdffilelist.append(pdfname)
    

with open("template.html","r",encoding='utf-8') as htmlfile:
    htmldata = (htmlfile.read())
    htmllist = ""
    x = 0
    for file in mdfilelist:
         htmllist += f"md file is <a href=\{mdfilelist[x]}> {mdfilelist[x]} </a>" +  "<br>" + f"pdf file is <a href=\{pdffilelist[x]}> {pdffilelist[x]} </a>" "<br>" + "\n" + "<br>"
         x+=1
    
    htmldata = htmldata.replace("data",htmllist)

    with open("index.html","w") as htmloutput:
        htmloutput.write(htmldata)

repo = Repo(localrepo)
comandpush(repo)

#installeer GTK3-runtime
#werkt niet zonder