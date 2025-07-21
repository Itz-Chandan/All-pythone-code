#!/bin/bash

# Define an array of tools to check and install
tools=("git" "bash" "python3")

# Function to install a tool
install_tool() {
	local tool=$1 # tool name passed as argument

	echo "$tool is not installed. Installing $tool..."

	# Check for macOS or Linux and install accordingly
	if [[ "$(uname)" == "Drawin" ]]; then
		brew install $tool
	elif [[ "$(uname)" == "Linux" ]]; then
		sudo apt update
		sudo apt install -y $tool
	else
		echo "Unspported OS. Cannot install $tool."
		return 1
	fi

	# Verify installation
	if command -v $tool $> /dev/null; then
		echo "$tool has been installed successfully."
	else
		echo "Failed to install $tool. please check your system or package manager."
	fi
}

# Loop through each tool in the tools array

for tool in "${tools[@]}"; do
	if command -v $tool $> /dev/null; then
		echo "$tool is already installed."

	else
		install_toll $tool #call the function to install the tool
	fi
done

# Final completion massage
echo "Installation check complete."
