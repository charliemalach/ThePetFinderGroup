import click
from methods import methods

# The PetFinder Group
# @author Charlie Malachinski
# @version 1.0.0
# @since 10-28-22
# This file is used as the main class 'driver' file. Has mostly the Click commands and their respective options. Uses methods from 'methods.py'

# creates a group using Click and adds help option to the group 
@click.group()
@click.help_option('--help', help='Displays this screen and all available commands.')

# sorry for the awkward formatting in the text, I thought it would bea nice touch for the UI d:^)~
def main():
    """------------------------------ \n
\n### The PetFinder Group. ###  \n \n
\n - We are dedicated to finding forever homes for beautiful cats. \n
\n - Here are some of the basic commands for using our program. \n
------------------------------"""
    pass

# this command shows the list of cats filtered by AGE with the option to save the filtered list of cats to a CSV
@click.command()
@click.option("--age", prompt="Enter the desired age", help="The age of the cat", type=int)
@click.option("--save", help="Saves the data to a new path", is_flag=True) #option to save results to CSV
def age(age, save):
    """Simple command that filters cats based on AGE."""
    payload = {"age": age}
    result = methods.filter_data(payload) #filters through data based on age
    methods.results(result, save)

# this command shows the list of cats filtered by COLOR with the option to save the filtered list of cats to a CSV
@click.command()
@click.option("--color", prompt="Enter the desired color", help="The color of the cat")
@click.option("--save", help="Saves the data to a new path", is_flag=True) #option to save results to CSV
def color(color, save):
    """Simple command that filters cats based on COLOR."""
    color = methods.format_text(color) #formats the color 
    payload = {"color": color}
    result = methods.filter_data(payload) #filters through data based on color
    methods.results(result, save)

# this command shows the list of cats filtered by being DECLAWED with the option to save the filtered list of cats to a CSV
@click.command()
@click.option("--declaw", prompt="Do you want a cat that is declawed? (Y/N)", help="Determines if the cat is declawed or not.")
@click.option("--save", help="Saves the data to a new path", is_flag=True) #option to save results to CSV
def declawed(declaw, save):
    """Simple command that filters cats based on being DECLAWED."""
    declaw = methods.format_text(declaw) #formats the text for declaw 
    payload = {"declawed": declaw}
    result = methods.filter_data(payload) #filters through data based on cat being declawed 
    methods.results(result, save)

# this command shows the list of cats filtered by GENDER with the option to save the filtered list of cats to a CSV
@click.command()
@click.option("--gender", prompt="Enter the desired gender (M/F)", help="The gender of the cat")
@click.option("--save", help="Saves the data to a new path", is_flag=True) #option to save results to CSV
def gender(gender, save):
    """Simple command that filters cats based on GENDER."""
    gender = methods.format_text(gender) #formats the gender 
    payload = {"gender": gender}
    result = methods.filter_data(payload) #filters through data based on gender
    methods.results(result, save)

# this command shows the list of cats filtered by NAME with the option to save the filtered list of cats to a CSV
@click.command()
@click.option("--name", prompt="Enter the desired name", help="The name of the cat")
@click.option("--save", help="Saves the data to a new path", is_flag=True) #option to save results to CSV
def name(name, save):
    """Simple command that filters cats based on NAME."""
    name = methods.format_text(name) #formats the name 
    payload = {"name": name}
    result = methods.filter_data(payload) #filters through data based on name
    methods.results(result, save)

# this command shows the original list of ALL cats with the option to save ALL cats as a CSV
@click.command()
@click.option("--save", help="Saves the data to a new path", is_flag=True)
def list(save):
    """Simple command that lists ALL original cats."""
    result = methods.filter_data() #fetches original data
    methods.results(result, save)

# add all commands to the CLI
main.add_command(age)
main.add_command(color)
main.add_command(declawed)
main.add_command(gender)
main.add_command(list)
main.add_command(name)

# driver the cause main to run
if __name__ == "__main__":
    main()