*** Settings ***
Library    ../CustomLibrary.py

*** Test Cases ***
Change Theme And Underline Text
    Open Url
    Reject Cookies
    Change Theme
    Style Underline
    Take Screenshot
    Close Browser