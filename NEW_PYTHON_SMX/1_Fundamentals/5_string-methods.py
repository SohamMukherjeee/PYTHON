course='soham mukherjee'
print(course.upper()) ##---> SOHAM MUKHERJEE
print(course.title()) ##---> Soham Mukherjee



course1='    soham mukherjee'
print(course1) ##--->     soham mukherjee  .. you can empty spaces before text
print(course1.strip()) ##-->soham mukherjee  .. empty spaces removed because .stipe function


course2='soham mukherjee'
print(course2.find("mukh")) ###-------> 6
print(course2.find("Mukh")) ###-------> -1, unable to find because of m is capital Here,
print(course2.replace("m","l")) ##----> sohal lukherjee
print("mukh" in course2)


