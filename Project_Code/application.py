from choice import show_menu
from functions import *

# Exploratory Data Analysis

#Taking choice Input
choice = show_menu()

if choice==1:
    statistics()
elif choice==2:
    category_save()
elif choice==3:
    whole_save()
elif choice==4:
    categorical_visual()
elif choice==5:
    full_visual()
else:
    print("wrong choice")
















