import requests

# Function to log in to Kobo Toolbox and retrieve an Excel file
def login_and_get_excel(username, password, form_id, file_name):
    # Log in to Kobo Toolbox
    login_url = 'https://kc.kobotoolbox.org/accounts/login/'
    session = requests.Session()
    login_data = {'username': username, 'password': password}
    session.post(login_url, data=login_data)

    # Retrieve the Excel file
    excel_url = f'https://kc.kobotoolbox.org/assets/{form_id}/export.xlsx'
    response = session.get(excel_url)

    # Save the Excel file
    with open(file_name, 'wb') as file:
        file.write(response.content)

    print('Excel file downloaded successfully!')

# Example usage
username = 'your_username'
password = 'your_password'
form_id = 'your_form_id'
file_name = 'output.xlsx'

login_and_get_excel(username, password, form_id, file_name)
