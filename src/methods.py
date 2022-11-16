import json
import click
import requests
import pandas as pd
import sys
from requests.exceptions import ConnectionError

# The PetFinder Group
# @author Charlie Malachinski
# @version 1.0.0
# @since 10-28-22
# This class file is used to host the methods that are used by the main class file. 

# sets the localhost server as the endpoint for the program
URL = "http://localhost:3000/cats"

class methods:
    # function to return the data with filter arguments  
    def filter_data(selection = None):
        try: 
            request = requests.get(URL, params=selection)
            return request.content
        # i was running into an error when the server was not running, so now there is a reminder for users to run the server before executing commands 
        except ConnectionError:
                methods.print_bar()
                print("ERROR! Could not connect to JSON SERVER. Please run 'server-run.bat' and try again.")
                methods.print_bar()
                sys.exit(3)
            
    # function to filter the entry by the user. takes care of the case that user enters CAPS vs lowercase.
    def format_text(entry):
        entry = entry.lower().capitalize()
        return entry

    # function to print bars just for the aesthetics of the command prompt 
    def print_bar():
        print("---------------------------------------------------------------------------------------------")

    #function to convert the json response to a CSV
    def convert_csv(response):
        output = json.dumps(response.decode('utf-8'))
        json_data = json.loads(output)
        df = pd.read_json(json_data)
        return df 

    # displays the filtered results as csv (i think this looks MUCH better)
    def display_results(response):
        methods.print_bar()
        print("Here are your results: ")
        methods.print_bar()
        df = methods.convert_csv(response)
        if df.empty:
            click.echo('Error: No results matched your criteria. Please try again with different criteria.')
        else:
            click.echo(df.to_csv(index=False))
            
    # function to save the search response to a CSV
    def save_csv(response):
        df = methods.convert_csv(response)
        file = input("Please name new CSV output:")
        df.to_csv('../results/'+ file + '.csv', index=False)
        click.echo("Success! Your results have been saved to " + file + ".csv.")

    #function to print results and save
    def save_results(response):
        methods.display_results(response)
        methods.save_csv(response)

    # final function to save and print or just print results  
    def results(response, save = None):
        if not save:
            methods.display_results(response)
            methods.print_bar()
        else:
            methods.save_results(response)
            methods.print_bar()