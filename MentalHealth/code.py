import matplotlib.pyplot as plt
import pandas as pd
#store the mh.csv file in a location and specify it in the file path

# Choice #1: Age and Hours Analysis
def age_hours():
    #Update the file path
    file_path = r'C:\Users\Hp\Desktop\mh.csv'
    df = pd.read_csv(file_path, usecols=["Age", "Hours per day"])
    df_sorted = df.sort_values(by=['Age'])
    class_intervals = [11, 21, 31, 41, 51, 61, 71, 81, 91]
    df_sorted['Age Group'] = pd.cut(
        df_sorted['Age'], 
        bins=class_intervals, 
        labels=['10-20', '20-30', '30-40', '40-50', '50-60', '60-70', '70-80', '80-90']
    )
    age_group_hours = df_sorted.groupby('Age Group')['Hours per day'].mean()
    age_group_hours.plot(kind='pie', autopct='%1.1f%%', startangle=140)
    plt.ylabel('')
    plt.title("Average Hours Spent per Day by Different Age Groups")
    plt.legend(loc="best", title="Age Groups")
    plt.show()

# Choice #2: Favorite Genre Analysis
def fav_genre():
    #Update the file path
    file_path = r'C:\Users\Hp\Desktop\mh.csv'
    df1 = pd.read_csv(file_path, usecols=["Fav genre"])
    a = df1['Fav genre'].value_counts()
    a.plot(kind="bar", color=["b", "m"])
    plt.title("Favorite Genre")
    plt.show()

# Choice #3: Most Used App (Primary Streaming Service)
def app_preferance():
     #Update the file path
    file_path = r'C:\Users\Hp\Desktop\mh.csv'
    df1 = pd.read_csv(file_path, usecols=["Primary streaming service"])
    counting = df1['Primary streaming service'].value_counts()
    counting.plot(kind="bar", color=["b", "c"])
    plt.legend()
    plt.title("Favorite Streaming Service")
    plt.show()

# Choice #4: Music Preference While Working
def music_preferance():
    #Update the file path
    file_path = r'C:\Users\Hp\Desktop\mh.csv'
    df1 = pd.read_csv(file_path, usecols=["While working"])
    a = df1['While working'].value_counts()
    a.plot(kind="pie", autopct='%1.1f%%')
    plt.title("Preference of Music While Working")
    plt.show()

# Choice #5: Anxiety Analysis
def anxiety():
    #Update the file path
    file_path = r'C:\Users\Hp\Desktop\mh.csv'
    df1 = pd.read_csv(file_path, usecols=["Anxiety"])
    b = df1['Anxiety'].value_counts()
    b.plot(kind="barh")
    plt.legend()
    plt.title("Effectiveness of Music on Anxiety")
    plt.show()

# Choice #6: Depression Analysis
def depression():
     #Update the file path
    file_path = r'C:\Users\Hp\Desktop\mh.csv'
    df1 = pd.read_csv(file_path, usecols=["Depression"])
    a = df1['Depression'].value_counts()
    a.plot(kind="pie", autopct='%1.1f%%')
    plt.title("Effectiveness of Music on Depression")
    plt.show()

# Choice #7: Insomnia Analysis
def insomnia():
     #Update the file path
    file_path = r'C:\Users\Hp\Desktop\mh.csv'
    df1 = pd.read_csv(file_path, usecols=["Insomnia"])
    c = df1['Insomnia'].value_counts()
    c.plot(kind="pie", autopct='%1.1f%%')
    plt.title("Effectiveness of Music on Insomnia")
    plt.show()

# Choice #8: OCD Analysis
def ocd():
    #Update the file path
    file_path = r'C:\Users\Hp\Desktop\mh.csv'
    df1 = pd.read_csv(file_path, usecols=["OCD"])
    d = df1['OCD'].value_counts()
    d.plot(kind="bar", color=["g", "r"])
    plt.legend()
    plt.title("Effectiveness of Music on OCD")
    plt.show()

# Choice #9: People's Opinion on Effectiveness of Music
def music_effect():
    #Update the file path
    file_path = r'C:\Users\Hp\Desktop\mh.csv'
    df1 = pd.read_csv(file_path, usecols=["Music effects"])
    counts = df1['Music effects'].value_counts()
    counts.plot(kind='pie', autopct='%1.1f%%')
    plt.title("Population's Opinion on Effectiveness of Music")
    plt.show()

# Main Menu to Choose Multiple Analyses
def main_menu():
    while True:
        print("\nPlease choose an option:")
        print("1. Age and Hours Analysis")
        print("2. Favorite Genre Analysis")
        print("3. Most Used App (Streaming Service)")
        print("4. Music Preference While Working")
        print("5. Anxiety Analysis")
        print("6. Depression Analysis")
        print("7. Insomnia Analysis")
        print("8. OCD Analysis")
        print("9. People's Opinion on Effectiveness of Music")
        print("0. Exit")  # Option to exit

        # Allow user to enter multiple choices separated by commas
        choices = input("Enter the numbers corresponding to your choices : ").split(',')

        for choice in choices:
            choice = choice.strip()  
          # Remove any extra spaces
            if choice == "1":
                age_hours()
            elif choice == "2":
                fav_genre()
            elif choice == "3":
                app_preferance()
            elif choice == "4":
                music_preferance()
            elif choice == "5":
                anxiety()
            elif choice == "6":
                depression()
            elif choice == "7":
                insomnia()
            elif choice == "8":
                ocd()
            elif choice == "9":
                music_effect()
            elif choice == "0":
                print("Exiting the program.")
                return  
            else:
                print(f"Invalid choice: {choice}. Please enter a number between 0 and 9.")

if __name__ == "__main__":
    main_menu()
