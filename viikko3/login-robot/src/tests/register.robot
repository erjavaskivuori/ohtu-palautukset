*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  pekka  pekka123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  salasana1
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  ka  kalle123
    Output Should Contain  Username has to contain atleast 3 characters

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials  kalle1  kalle123
    Output Should Contain  Username should only contain letters a-z

Register With Valid Username And Too Short Password
    Input Credentials  laura  la1
    Output Should Contain  Password has to contain atleast 8 characters

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  maria  salasana
    Output Should Contain   Password cannot contain only letters

*** Keywords ***
Input New Command And Create User
    Create User  kalle  kalle123
    Input New Command
