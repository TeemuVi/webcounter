*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
test Setup  Reset Application And Go To Home Page

*** Test Cases ***
set number test
    Go To  ${HOME_URL}
    Input Text  value  10
    Click Button  Aseta
    Page Should Contain  nappia painettu 10 kertaa
