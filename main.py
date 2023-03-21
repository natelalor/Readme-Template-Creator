

from time import sleep


def main():

    project_overview = ""

    print("--------------------------")
    print("Welcome to the Readme Template Creator. You will be prompted with a few small free-response questions that will help define the content of the readme. Once you finish the prompts, it will generate a file for you that contains all of your information as a beautifully made markdown file (.md) that you can then use as a readme.")
    print("The goal of this project is to assist you in making a useful and informative readme for projects to save you the trouble.")
    print("--------------------------")
    sleep(10)
    # ========= inputs start here ==========
    # title input
    title = print(input("To start out, give your project a title. Keep it as short as you can, 2 to 3 words:\n"))
    # overview input
    project_overview = print(input(
        "Now, describe what project you made. Keep this as specific as you can. Recommended 3-5 sentences. Explain it like a short elevator pitch to a colleague or friend:\n"))

    # developers list input
    developers_str = print(input("Next, say the full names (first & last) of everyone on your team (including you). If this was a solo project, say only your full name. Separate full names with commas and spaces! Example input: Nate Lalor, Johnny Appleseed, Hi Mom:\n"))
    # this turns developers input into a list of strings
    developers_list = developers_str.split(", ")

    # materials input
    materials = print(input("Now, please write about the materials you used. Please use complete sentences and make it as detaied and thorough as you can. If this was a physical project, (i.e., involving hardware), you may list the hardware used. If this was software, or otherwise in cyberspace, now is the time to list out your language(s) used, specifics about your programming, libraries used, APIs, or other relevant information here:\n"))

    # main process input
    process = print(input("Explain your process here. How long did the project take? Was it for a class, or in your free time? What obstacles did you face, how did you triumph? What worked well? What didn't work well? Concluding thoughts? Etc:\n"))

    # extra info input
    extra_info = print(input("Finally, here is the place to put a link to learn more. Maybe a source you used, or a website you've created, or a link where the reader can learn more. If this is not needed, just press enter and skip this input:\n"))

    print("-----------------")
    print("\n")
    print("Thank you! Your data will now be processed...")

    md_file = formatter(title, project_overview, developers_list,
                        materials, process, extra_info)

    # TO DO: open an md file here
    # named README.md
    # add md_file contents to file
    # tell user heres your md file!
    # now you can add it to your project and upload it to your GitHub, GitLab, or more!

    #COMMENTED OUT FOR TESTING:
    # fo = open("WOWREADME.md" , "w")
    # fo.write(md_file)
    # fo.close()
    # print("Your new beautiful readme has been created with the name \"WOWREADME.md\"! You can now add it
    #           to your project and upload it to your GitHub, GitLab, or more! Enjoy!")

def formatter(title, project_overview, developers_list, materials, process, extra_info):
    md_file = ""
    extra_info_bool = True
    # waits a few seconds to send user another update
    sleep(2)
    print("Data Received...")

    # to catch if the user did not add any extra info
    if (extra_info == "" or extra_info == " "):
        # scrap extra info section here
        extra_info_bool = False

    # =========== FILE FORMATTING BEGINS ============


    if (extra_info_bool):
        # dont print this, but just add it
        print("Want to learn more? You're in luck! ")


    return md_file

main()
