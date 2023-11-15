*** Settings ***
Resource  resource.robot
Resource  login_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  maria
    Set Password  kalle123
    Confirm Password  kalle123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  em
    Set Password  salasana1
    Confirm Password  salasana1
    Submit Credentials
    Register Should Fail With Message  Username has to contain atleast 3 characters

Register With Valid Username And Invalid Password
    Set Username  anni
    Set Password  salasana
    Confirm Password  salasana
    Submit Credentials
    Register Should Fail With Message  Password cannot contain only letters

Register With Nonmatching Password And Password Confirmation
    Set Username  matti
    Set Password  salasana1
    Confirm Password  salasana2
    Submit Credentials
    Register Should Fail With Message  Passwords do not match

Login After Successful Registration
    Set Username  emmi
    Set Password  emmi1234
    Confirm Password  emmi1234
    Submit Credentials
    Register Should Succeed
    Click Link  Continue to main page
    Click Button  Logout
    Set Username  emmi
    Set Password  emmi1234
    Submit Login Credentials
    Login Should Succeed

Login After Failed Registration
    Set Username  em
    Set Password  salasana1
    Confirm Password  salasana1
    Submit Credentials
    Click Link  Login
    Set Username  em
    Set Password  salasana1
    Submit Login Credentials
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Register

Submit Login Credentials
    Click Button  Login

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Confirm Password
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}
    
Open Register Page
    Go To Register Page
    Register Page Should Be Open  