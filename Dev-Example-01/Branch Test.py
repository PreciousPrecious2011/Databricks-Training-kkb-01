# Databricks notebook source
## Check Age
def check_eligibility(age):
    if age >= 18:
        print("You are eligible to work here!")
    else:
        print("Sorry, you are not eligible to work here.")

# Get user input for age
user_age = int(input("Enter your age: "))

# Call the function to check eligibility
check_eligibility(user_age)

