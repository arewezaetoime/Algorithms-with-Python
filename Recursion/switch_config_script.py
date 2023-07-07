import paramiko

# Switch details

switches = [

    {"host": "192.168.1.1", "username": "admin", "password": "password"},

    {"host": "192.168.1.2", "username": "admin", "password": "password"},

    # Add more switches here

]


# SSH connection function
def connect_ssh(host, username, password):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, username=username, password=password)

    return client


# Save configuration

def save_configuration(switch):
    try:

        ssh_client = connect_ssh(switch["host"], switch["username"], switch["password"])
        ssh_shell = ssh_client.invoke_shell()

        # Send commands to save configuration and export it to a file

        ssh_shell.send("terminal length 0\n")  # Disable pagination
        ssh_shell.send("copy running-config flash:backup_config.txt\n")  # Save configuration to file

        output = ""

        while not output.endswith("#"):  # Wait for command execution to complete

            output += ssh_shell.recv(4096).decode("utf-8")

        # Check if the configuration was successfully saved

        if "bytes copied" in output:
            print(f"Configuration saved for {switch['host']}")
        else:
            print(f"Failed to save configuration for {switch['host']}")

        ssh_client.close()

    except paramiko.AuthenticationException:
        print(f"Authentication failed for {switch['host']}")

    except paramiko.SSHException as ssh_ex:
        print(f"SSH connection failed for {switch['host']}: {ssh_ex}")


# Backup configurations for all switches

for switch in switches:
    save_configuration(switch)
